import pytest
import os
import pandas as pd
from calculator.history import History

@pytest.fixture
def history():
    # Create a temporary History object with a test CSV file
    return History(filename='test_history.csv')

def test_add_record(history):
    history.add_record('add', 1, 2, 3)
    assert len(history.df) == 1
    assert history.df.iloc[0]['operation'] == 'add'
    assert history.df.iloc[0]['a'] == 1
    assert history.df.iloc[0]['b'] == 2
    assert history.df.iloc[0]['result'] == 3

def test_clear_history(history):
    history.add_record('add', 1, 2, 3)
    history.clear_history()
    assert len(history.df) == 0

def test_load_history(history):
    history.add_record('add', 1, 2, 3)
    history.add_record('subtract', 5, 3, 2)
    history.df.to_csv(history.filename, index=False)

    new_history = History(filename='test_history.csv')
    assert len(new_history.df) == 2
    assert new_history.df.iloc[0]['operation'] == 'add'
    assert new_history.df.iloc[1]['operation'] == 'subtract'

def test_save_history(history):
    history.add_record('add', 1, 2, 3)
    history.df.to_csv(history.filename, index=False)
    loaded_df = pd.read_csv(history.filename)
    assert len(loaded_df) == 1
    assert loaded_df.iloc[0]['operation'] == 'add'
    assert loaded_df.iloc[0]['a'] == 1
    assert loaded_df.iloc[0]['b'] == 2
    assert loaded_df.iloc[0]['result'] == 3

def teardown_function(function):
    # Clean up the test CSV file after each test
    if os.path.exists('test_history.csv'):
        os.remove('test_history.csv')
