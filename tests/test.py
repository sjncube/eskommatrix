from eskommatrix import eskomModule

def dictionary_of_metrics():
    """
    unit test cases for dictionary_of_metrics
    """
    assert eskomModule.dictionary_of_metrics(
        [8, 3, 2, 7, 4]) == {'mean': 4.8, 'median': 4.0, 'var': 6.7,
                             'std': 2.59, 'min': 2, 'max': 8}, 'incorrect'


    assert eskomModule.dictionary_of_metrics(
        [10, 1, 12, 9, 2]) == {'mean': 6.8, 'median': 9.0, 'var': 24.7, 
                               'std': 4.97, 'min': 1, 'max': 12}, 'incorrect'


def five_num_summary():
    """
    unit test cases for five_num_summary
    """
    assert eskomModule.five_num_summary(
        [8, 3, 2, 7, 4]) == {'max': 8, 'median': 4.0, 'min': 2,
                             'q1': 3.0, 'q3': 7.0}, 'incorrect'


def date_parser():
    """
    unit test cases for date_parser
    """
    assert eskomModule.date_parser(['2019-11-29 12:50:54',
                                    '2019-11-29 12:46:53',
                                    '2019-11-29 12:46:10']
                                   ) == ['2019-11-29',
                                         '2019-11-29',
                                         '2019-11-29'], 'incorrect'
