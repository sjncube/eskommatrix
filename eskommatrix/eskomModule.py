#importing important packages
import pandas as pd
import numpy as np
#----------------------------------------------------------------------------------#
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

    metric_dict =  {'mean':round(np.mean(items),2),
                 'median':round(np.median(items),2),
                 'var':round(np.var(items, ddof=1),2),
                 'std':round(np.std(items, ddof=1),2),
                 'min':round(np.min(items),2),
                 'max':round(np.max(items),2)}
    return metric_dict
### END FUNCTION
#----------------------------------------------------------------------------------#
### START FUNCTION
def five_num_summary(items):
    # your code here
    """
    Returns the five number summary in dictionary form.
    
    Keyword Arguments:
    items -- input list of integers.
    
    Return:
    returns the five number summary in dictionary form with keys 
    'max', 'median', 'min', 'q1', and 'q3' corresponding to the 
    maximum, median, minimum, first quartile and third quartile 
    of a list of integers.
    
    Example:
    five_num_summary([1,2,3,4,5,6]) returns {'max': 6, 'median': 
    3.5, 'min': 1, 'q1': 2.25, 'q3': 4.75}
    """
    out_dict={'max':round(max(items),2),#calculates the max
       'median':round(np.median(items),2),#calculates the median of the numbers
       'min':round(min(items),2),#calculates the minimum
       'q1':round(np.percentile(items,25),2),#calculates the lower quartile
       'q3':round(np.percentile(items,75),2)}#calculates the upper quartile
    return out_dict

### END FUNCTION
#----------------------------------------------------------------------------------#
### START FUNCTION
def date_parser(dates):
    """Returns dates in the 'YYYY-MM-DD' format from an input list of datetime
    strings"""
    date_only = [date[0:][0:10] for date in dates]
    return date_only
### END FUNCTION
#----------------------------------------------------------------------------------#
### START FUNCTION
def extract_municipality_hashtags(df):
    """
    Returns a modified dataframe with addtional columns 
    'municipality' and 'hashtags', containing the muncipality
    and hashtags mentioned in the tweet or the entry np.nan 
    if neither are found.
    
    Keyword Arguments:
    df -- Pandas dataframe as input with column of 'Tweets'
    
    Example:
    For the tweet '@EMMInfo Please update on the sitation #eskom'
    
    '@EMMInfo' will be displayed in the 'municipality' column
    '#eskom' will be displayed in the 'municipality' column
    """
    twitter_df = df
    #dictionary containing municipalities
    mun_dict = {'@CityofCTAlerts' : 'Cape Town',
                '@CityPowerJhb' : 'Johannesburg',
                '@eThekwiniM' : 'eThekwini' ,
                '@EMMInfo' : 'Ekurhuleni',
                '@centlecutility' : 'Mangaung',
                '@NMBmunicipality' : 'Nelson Mandela Bay',
                '@CityTshwane' : 'Tshwane'}
    #Extract municipalies from tweets and put NANs if municipality is not found
    municipal = []
    for tweet_row in twitter_df['Tweets']:
        municipality = []  #will store extracted words from  mun_dict
        #Extract municipality and put it on my list
        [municipality.append(mun_dict[word])  for word in mun_dict if word in tweet_row.split()]
        municipal.append(municipality)
    #Adding municipality column on my twitter_df
    twitter_df['municipality'] = municipal
    twitter_df['municipality'] = twitter_df['municipality'].apply(lambda municipal: municipal if len(municipal) != 0 else np.nan)
    
    #extract hashtags from tweets and put NANs if words on tweet row does not start with # 
    hashtags = []
    for tweet_row in twitter_df['Tweets']:
        extracted_hashtags = []  #will store extracted words from  each tweet rows
        #extract words which starts with # from tweets
        [extracted_hashtags.append(word.lower()) for word in tweet_row.split() if word[0] == "#"]
        hashtags.append(extracted_hashtags)
    #Adding a new hashtags column on my twitter_df and Add extracted hashtags to the column
    twitter_df['hashtags'] = hashtags
    twitter_df['hashtags'] = twitter_df['hashtags'].apply(lambda hashtags: hashtags if len(hashtags) != 0 else np.nan)
    df = twitter_df
    return df
### END FUNCTION
#----------------------------------------------------------------------------------#
### START FUNCTION
def number_of_tweets_per_day(df):
    """Calculates the number of tweets per day as a dataframe output.
    Note input data must be in the form 'YYYY-MM-DD HH:MM:SS"""

    df['Date']  = pd.to_datetime(df['Date']).dt.date
    tweetsperday_df = df.groupby(['Date'])[['Tweets']].count()
    return tweetsperday_df

### END FUNCTION
#----------------------------------------------------------------------------------#
### START FUNCTION
def word_splitter(df):
    """Splits the sentences in a dataframe's column into a list of
    separate lowercase words. Returns a modified dataframe with 
    a new column named 'Split Tweets'
    
    Keyword Arguments:
    Pandas dataframe as input with column named 'Tweets'
    
    Example:
    For the tweet: 
    
    '@EMMInfo Please update on the sitation #eskom'
    
    [@emminfo, please, update, on, the, situation, #eskom]
    is returned in the 'Split Tweets' column.
    """
    df['Split Tweets'] = df.Tweets.apply(lambda x: x.lower().split())#splits the tweets then returns the lower case output on a new column of the dataframe
    return df
### END FUNCTION
#----------------------------------------------------------------------------------#
### START FUNCTION
def stop_words_remover(df):
    """ Removes english stop words from a tweet (tokenised list of tweets) using pandas dataframe as input.The stop words are provided in the dictionary ('stop_words_dict' ) 
    The function  modifies the input dataframe and returns a new dataframe"""

    split_tweets = df.Tweets.apply(lambda x: x.lower().split()) # slitting sentences into a list and making the words lower cases form the Tweeets
    df["Without Stop Words"] = split_tweets.apply(lambda x: [word for word in x if word not in stop_words_dict['stopwords']]) #Removing the english stop words using the provided dictionary
    
    return df
### END FUNCTION
#----------------------------------------------------------------------------------#