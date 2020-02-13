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
    out_dict={'max':round(max(items),2),
       'median':round(np.median(items),2),
       'min':round(min(items),2),
       'q1':round(np.percentile(items,25),2),
       'q3':round(np.percentile(items,75),2)}
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
    
    """
    twitter_df = df
    mun_dict = {'@CityofCTAlerts' : 'Cape Town',
                '@CityPowerJhb' : 'Johannesburg',
                '@eThekwiniM' : 'eThekwini' ,
                '@EMMInfo' : 'Ekurhuleni',
                '@centlecutility' : 'Mangaung',
                '@NMBmunicipality' : 'Nelson Mandela Bay',
                '@CityTshwane' : 'Tshwane'}
    
    municipal = []
    for tweet_row in twitter_df['Tweets']:
        municipality = [] #will store extracted words from  mun_dict
        [municipality.append(mun_dict[word])  for word in mun_dict if word in tweet_row.split()]  #Extract municipality and put it on my list
        municipal.append(municipality)
    twitter_df['municipality'] = municipal 
    twitter_df['municipality'] = twitter_df['municipality'].apply(lambda municipal: municipal if len(municipal) != 0 else np.nan) #Adding municipality column on my dataframe
    
    hashtags = []
    for tweet_row in twitter_df['Tweets']:
        extracted_hashtags = [] #will store extracted words from  each tweet rows
        [extracted_hashtags.append(word.lower()) for word in tweet_row.split() if word[0] == "#"]
        hashtags.append(extracted_hashtags)
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
def stop_words_remover(df):
    """removes english stop words from a tweet (tokenised list of tweets) using pandas dataframe as input.
    The function  modifies the input dataframe and returns a new dataframe"""
    split_tweets = df.Tweets.apply(lambda x: x.lower().split())
    df["Without Stop Words"] = split_tweets.apply(lambda x: [word for word in x if word not in stop_words_dict['stopwords']]) 
    return df
### END FUNCTION
#----------------------------------------------------------------------------------#
### START FUNCTION
def word_splitter(df):
    """
   The funcrion splits the sentences in a dataframe's column into a list of the separate words.
    The created lists  is placed in a column named 'Split Tweets' in the original dataframe.

Function Specifications:

It takes a pandas dataframe as an input.
The dataframe contains a column, named 'Tweets'.
The function splits the sentences in the 'Tweets' into a list of seperate words, and place the result into a new column named 'Split Tweets'. The resulting words must all be lowercase!
The function modifies the input dataframe directly.
The function then returns the modified dataframe as an output on the new column.
    """
    df['Split Tweets'] = df.Tweets.apply(lambda x: x.lower().split())
    return df

### END FUNCTION