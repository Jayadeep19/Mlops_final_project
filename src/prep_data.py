import os
import io
import requests
import zipfile
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split

import variables as var


def download_dataset(url, data_folder):

    os.makedirs(data_folder, exist_ok=True)
    ZIP_PATH = data_folder.joinpath("dataset.zip")

    for file in os.listdir(data_folder):
        if file == 'raw':
            for f in os.listdir(data_folder.joinpath('raw')):
                if f.endswith('csv'):
                    print("Raw dataset already exists, skipping the download again")
                    return True
                else:
                    continue
        elif file.endswith('.zip') and len(os.listdir(data_folder))==1:
            print('Found exisitng zip file for dataset')
            unzip(ZIP_PATH, data_folder)
            return True

    response = requests.get(url)
    if response.status_code == 200:
        with open(ZIP_PATH, 'wb') as file:
            file.write(response.content)
            print("Download completed successfully.")
    unzip(ZIP_PATH, data_folder)
    return True

def unzip(zip_path, data_folder):
    if os.path.exists(zip_path):
                if zipfile.is_zipfile(zip_path):
                    print("unzipping dataset")
                    with zipfile.ZipFile(zip_path, 'r') as zip_file:
                        for file in zip_file.namelist():
                            if file.endswith('.csv'):
                                zip_file.extract(file, data_folder.joinpath('raw'))
                                print("File extraction from the zip completed")


def run_prep_data(raw_data_path, dest_path):
    df = pd.read_csv(raw_data_path, decimal = ',')
    df = prep_data(df)
    train_df1, test_df = train_test_split(df, test_size=0.25, random_state=42)
    train_df, val_df = train_test_split(train_df1, test_size=0.2, random_state=42)

    target = var.target      #str

    X_train = train_df.drop(columns=[target])
    y_train = train_df[target]

    X_val = val_df.drop(columns = [target])
    y_val = val_df[target]

    X_test = test_df.drop(columns = [target])
    y_test = test_df[target]


    dump_pickle((X_train, y_train), dest_path.joinpath('processed_data','train.pkl'))
    dump_pickle((X_val, y_val), dest_path.joinpath('processed_data','val.pkl'))
    dump_pickle((X_test, y_test), dest_path.joinpath('processed_data','test.pkl'))
    write_txt(X_train, 'train_dataset')
    write_txt(X_val, 'val_dataset')
    write_txt(X_test, 'test_dataset')
    print("Data split and save as pickle files")
    return True

def prep_data(data):
    '''Takes the dataset and applies required filters and downsamples the dataset set as necessary
    1. Drop the duplicates
    2. convert the dates to datetime format
    3. Filter the data to every 5seconds. The distribution of the data remains similar to the original data after the downasampling (see EDA.ipynb)'''
    #remove duplicates
    #count_dup = data.duplicated(keep = False).sum()
    data = data.drop_duplicates()

    # convert the dates to datetime and filter the data to every minute
    data['date'] = pd.to_datetime(data['date'])
    data = data.set_index("date")
    data = data.resample("5S").first().dropna().reset_index()

    # average out the air flow and froth level columns
    air_flow = data[var.air_flow]
    froth_lvl = data[var.froth_lvl]
    data['Average Air Flow'] = air_flow.mean(axis=1).round(2)
    data['Average Froth Level'] = froth_lvl.mean(axis=1).round(2)
    data.insert(8, 'Average Air Flow', data.pop('Average Air Flow'))
    data.insert(9, 'Average Froth Level', data.pop('Average Froth Level'))
    col_to_drop = air_flow + froth_lvl
    data = data.drop(columns=col_to_drop)

    return data

def write_txt(df, type):
    '''save the info about the df into txt file'''
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    path = var.DATA_PATH.joinpath('processed_data', f'{type}.txt')
    with open(path, "w",
              encoding="utf-8") as f:
        f.write(s)
    return None

def dump_pickle(data, filename):
    '''Save the dataset as a pickel file.
    The data is in the form features, target values'''
    if not os.path.exists(filename.parent):
        os.makedirs(filename.parent)
    with open(filename, 'wb') as f_out:
        pickle.dump(data, f_out)
    pass



if __name__ == '__main__':

    data_folder = var.DATA_PATH
    download_dataset(var.DATASET_URL, data_folder=data_folder)
    run_prep_data(raw_data_path=var.RAW_DATA_PATH, dest_path=data_folder)
