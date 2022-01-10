import praw
import config
import alpaca_trade_api as tradeapi
from data import *
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import squarify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class WSBets:
    def __init__(self, current_time, c_analyzed, posts, picks, top_picks, symbols, titles, picks_sa, scores):
        self.current_time = current_time
        self.c_analyzed = c_analyzed
        self.posts = posts
        self.picks = picks
        self.top_picks = top_picks
        self.symbols = symbols
        self.titles = titles
        self.picks_sa = picks_sa
        self.scores = scores

def analyze():
    # set parameters
    limit = 100   # number of comments
    upvotes = 3   # comment is considered if upvotes exceed this #
    picks = 10    # prints as "Top ## picks are:"
    picks_sa = 5   # of picks for sentiment analysis
    post_flairs = ['Daily Discussion', 'Weekend Discussion', 'Discussion']    # posts flairs to search
    posts, count, c_analyzed, tickers, titles, a_comments = 0, 0, 0, {}, [], {}   #set variables to empty
    stocks = get_stocks()  # calls function below

    start_time = time.time()
    reddit = reddit_login("Comment Extractor", config.REDDIT_CLIENT_ID, config.REDDIT_CLIENT_SECRET, config.REDDIT_USERNAME, config.REDDIT_PASSWORD)
    subreddit = reddit.subreddit('wallstreetbets')
    hot_subreddit = subreddit.hot(limit=10)    # sorting posts by most liked and recent
    # Extract Comments -> updateds global variables 
    extract_comments_symbols(hot_subreddit, post_flairs, titles, posts, limit, upvotes, stocks, tickers, a_comments, count, c_analyzed)
    # print(tickers)
    # print(a_comments)

    # sorts by most mentioned
    symbols = dict(sorted(tickers.items(), key=lambda item: item[1], reverse = True))
    top_picks = list(symbols.keys())[0:picks]
    current_time = (time.time() - start_time)
    scores = apply_sentiment_analysis(symbols, picks_sa, a_comments)

    # Calls class
    WSB = WSBets(current_time, c_analyzed, posts, picks, top_picks, symbols, titles, picks_sa, scores)
    # Results
    print_results(WSB)
    print_sentiment_analysis(WSB)
    return WSB

def reddit_login(user, clientid, clientsecret, username, passwrd):
    return praw.Reddit(user_agent=user,
        client_id=clientid,
        client_secret=clientsecret,
        username=username,
        password=passwrd)

def get_stocks():
    # Get list of valid tickers - Alpaca API 
    api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url=config.API_URL)
    assets = api.list_assets()
    stocks = []
    for asset in assets:
        if asset.status == 'active' and asset.tradable:
            stocks.append(asset.symbol)
    # print(stocks) 
    return stocks

# need to update
def extract_comments_symbols(hot_subreddit, post_flairs, titles, posts, limit, upvotes, stocks, tickers, a_comments, count, c_analyzed):
    # Extracting comments, symbols from subreddit
    for submission in hot_subreddit:
        if submission.link_flair_text in post_flairs:  #filters discussions
            submission.comment_sort = 'new'            #sorts to by newest
            comments = submission.comments             #stores comments for each submission
            titles.append(submission.title)
            posts += 1                                 #count number of posts
            submission.comments.replace_more(limit=limit)   
            for comment in comments:                   # loop through comments
                c_analyzed += 1                        # count analyzed comments
                if comment.score > upvotes:      
                    split = comment.body.split(" ")
                    for word in split:
                        word = word.replace("$", "")        
                        if word in stocks:
                            if word in tickers:
                                tickers[word] += 1
                                a_comments[word].append(comment.body)
                                count += 1
                            else:
                                tickers[word] = 1
                                a_comments[word] = [comment.body]
                                count += 1


def apply_sentiment_analysis(symbols, picks_sa, a_comments):
    # Applying Sentiment Analysis
    scores = {}
    vader = SentimentIntensityAnalyzer()
    picks_sentiment = list(symbols.keys())[0:picks_sa]  # creats list of symbols 

    for symbol in picks_sentiment:
        # get list of comments per symbol
        stock_comments = a_comments[symbol]
    
        for comment in stock_comments:
            # score each comment with Vader library
            score = vader.polarity_scores(comment)
            # add score to symbol
            if symbol in scores:
                # scores[symbol] 
                for key, values in score.items():
                    scores[symbol][key] += score[key]
            else:
                scores[symbol] = score

        # get Avg. score
        for key in score:
            scores[symbol][key] = scores[symbol][key] / symbols[symbol]   # divide symbol score by # of symbol occurences
            scores[symbol][key]  = "{pol:.3f}".format(pol=scores[symbol][key] )   # format
    print(scores)
    return scores



def print_results(WSB):
    # print top picks
    print("It took {t:.2f} seconds to analyze {c} comments in {p} posts.\n".format(t=WSB.current_time, c=WSB.c_analyzed, p=WSB.posts))
    print("Posts analyzed:")
    for i in WSB.titles: print(i)
    print(f"\n{WSB.picks} most mentioned picks: ")
    times = []
    top = []
    for i in WSB.top_picks:
        print(f"{i}: {WSB.symbols[i]}")
        times.append(WSB.symbols[i])
        top.append(f"{i}: {WSB.symbols[i]}")

    # squarify.plot(sizes=times, label=top, alpha=.7 )
    # plt.axis('off')
    # plt.title(f"{picks} most mentioned picks")
    # plt.show()

def print_sentiment_analysis(WSB):
    # printing sentiment analysis 
    print(f"\nSentiment analysis of top {WSB.picks_sa} picks:")
    df = pd.DataFrame(WSB.scores)
    df.index = ['Bearish', 'Neutral', 'Bullish', 'Total/Compound']
    df = df.T
    print(df)
    # test
    # df = df.astype(float)
    # colors = ['red', 'springgreen', 'forestgreen', 'coral']
    # df.plot(kind = 'bar', color=colors, title=f"Sentiment analysis of top {picks_ayz} picks:")
    # plt.show()


analyze()

# ----------------------------------------------
# Date Visualization
# most mentioned picks  
# def visualize(times, top):  
#     squarify.plot(sizes=times, label=top, alpha=.7 )
#     plt.axis('off')
#     plt.title(f"{picks} most mentioned picks")
#     plt.show()

# Sentiment analysis
# df = df.astype(float)
# colors = ['red', 'springgreen', 'forestgreen', 'coral']
# df.plot(kind = 'bar', color=colors, title=f"Sentiment analysis of top {picks_ayz} picks:")
# plt.show()
# -----------------------------------------------