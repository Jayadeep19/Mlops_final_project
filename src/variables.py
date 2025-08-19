from pathlib import Path

#data paths locally and dataset url
PROJECT_DIR = Path(__file__).absolute().parent.parent
DATA_PATH = PROJECT_DIR.joinpath('data')
DATASET_URL = 'https://www.kaggle.com/api/v1/datasets/download/edumagalhaes/quality-prediction-in-a-mining-process'
RAW_DATA_PATH = DATA_PATH.joinpath('raw', 'MiningProcess_Flotation_Plant_Database.csv')
TRAIN_DATA_PATH = DATA_PATH.joinpath('processed_data','train.pkl')
TEST_DATA_PATH = DATA_PATH.joinpath('processed_data','test.pkl')
VAL_DATA_PATH = DATA_PATH.joinpath('processed_data','val.pkl')
TESTING_DATA = PROJECT_DIR.joinpath('tests', 'test_data')

#features and targets obtained from EDA
air_flow = ['Flotation Column 01 Air Flow', 'Flotation Column 02 Air Flow', 'Flotation Column 03 Air Flow', 'Flotation Column 04 Air Flow', 'Flotation Column 05 Air Flow', 'Flotation Column 06 Air Flow', 'Flotation Column 07 Air Flow']
froth_lvl =['Flotation Column 01 Level', 'Flotation Column 02 Level', 'Flotation Column 03 Level', 'Flotation Column 04 Level', 'Flotation Column 05 Level', 'Flotation Column 06 Level', 'Flotation Column 07 Level']
features = ['% Iron Concentrate', 'Amina Flow', 'Ore Pulp pH', 'Average Air Flow']
target = '% Silica Concentrate'

# ml model parameters
model_params = {"n_estimators": 10,
                "max_depth": 10,
                "min_samples_split": 2,
                "min_samples_leaf": 1,
                "random_state": 42}

#mlflow variables
MLFLOW_TRACKING_URI = 'sqlite:///backend.db'
MLFLOW_EXPERIMENT_NAME = 'iron_ore_quality_prediction'
MLFLOW_MODEL_NAME = 'ore_quality_regression_model'
REGISTERED_MODEL = {"run_id":None,
                    "model_uri":None}
