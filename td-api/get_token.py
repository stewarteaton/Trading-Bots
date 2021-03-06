from tda import auth, client
import json
import config
import datetime as dt

try:
    c = auth.client_from_token_file(config.TOKEN_PATH, config.API_KEY)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH) as driver:
        c = auth.client_from_login_flow(
            driver, config.API_KEY, config.REDIRECT_URL, config.TOKEN_PATH)