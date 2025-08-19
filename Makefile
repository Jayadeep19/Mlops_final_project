export PIPENV_VENV_IN_PROJECT := 1


env_setup:
	@echo 'Building python environment for the project...'
	pip install pipenv
	pipenv install --python 3.11
	pipenv run python ./src/prep_data.py

mlflow:
	@echo 'Starting ml flow server with backend artifact storage'
	pipenv run mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifacts_local

prefect:
	@echo 'Running prefect server'
	pipenv run prefect server start
	pipenv run prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

make_deployment:
	@echo 'Deploying workflow using pool with prefect and yaml file'
	#pipenv run prefect work-pool delete ore_quality_prediction_pool
	pipenv run prefect work-pool create --type process ore_quality_prediction_pool
	pipenv run prefect deploy --name ore_quality_prediction_deployment
	pipenv run prefect worker start --pool 'ore_quality_prediction_pool'
	@echo 'Now run the deployment from gui'

web_service:
	@echo 'Creating docker container for model deployment (as web service)'
	@echo 'open new terminal and run'
	@echo 'cd web_service'
	pipenv run docker build -f Dockerfile -t ore-quality-prediction:v1 .
	pipenv run docker run -it --rm -p 9696:9696 ore-quality-prediction:v1
	@echo 'open a new terminal and run'
	@echo 'python test.py'

monitoring:
	@echo 'Starting monitoring with evidently and grafana dashboards'
	docker-compose -f ./monitoring/docker-compose.yaml up --build
	@echo 'Open a new terminal and run'
	@echo 'cd monitoring'
	@echo 'python generate_evidently_metrics.py'

reset:
	@echo 'Cleaning the project directory'
	rm -rf __pycache__
	rm -rf data
	rm -rf mlruns
	rm -rf artifacts_local
	rm -rf backend.db
	pipenv --rm
