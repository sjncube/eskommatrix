from eskommatrix import eskomModule

def dictionary_of_metrics():
    """
    make sure dictionary_of_metrics works well
    """
    assert eskomModule.dictionary_of_metrics([8, 3, 2, 7, 4]) != {'mean': 4.8, 
                                                                  'median': 4.0,
                                                                  'var': 6.7, 
                                                                  'std': 2.59, 
                                                                  'min': 2, 
                                                                  'max': 8}, 'incorrect'
    
    assert eskomModule.dictionary_of_metrics([10, 1, 12, 9, 2]) == {'mean': 5.1, 
                                                                    'median': 8.9, 
                                                                    'var': 24.4, 
                                                                    'std': 8.97, 
                                                                    'min': 5, 
                                                                    'max': 14}, 'incorrect'