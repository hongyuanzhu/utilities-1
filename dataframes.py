import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

def equal_dfs(df1, df2):
    try:
        assert_frame_equal(df1.sort(axis=1), df2.sort(axis=2), check_names=True)
        return True
    except:
        return False
