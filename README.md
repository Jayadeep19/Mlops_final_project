To remember:
1. Remember to include the steps for precommit hook generation
2. Add the other tools to the precommit hook at the end of the project


##Dataset:
1 use `curl -L -o ./data/mining_dataset2.zip\
  https://www.kaggle.com/api/v1/datasets/download/edumagalhaes/quality-prediction-in-a-mining-process`


Start of actual Documentation:
# Add the title
-Add the description about the dataset and the purpose of the peoject

## Describe requirments
- python version etc....
- all the services included in this project..
- check others readme style to include more information

## Setup and Usage
### 1. Setting us the environment and getting data
- To prepare the environment run: __make env_setup__ (_python3.11_ is required for successful installation)
  ```
  env_setup:
	@echo 'Building python environment for the project...'
	pip install pipenv
	pipenv install --python 3.11
	pipenv run python ./src/prep_data.py
  ```
