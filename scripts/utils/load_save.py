#created by: aime nishimwe
#created at: Avery Hall, UNL
#created on: Monday, March 21 2022

import sys
import os
import pandas as pd
import numpy as np
import json
sys.path.insert(0,"config/")
from definitions import ROOT_DIR

def load_data(tp:str,name:str, sorghum = False) ->pd.core.frame.DataFrame:
    '''
    Given the name of a dataframe,
    And base = False/True, to indicate whether the dataframe is part of the base population data,
    The function reads the pickle file corresponding to the name of dataframe
    '''
    df = None
    path = data_path(tp,name,sorghum)
    return pd.read_csv(path, index_col = 0)



    ## TODO: try--except for keyerror and filenotfounderror

def batch_load(tp:str, names:list, sorghum = False) -> pd.core.frame.DataFrame:
    '''
    Given a list of named dataframe
    Base: indication whether just data or base population data
    Load several pickle files and return a list
    '''
    frames = dict()
    for name in names:
        frames[name] = load_data(tp,name,sorghum)
    return frames

def data_path(tp, name,sorghum = False):

    jsn = None
    path= None

    data_paths = os.path.join(ROOT_DIR, 'data','paths.json')
    try:
        with open(data_paths)as f:
            jsn = json.load(f)
    except FileNotFoundError:
        raise Exception('path.json file was not found.')

    match tp:
        case "raw":
            if sorghum:
                path = jsn['raw'][0]['sorghum'][name]
            elif not sorghum:
                path = jsn['raw'][0]['maize'][name]

        case "preprocessed":
            if sorghum:
                path = jsn['preprocessed'][0]['sorghum'][name]
            elif not sorghum:
                path = jsn['preprocessed'][0]['maize'][name]

        case "train_test":
            if sorghum:
                path = jsn['train_test'][0]['sorghum'][name]
            elif not sorghum:
                path = jsn['train_test'][0]['maize'][name]

        case _:
            print("None of the cases were met!")
    return path



def save_data(tp:str, name:str, df, sorghum = False):
    rt_path = os.path.join(ROOT_DIR, 'data','paths.json')
    with open(rt_path, 'r') as f:
        jsn = json.load(f)
        df_path = data_path(tp, name, sorghum)
        df.to_csv(df_path)

def batch_save(tp:str,dfs:dict, sorghum = False):
    for name, df in dfs.items():
        save_data(tp, name, df, sorghum)

if __name__ == '__main__':
    df = load_data('raw','field_map', sorghum = True)
    print (df.head(5))
