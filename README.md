# Iron Ore Quality Prediction
This project is the *Iron Ore Quality Prediction in a Mining Process*, the dataset from [Eduardo MagalhãesOliveira](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process/data), a Kaggle user. The information was obtained from a flotation facility, a typical method of iron ore concentration. Finding out if we can forecast the ore concentrate's silica impurity concentration (% Silica Concentrate) is the main goal of the analysis.

Predicting the amount of impurities in the ore concentrate using this data is the primary objective.  Since this impurity is monitored hourly, we can assist the engineers by providing them with early knowledge to take action (empowering!) if we can estimate the amount of silica (impurity) in the ore concentrate.  As a result, they may take proactive remedial measures (reducing impurity, if applicable) and benefit the environment (cutting the quantity of ore that ends up as tailings, just as you reduce silica in the ore concentrate).

| date | % Iron Feed | % Silica Feed | Starch Flow | Amina Flow | Ore Pulp Flow | Ore Pulp pH | Ore Pulp Density | Flotation Column 01 Air Flow | Flotation Column 02 Air Flow | Flotation Column 03 Air Flow | Flotation Column 04 Air Flow | Flotation Column 05 Air Flow | Flotation Column 06 Air Flow | Flotation Column 07 Air Flow | Flotation Column 01 Level | Flotation Column 02 Level | Flotation Column 03 Level | Flotation Column 04 Level | Flotation Column 05 Level | Flotation Column 06 Level | Flotation Column 07 Level | % Iron Concentrate | % Silica Concentrate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2017-03-10 01:00:00 | 55.2 | 16.98 | 3019.53 | 557.434 | 395.713 | 10.0664 | 1.74 | 249.214 | 253.235 | 250.576 | 295.096 | 306.4 | 250.225 | 250.884 | 457.396 | 432.962 | 424.954 | 443.558 | 502.255 | 446.37 | 523.344 | 66.91 | 1.31 |
| 2017-03-10 01:00:00 | 55.2 | 16.98 | 3024.41 | 563.965 | 397.383 | 10.0672 | 1.74 | 249.719 | 250.532 | 250.862 | 295.096 | 306.4 | 250.137 | 248.994 | 451.891 | 429.56 | 432.939 | 448.086 | 496.363 | 445.922 | 498.075 | 66.91 | 1.31 |
| 2017-03-10 01:00:00 | 55.2 | 16.98 | 3043.46 | 568.054 | 399.668 | 10.068 | 1.74 | 249.741 | 247.874 | 250.313 | 295.096 | 306.4 | 251.345 | 248.071 | 451.24 | 468.927 | 434.61 | 449.688 | 484.411 | 447.826 | 458.567 | 66.91 | 1.31 |
| 2017-03-10 01:00:00 | 55.2 | 16.98 | 3047.36 | 568.665 | 397.939 | 10.0689 | 1.74 | 249.917 | 254.487 | 250.049 | 295.096 | 306.4 | 250.422 | 251.147 | 452.441 | 458.165 | 442.865 | 446.21 | 471.411 | 437.69 | 427.669 | 66.91 | 1.31 |
| 2017-03-10 01:00:00 | 55.2 | 16.98 | 3033.69 | 558.167 | 400.254 | 10.0697 | 1.74 | 250.203 | 252.136 | 249.895 | 295.096 | 306.4 | 249.983 | 248.928 | 452.441 | 452.9 | 450.523 | 453.67 | 462.598 | 443.682 | 425.679 | 66.91 | 1.31 |

There are 22 columns(features) in the dataset as given in the above table
- Date: Date and Timestamp
- % Iron Feed: % of Iron that comes from the iron ore that is being fed into the flotation cells
- % Silica Feed: % of silica (impurity) that comes from the iron ore that is being fed into the flotation cells
- Starch Flow: Starch (reagent) Flow measured in m3/h
- Amina Flow: Amina (reagent) Flow measured in m3/h
- Ore Pulp Flow: t/h
- Ore Pulp pH: pH scale from 0 to 14
- Ore Pulp Density: Density scale from 1 to 3 kg/cm³
- Flotation Column 01-07 Air Flow: Air flow that goes into the flotation cell measured in Nm³/h
- Flotation Column 01-07 Level: Froth level in the flotation cell measured in mm (millimeters)
- % Iron Concentrate: % of Iron which represents how much iron is presented in the end of the flotation process (0-100%, lab measurement)
- % Silica Concentrate: % of silica which represents how much iron is presented in the end of the flotation process (0-100%, lab measurement).

The flotation columns for air flow and froth level are averaged out for easier understanding of tempporal dependencies and only the highly coorelating features are taken for training the ml model. See [EDA.ipynb](src/EDA.ipynb)

## Approch

A machine learning model is to be traind on the highly coorelated features to the target value. Containerize the model in a docker image and deploy locally as a web appkication. The model is monitored using Evidently metrics, store them in postgre sql database and visualised with grafana.

- [x] Unit testing
- [x]  Pre-commit hooks
- [x]  Formatter (isort, black)
- [x]  linter


## Describe requirments
- python version 3.11
- docker pre-installed

## Used tools
- mlflow: To track the experiments and register the best model to model registery
- Prefect: To orchestrate and automate the pipelines
- Docker: To containerize the applications
- evidently: To calculate the performance metrics of the model during deployment
- Grafana: To visuaise the evidently metrics in UI
- Flask: To send requests and recieve responses to and from the web server
- Pytest: To generate Unit tests
- Pylint: For linting and formatting
- Black and isort: Formatters
- makefile: To define the set of tasks to be executed for each service


## Setup and Usage
### 1. Setting us the environment and getting data
- To prepare the environment run: __make env_setup__
  ```
  env_setup:
	@echo 'Building python environment for the project...'
	pip install pipenv
	pipenv install --python 3.11
	pipenv run python ./src/prep_data.py
  ```
### 2. To start mlflow tracking server
- Run : __make mlflow__
```
mlflow:
	@echo 'Starting ml flow server with backend artifact storage'
	pipenv run mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifacts_local

```
This starts the tracking server. The model tracking and model registery were both implemented which is executed after the training is done [train.py](src/train.py) and look [register_model.py](src/register_model.py)

![](/images/mlflow.PNG)

### 3. Start a prefect server
- Run: __make prefect__
```
prefect:
	@echo 'Running prefect server'
	pipenv run prefect server start
	pipenv run prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

```

### 4. Fully deploy the workflow to perfect server
Run: __make deployment__
```
make_deployment:
	@echo 'Deploying workflow using pool with prefect and yaml file'
	#pipenv run prefect work-pool delete ore_quality_prediction_pool
	pipenv run prefect work-pool create --type process ore_quality_prediction_pool
	pipenv run prefect deploy --name ore_quality_prediction_deployment
	pipenv run prefect worker start --pool 'ore_quality_prediction_pool'
	@echo 'Now run the deployment from gui'
```
This starts the work pool named __ore_quality_prediction_pool__ and starts a deployment named __ore_quality_prediction_deployment__. Once the worker is started, head to the perfect server and hit `quick run` on the deployment. And the deployment starts.

![](/images/quick_run_prefect.PNG)
![](/images/prefect.PNG)

### 5. Make model available as webservice
- Run: __make web_service__
  ```
  web_service:
	@echo "Creating docker container for model deployment (as web service)"
	@echo "open new terminal and run"
	@echo "cd web_service"
	pipenv run docker build -f Dockerfile -t ore-quality-prediction:v1 .
	pipenv run docker run -it --rm -p 9696:9696 ore-quality-prediction:v1
	@echo 'open a new terminal and run'
	@echo 'python test.py'
  ```
  The model is containerized to be able to easily deploy locally and in further developments in cloud services as well. This will build an image named __ore-quality-prediction__ with tag __v1__. Then, it runs a container which is available at port-9696. Now, the requests can be sent to get the predictions.

### 6. Model monitoring:
- Run: __make monitoring__
  ```
  monitoring:
	@echo "Starting monitoring with evidently and grafana dashboards"
	docker-compose -f ./monitoring/docker-compose.yaml up --build
	@echo "Open a new terminal and run"
	@echo "cd monitoring"
	@echo "python generate_evidently_metrics.py"
  ```
  The model monitoring is done using evidently, postgres and grafana. A docker-compose.yaml is created with all the required services. The password for the table __ore_evidently_metrics__ is __admin__. And dashboard is created. See [monitoring](monitoring/)

### 7. Reset the project
- Run: __reset__
  ```
  reset:
	@echo 'Cleaning the project directory'
	rm -rf __pycache__
	rm -rf data
	rm -rf mlruns
	rm -rf artifacts_local
	rm -rf backend.db
	pipenv --rm
  ```
  Running this command will clean the entire project directory and sets it to the former condition. Note: This also removes the virtual_environment also
