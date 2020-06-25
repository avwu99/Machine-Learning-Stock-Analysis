import numpy as np
import json
import os
import os.path
import config
import requests
from datetime import datetime, timedelta

class processor():
    def __init__(self, direc, macd, rsi, hist):
        self.features = []
        self.targets = []
        self.directory = direc
        self.macddirectory = macd
        self.rsidirectory = rsi
        self.historical = hist
        self.ones = 0
        self.zero = 0


    def get_sentiment(self):
        """ Grabs sentiment from JSON file of articles in a folder, and appends to the features of the class

        Parameters:
        None

        Returns:
        None

        """
        for file in os.listdir(self.directory):
            with open(os.path.join(self.directory, file), 'r') as curr_file:
                articles = json.load(curr_file)

                for i in articles['data']:
                    if i['sentiment'] == 'Positive':
                        self.features.append([0, 0, 0, 0])
                    elif i['sentiment'] == 'Negative':
                        self.features.append([1, 0, 0, 0])
                    else:
                        self.features.append([2, 0, 0, 0])
            curr_file.close()

    def get_date(self, orig):
        """ Transforms date format to YEAR-MONTH-DAY from Day Month Year to be used later

        Parameters:
        orig(str) : date in string format of "Day Month Year" (i.e 05 May 2020)

        Returns:
        dates(list) : List of dates 2 days prior to the original, and the original date, all in correct format for later use. 3 days in case article was published on weekend.

        """
        orig_date = orig[5:16]

        datetimeobj = datetime.strptime(orig_date, '%d %b %Y')
        threedate = datetimeobj - timedelta(days=3)
        twodate = datetimeobj - timedelta(days=2)
        onedate = datetimeobj - timedelta(days=1)
        new_date = datetimeobj.strftime('%Y-%m-%d')

        dates = [threedate.strftime('%Y-%m-%d'), twodate.strftime('%Y-%m-%d'), onedate.strftime('%Y-%m-%d'), new_date]

        day_after = datetimeobj + timedelta(days=1)
        day_after1 = datetimeobj + timedelta(days=2)
        day_after2 = datetimeobj + timedelta(days=3)
        day_after3 = datetimeobj + timedelta(days=3)
        day_after = day_after.strftime('%Y-%m-%d')
        day_after1 = day_after1.strftime('%Y-%m-%d')
        day_after2 = day_after2.strftime('%Y-%m-%d')
        day_after3 = day_after3.strftime('%Y-%m-%d')

        new_days = [day_after, day_after1, day_after2, day_after3]

        return dates, new_days

    def trend_macd(self, macds):
        pass

    def trend_rsi(self, rsis):
        """ Find overall trend of given RSIs, using moving average equation

        Parameters:
        rsis(list) : List of RSIs

        Returns:
        0(int) : Positive Trend
        1(int) : Negative Trend
        2(int) : Neutral Trend

        """
        # list of rsis
        # calculate trend over 6 points, 3point Moving Average
        ma1 = sum(rsis[:3]) / 3
        ma2 = sum(rsis[3:]) / 3

        slope = (ma1 - ma2) / 2

        if slope > 1:
            return 0
        elif slope < -1:
            return 1
        else:
            return 2

    def get_macd(self):
        pass

    def get_rsi(self):
        """ Builds upon features by calculating trend of RSIs the past 6 days from the date the article was published.
        Also adds in feature of the RSI value of that day. Also populates targets.

        Parameters:
        None

        Returns:
        None

        """
        counter = 0
        for file in os.listdir(self.directory):
            with open(os.path.join(self.directory, file), 'r') as curr_file:
                articles = json.load(curr_file)
                with open(os.path.join(self.rsidirectory, file), 'r') as rsi_file:
                    rsi_vals = json.load(rsi_file)
                    rsis_keys = list(rsi_vals['Technical Analysis: RSI'].keys())
                    rsis_keys[0] = rsis_keys[0][0:11]
                    rsis = list(rsi_vals['Technical Analysis: RSI'].values())

                    with open(os.path.join(self.historical, file), 'r') as hist_file:
                        hist_vals = json.load(hist_file)
                        hist_keys = list(hist_vals['Time Series (Daily)'].keys())
                        hists = list(hist_vals['Time Series (Daily)'].values())

                        for i in range(len(articles['data'])):
                            #print(file)
                            list_rsis = []
                            orig = articles['data'][i]['date']
                            formatted_date, new_day = self.get_date(orig)

                            try:
                                idx = rsis_keys.index(formatted_date[-1])
                                histidx = hist_keys.index(formatted_date[-1])
                            except Exception as e:
                                try:
                                    idx = rsis_keys.index(formatted_date[2])
                                    histidx = hist_keys.index(formatted_date[2])
                                except Exception as e:
                                    try:
                                        idx = rsis_keys.index(formatted_date[1])
                                        histidx = hist_keys.index(formatted_date[1])
                                    except Exception as e:
                                        try:
                                            idx = rsis_keys.index(formatted_date[0])
                                            histidx = hist_keys.index(formatted_date[0])
                                        except Exception as e:
                                            del self.features[counter]
                                            continue


                            if float(rsis[idx]['RSI']) < 35:
                                self.features[counter][2] = 0
                            elif float(rsis[idx]['RSI']) >= 35 and float(rsis[idx]['RSI']) <= 65:
                                self.features[counter][2] = 1
                            else:
                                self.features[counter][2] = 2

                            list_rsis.append(float(rsis[idx]['RSI']))

                            for u in range(1, 6):
                                list_rsis.insert(0, float(rsis[idx-u]['RSI']))


                            try:
                                newDateIdx = hist_keys.index(new_day[0])
                            except Exception as e:
                                try:
                                    newDateIdx = hist_keys.index(new_day[1])
                                except Exception as e:
                                    try:
                                        newDateIdx = hist_keys.index(new_day[2])
                                    except Exception as e:
                                        try:
                                            newDateIdx = hist_keys.index(new_day[3])
                                        except Exception as e:
                                             del self.features[counter]
                                             continue


                            close1 = float(hists[histidx]['4. close'])
                            close2 = float(hists[newDateIdx]['4. close'])

                            self.features[counter][1] = self.trend_rsi(list_rsis)

                            self.targets.append(self.calc_return(close1, close2))

                            counter += 1

                        hist_file.close()
                rsi_file.close()
            curr_file.close()

    def calc_return(self, close1, close2):
        """ Takes in two closing prices to determine whether or not there was a significant increase/ rate of return

        Parameters:
        close1 (float): closing price of earliest date
        close2 (float): Closing price of most recent date

        Returns:
        1 (int): good profit
        0 (int): not significant profit

        """
        revenue = close2 - close1
        percentProfit = revenue/close2

        if percentProfit >= 0.05:
            self.ones += 1
            return 1
        else:
            self.zero += 1
            return 0

    def populate_data(self):
        self.get_sentiment()
        self.get_rsi()
        self.get_macd()
