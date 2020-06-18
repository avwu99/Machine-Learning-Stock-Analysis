import os
import os.path
import config
import requests
import time
import json
from datetime import datetime, timedelta

directory = 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energy/'
macddirectory = 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energyMACD/'
rsidirectory = 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energyRSI/'
historical = 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energyHistorical/'

def get_macd():

    url = 'https://www.alphavantage.co/query?function=MACD&symbol='
    url2 = '&interval=daily&series_type=open&apikey=' + config.alpha_token

    counter = 0
    for file in os.listdir(directory):
        if counter == 5:
            counter = 0
            time.sleep(60)

        with open(os.path.join(directory, file), 'r') as curr_file:
            ticker = file[0:-5]
            comp_url = url + ticker + url2

            response = requests.get(comp_url).json()

            title = ticker + '.json'
            completepath = os.path.join(macddirectory, title)

            with open(completepath, 'w+') as macd_file:
                json.dump(response, macd_file, indent=4)

            macd_file.close()
        curr_file.close()
        counter += 1

def get_rsi():
    url = 'https://www.alphavantage.co/query?function=RSI&symbol='
    url2 = '&interval=daily&time_period=14&series_type=open&apikey=' + config.alpha_token

    counter = 0
    for file in os.listdir(directory):
        if counter == 5:
            counter = 0
            time.sleep(60)

        with open(os.path.join(directory, file), 'r') as curr_file:
            ticker = file[0:-5]
            comp_url = url + ticker + url2

            response = requests.get(comp_url).json()

            title = ticker + '.json'
            completepath = os.path.join(rsidirectory, title)

            with open(completepath, 'w+') as rsi_file:
                json.dump(response, rsi_file, indent=4)

            rsi_file.close()
        curr_file.close()
        counter += 1

def get_hist():

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    url2 = '&apikey=' + config.alpha_token

    counter = 0
    for file in os.listdir(directory):
        if counter == 5:
            counter = 0
            time.sleep(60)

        with open(os.path.join(directory, file), 'r') as curr_file:
            ticker = file[0:-5]
            comp_url = url + ticker + url2

            response = requests.get(comp_url).json()

            title = ticker + '.json'
            completepath = os.path.join(historical, title)

            with open(completepath, 'w+') as hist_file:
                json.dump(response, hist_file, indent=4)

            hist_file.close()
        curr_file.close()
        counter += 1
