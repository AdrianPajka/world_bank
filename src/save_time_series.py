import os

import pandas as pd

directory: str = os.getcwd()
path: str = os.path.join(directory, 'saved_time_series')


def save_data(dataframe: pd.DataFrame, filename: str) -> None:
    if 'saved_time_series' not in os.listdir(directory):
        os.mkdir(path)

    df = dataframe.rename_axis('date').reset_index()
    df.to_csv(os.path.join(path, f'{filename}.csv'))
