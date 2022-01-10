from psaw import PushshiftAPI
import config
import datetime as dt
import alpaca_trade_api as tradeapi
import psycopg2
import psycopg2.extras

# Connect DB
connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("select * from stock")
cursor.execute("""
    SELECT * FROM stock
""")
rows = cursor.fetchall()

# # Alpaca API
# api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url=config.API_URL)
# assets = api.list_assets()

# create stocks dictionary from local DB
stocks = {}
for row in rows:
    stocks['$' +row['symbol']] = row['id'] 

# Reddit api wrapper
redditAPI = PushshiftAPI()
# Enter date to search
start_time =int(dt.datetime(2022, 1, 5).timestamp())
# Query WSB subreddit
submissions = redditAPI.search_submissions(after=start_time,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'])

for submission in submissions:
    # print(submission.created_utc)
    # print(submission.title)
    # print(submission.url) 
    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
        print(submission.title)
 
        # for cashtag in cashtags:
        #     submitted_time = dt.datetime.fromtimestamp(submission.created_utc).isoformat()
        #     try:
        #         cursor.execute("""
        #             INSERT INTO mention ( stock_id, dt, message, source, url)
        #             VALUES (%s, %s, %s, %s, %s)
        #         """, ( stocks[cashtag], submitted_time, submission.title, 'wallstreetbets', submission.url))
        #         connection.commit()
        #     except Exception as e:
        #         print(e)
        #         connection.rollback()
