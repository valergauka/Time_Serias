import numpy as np
from get_speeds import get_speeds

def closest_pdist(vdf):
    result = vdf.groupby(['pid', pd.Grouper(freq='10T', key='tmstmp'), 'vid'])['pdist'].mean().groupby(['pid', 'tmstmp']).apply(lambda group: np.diff(np.sort(group))).min()
    return result.dropna()
