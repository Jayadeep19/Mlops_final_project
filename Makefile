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
	pipenv run prefect work-pool delete ore_quality_prediction_pool
	pipenv run prefect work-pool create --type process ore_quality_prediction_pool
	pipenv run prefect deploy --name ore_quality_prediction_deployment
	pipenv run prefect worker start --pool 'ore_quality_prediction_pool'
	@echo 'Now run the deployment from gui'
