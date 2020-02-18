#importing important packages
import pandas as pd
import numpy as np
#------------------------------------------------------------------------------#
### START FUNCTION
def dictionary_of_metrics(items):
    """
    Returns a dictionary of the mean, median, variance, standard deviation,
    minimum and maximum of a given list.

    Keyword Arguments:
    items -- input list containing numerical entries.

    Return:
    dictionary(metric_dict) with keys 'mean', 'median', 'std', 'var', 'min',
    and 'max', corresponding to the mean, median, standard deviation, variance,
    minimum and maximum of the input list, respectively.

    Example: dictionary_of_metrics([1,2,3,4,5,6]) returns {'mean': 3.5,
    'median': 3.5, 'var': 3.5, 'std': 1.87, 'min': 1, 'max': 6}
    """

    metric_dict = {
        'mean': round(np.mean(items), 2),
        'median': round(np.median(items), 2),
        'var': round(np.var(items, ddof=1), 2),  # ddof=1 for unbiased estimate
        'std': round(np.std(items, ddof=1), 2),  # ddof=1 for unbiased estimate
        'min': round(np.min(items), 2),
        'max': round(np.max(items), 2)
    }
    return metric_dict

### END FUNCTION
#------------------------------------------------------------------------------#
### START FUNCTION
### Function 2
def five_num_summary(items):
    """
    Returns the five number summary in dictionary form.

    Keyword Arguments:
    items -- input list of integers.

    Return:
    returns the five number summary in dictionary form with keys 'max',
    'median', 'min', 'q1', and 'q3' corresponding to the maximum, median,
    minimum, first quartile and third quartile of a list of integers.

    Example:
    five_num_summary([1,2,3,4,5,6]) returns {'max': 6, 'median':
    3.5, 'min': 1, 'q1': 2.25, 'q3': 4.75}
    """

    summ_dict = {
        'max': round(max(items), 2),
        'median': round(np.median(items), 2),
        'min': round(min(items), 2),
        'q1': round(np.percentile(items, 25), 2),
        'q3': round(np.percentile(items, 75), 2)
    }
    # default linear interpolation used for 'q1' and 'q3'
    return summ_dict

### END FUNCTION
#------------------------------------------------------------------------------#
### START FUNCTION
### Function 3
def date_parser(dates):
    """
    Returns dates in the 'yyyy-mm-dd' format.

    Keyword Arguments:
    dates -- input a list of datetime strings formatted as
    'yyyy-mm-dd hh:mm:ss'.

    Return:
    list of strings where each element in the returned list
    contains only the date in the 'yyyy-mm-dd' format.

    Example:
    date_parser(['2016-12-01 23:12:40',
    '2012-02-05 16:10:55', '1999-01-01 19:17:20'])
    returns ['2016-12-01', '2012-02-05', '1999-01-01']
    """

    dates_only = [item[0:10] for item in dates]  # slice date portion of string
    return(dates_only)

### END FUNCTION
#------------------------------------------------------------------------------#
### START FUNCTION
### Function 4
def extract_municipality_hashtags(df):
    """
    Extracts the municipality and hashtags mentioned in
    tweets in two new columns.

    Keyword Arguments:
    df -- Pandas dataframe as input with column of 'Tweets'

    Return:
    a modified dataframe with addtional columns 'municipality'
    and 'hashtags', containing the muncipality and hashtags
    mentioned in the tweet or the entry np.nan if neither are found.

    Example:
    For the tweet '@EMMInfo Please update on the situation #eskom'

    '@EMMInfo' will be displayed in the 'municipality' column
    '#eskom' will be displayed in the 'hashtag' column
    """

    # dictionary of twitter handles and corresponding municipalities
    mun_dict = {'@CityofCTAlerts': 'Cape Town',
                '@CityPowerJhb': 'Johannesburg',
                '@eThekwiniM': 'eThekwini',
                '@EMMInfo': 'Ekurhuleni',
                '@centlecutility': 'Mangaung',
                '@NMBmunicipality': 'Nelson Mandela Bay',
                '@CityTshwane': 'Tshwane'}

    # extract municipalities from tweets
    municipal = []
    for tweet_row in df['Tweets']:
        municipality = []
        # extract municipality and append to list
        [municipality.append(mun_dict[word])
            for word in mun_dict if word in tweet_row.split()]
        municipal.append(municipality)
    # adding municipality column to dataframe
    df['municipality'] = municipal
    df['municipality'] = df['municipality'].apply(
        lambda municipal: municipal if len(municipal) != 0 else np.nan)

    # extract hashtags from tweets if word starts with '#'
    hashtags = []
    for tweet_row in df['Tweets']:
        extracted_hashtags = []
        # extract hashtag words and append to list
        [extracted_hashtags.append(word.lower())
            for word in tweet_row.split() if word[0] == "#"]
        hashtags.append(extracted_hashtags)
    # adding new hashtags column to dataframe
    df['hashtags'] = hashtags
    df['hashtags'] = df['hashtags'].apply(lambda hashtags: hashtags if
                                          len(hashtags) != 0 else np.nan)
    return df

### END FUNCTION
#------------------------------------------------------------------------------#
### START FUNCTION
### Function 5
def number_of_tweets_per_day(df):
    """
    Calculates the number of tweets per day as a dataframe output.

    Keyword Arguments:
    df -- Pandas dataframe as input with columns named 'Tweets' and 'Date'.

    Return:
    a new dataframe, grouped by day, with the number of tweets for that day.

    Example:
    Date        | Tweet
    2019-11-22  | @EMMInfo Please update on the situation #eskom
    2019-11-20  | @Joanne I'm not creative enough to think of a new tweet
    2019-11-20  | You were right, docstrings are fun @Ridhaa

    will return:
    Date        | Tweets
    2019-11-22  |   1
    2019-11-20  |   2
    """

    df['Date'] = pd.to_datetime(df['Date']).dt.date  # convert to yyyy-mm-dd
    tweetsperday_df = df.groupby(['Date'])[['Tweets']].count()
    return tweetsperday_df

### END FUNCTION
#------------------------------------------------------------------------------#
### START FUNCTION
### Function 6
def word_splitter(df):
    """Splits the sentences in a dataframe's column into a list of
    separate lowercase words.

    Keyword Arguments:
    Pandas dataframe as input with column named 'Tweets'

    Return:
    Returns a modified dataframe with a new column named 'Split Tweets'
    containing a list of 'tokens' or separated words

    Example:
    For the tweet:

    '@EMMInfo Please update on the situation #eskom'

    [@emminfo, please, update, on, the, situation, #eskom]
    is returned in the 'Split Tweets' column.
    """
    # tokenization (splitting string into list of tokens)
    df['Split Tweets'] = df.Tweets.apply(lambda x: x.lower().split())
    return df

### END FUNCTION
#------------------------------------------------------------------------------#
### START FUNCTION
### Function 7
def stop_words_remover(df):
    """Returns a modified dataframe with a column named 'Without
    Stop Words' that includes a tokenised list of words from the
    respective tweet with English stop words from the
    'stop_words_dict' removed.

    Keyword Arguments:
    Pandas dataframe as input with column named 'Tweets'

    Example:
    For the tweet:

    '@EMMInfo Please update on the situation #eskom'

    [@emminfo, update, situation, #eskom ] is returned in the
    'Without Stop Words' column.
    """
    # dictionary of english stopwords
    stop_words_dict = {
        'stopwords':[
            'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
            'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
            'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
            'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
            'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
            'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
            'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
            'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
            'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
            'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
            'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
            'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
            'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
            'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
            'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
            'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
            'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
            'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
            "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
            'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
            'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
            'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
            'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
            'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
            'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
            'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
            'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
            'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
            'same', 'were', 'it', 'every', 'third', 'together'
        ]
    }

    #spliting sentences into a list and making the words lower cases from the tweeets
    split_tweets = df.Tweets.apply(lambda x: x.lower().split())
    #Removing the english stop words using the provided dictionary
    df["Without Stop Words"] = split_tweets.apply(lambda x: [word for word in x if word not in stop_words_dict['stopwords']])
    return df

### END FUNCTION
#------------------------------------------------------------------------------#
