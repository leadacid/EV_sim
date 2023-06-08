"""
This file contains codes to extract relevant information about the EV database.
"""
import os

import pandas as pd
from EV_sim.config import definations


def print_model_info(database_dir=os.path.join(definations.ROOT_DIR, 'data/EV/EV_dataset.csv')):
    df = pd.read_csv(database_dir, index_col=(0,1))
    list_alias = df.columns
    for alias in list_alias:
        print(f'''{df.loc[('basic vehicle', 'manufacturer'), alias]} {df.loc[('basic vehicle', 'year'), alias]} {df.loc[('basic vehicle', 'model_name'), alias]} {df.loc[('basic vehicle', 'trim'), alias]} : {alias}''')


print_model_info()