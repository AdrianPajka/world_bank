import os

import pandas as pd
import pytest

from src.save_time_series import save_data


test_df = pd.DataFrame({'id': [1, 2, 3, 4], 'letters': ['a', 'b', 'c', 'd']})


@pytest.fixture
def create_remove():
    file_name = 'test_df'
    directory = os.getcwd()
    path = os.path.join(directory, 'saved_time_series')
    save_data(test_df, file_name)
    yield
    os.remove(os.path.join(path, f'{file_name}.csv'))
    os.rmdir(path)


def test_if_data_saved(create_remove):
    path = os.path.join(os.getcwd(), 'saved_time_series')

    assert 'test_df.csv' in os.listdir(path)
