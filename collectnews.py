import requests
import json
import os.path
import config
from datetime import datetime, date

class stocknews():
    def __init__(self):
        self.url = 'https://stocknewsapi.com/api/v1?tickers='
        self.secondurl = '&items=30&sortby=rank&token=' + config.api_token
        self.sentiment_rubric = {
            'positive' : 0.33,
            'negative' : -0.33,
            'neutral' : 0
        }
        self.savepath = 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/'

    def curr_date(self):
        """ Returns the current date

        Parameters:

        Returns:
        date-time in ISO 8601 format

        """

        today = datetime.now()

        return date(today.year, today.month, today.day).isoformat()

    def search(self, company):
        """ writes a json file to some path containing information from an api call

        Parameters:
        company (str) : ticker of company

        Returns:
        
        """
        comp_url =  self.url + company + self.secondurl
        responses = requests.get(comp_url).json()

        title = self.curr_date() + '-' + company + '.json'
        completepath = os.path.join(self.savepath, title)

        with open(completepath, 'w+') as curr_file:
            json.dump(responses, curr_file, indent=4)

        curr_file.close()

test = stocknews()
test.search('msft')
