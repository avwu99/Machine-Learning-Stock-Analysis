import requests
import json
from datetime import datetime, timedelta, date

class newsapi():
    def __init__(self, key):
        self.url = 'http://newsapi.org/v2/top-headlines?'
        self.sort = 'sortBy=relevancy&'
        self.apikey = 'apikey=' + key
        self.lang = 'language=en&'
        self.q = None
        self.f = None

    def date_from_past_month(self, N=25):
        """ Returns the date 25 days ago, or some N days ago if specified

        Parameters:
        N (int): number of days ago

        Returns:
        date-time in ISO 8601 format

        """

        date_N = datetime.now() - timedelta(days=N)

        return date(date_N.year, date_N.month, date_N.day).isoformat()

    def searchnews(self, company):
        temp_q = 'q=' + company + '&'
        temp_url = self.url
        past_date = self.date_from_past_month() + '&'
        temp_url += temp_q
        temp_url += past_date
        temp_url += self.lang
        temp_url += self.sort
        temp_url += self.apikey

        response = requests.get(temp_url).json()
        #print(response)
        articles = response['articles'][0:10]

        return response

    def get_descriptions(company):
        articles = self.searchnews(company)
        desc = []
        for article in articles:
            desc.append(article['description'])

        return desc

test = newsapi('62e85089066247dfaf298fdc1fc7f36d')
print(test.get_descriptions('apple'))
