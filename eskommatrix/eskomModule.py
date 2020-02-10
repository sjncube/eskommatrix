import pandas as pd
import numpy as np


### START FUNCTION
def dictionary_of_metrics(items):
    """
    Calculates the mean, median, variance, standard deviation, 
    minimum and maximum of a given list of items

    Args:
        items(list): allow a list as input containing  numerical 
        entries.
    Return:
        dictionary(dom_dict): with keys 'mean', 'median',
        'std', 'var', 'min', and 'max', corresponding to the mean, 
        median, standard deviation, variance, 
        minimum and maximum of the input list, respectively.

    Example:
        >>>dictionary_of_metrics([39660.0, 36024.0, 32127.0, 39488.0, 
        18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 
        25275.0])

        {'mean': 26244.42,
         'median': 24403.5,
         'var': 108160153.17,
         'std': 10400.01,
         'min': 8842.0,
         'max': 39660.0}

    """
    
    dom_dict =  {'mean':round(np.mean(items),2),
                 'median':round(np.median(items),2),
                 'var':round(np.var(items, ddof=1),2),
                 'std':round(np.std(items, ddof=1),2),
                 'min':round(np.min(items),2),
                 'max':round(np.max(items),2)}
    return dom_dict
### END FUNCTION