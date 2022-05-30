import pandas as pd
import twint

def searchTweets():
    c=twint.Config()
    # c.Username="elonmusk"
    # c.limit=500
    # c.Store_csv = True
    # c.Output = "elonMuskTweets.csv"     # path to csv file
    c.Search = ['Taylor Swift']       # topic
    c.Limit = 500      # number of Tweets to scrape
    c.Store_csv = True       # store tweets in a csv file
    c.Output = "taylor_swift_tweets.csv"     # path to csv file
    

    twint.run.Search(c)

def readCsv():
    1

searchTweets()
# c.Search = ['Elon Musk']       # topic
# c.Limit = 500      # number of Tweets to scrape
# c.Store_csv = True       # store tweets in a csv file
# c.Output = "taylor_swift_tweets.csv"     # path to csv file


#df = pd.read_csv('r.csv')
