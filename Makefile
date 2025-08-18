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
