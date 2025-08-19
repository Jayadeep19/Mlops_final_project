from prefect import flow

import predict
import train
import variables as var


@flow(name = 'main flow for ore quality prediction')
def main_flow():

    client, _,_ = train.main()
    data = var.TEST_DATA_PATH
    # X_test.loc['% Silica Concentrate'] = y_test
    #data = X_test['% Silica Concentrate'] = y_test
    predictions = predict.predict(mlflow_client=client, data = data)
    print(f"Some of the predictions are {predictions[3]}")
    pass

if __name__ == "__main__":
    main_flow()
