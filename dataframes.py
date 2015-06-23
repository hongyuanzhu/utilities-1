import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

def equal_dfs(df1, df2):
    try:
        assert_frame_equal(df1.sort(axis=1), df2.sort(axis=2), check_names=True)
        return True
    except:
        return False

def mask(df, key, value):
    # need to change the pandas.DataFrame.mask function
    # set pd.DataFrame.mask = mask after defining function
    return df[df[key] == value]
