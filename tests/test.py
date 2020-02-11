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



def five_num_summary():
    """
     make sure five_num_summary works well
    """
    assert eskomModule.five_num_summary([8, 3, 2, 7, 4]) != {'max': 8, 'median': 4.0, 'min': 2, 'q1': 3.0, 'q3': 7.0},'incorrect'
    

def date_parser():
    """
    make sure date_parser works well
    """
    assert eskomModule.date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53', '2019-11-29 12:46:10']) != ['2019-11-29', '2019-11-29', '2019-11-29'],'incorrect'
    
    assert eskomModule.date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53', '2019-11-29 12:46:10']) == ['2019-11-29 12:50:54', '2019-11-29 12:46:53', '2019-11-29 12:46:10'],'incorrect'

