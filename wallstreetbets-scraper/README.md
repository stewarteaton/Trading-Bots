The idea is to scrape reddit and twitter posts with stock/crpto ticker mentions and perform analysis based on sentiment and trends over time

Reddit API wrappers
    - PSAW best for historical data: https://psaw.readthedocs.io/en/latest/#
    - PRAW best for real-time data: https://praw.readthedocs.io/en/stable/

Vader Sentiment - Python Library
https://github.com/cjhutto/vaderSentiment
Problem:
    - Vader sentiment isn't very good for this use case as it lacks context.
        - Ex. Just bought puts on $GME, lets GO!! would produce a very positive sentiment, when it should be a bearish sentiment.
    - Solution: train custom sentiment model
        - manually tagging sentences 
        - train it on market returns


Timescale DB (local) to store data
    - docker start timescaledb