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

start_date = dt.datetime.strptime('2021-08-01', '%Y-%m-%d').date()
end_date = dt.datetime.strptime('2021-12-29', '%Y-%m-%d').date()
# response = c.get_option_chain(['TSLA'], contract_type=c.Options.ContractType.ALL, strike_count=8, to_date=start_date, from_date=end_date)
# response = c.get_option_chain(['TSLA'], contract_type=c.Options.ContractType.CALL, strike=1000, from_date=start_date, to_date=end_date)
response = c.get_option_chain(['TSLA'], contract_type=c.Options.ContractType.CALL, strike=1000, from_date=start_date, to_date=end_date)

print(json.dumps(response.json(), indent=4))
