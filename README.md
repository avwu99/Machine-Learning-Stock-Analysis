# Machine-Learning-Stock-Analysis
Use sentiment analysis of past articles and analysis of technical indicators to predict short term trends of stocks. Target specific industries and companies following a max market cap.

With about 600 data points for each industry, we are at an average of around 66% accuracy.

# Work in Progress
- Implementing MACD analysis
- Collecting more data
- Implementing Java Rest API for GUI 

# APIs Used
- Alpha Vantage
- Stocknews

# Libraries Used

- Numpy [pip-install](https://pypi.org/project/numpy/)
```bash
pip install numpy
```
- Sklearn [install](https://scikit-learn.org/stable/install.html)
```bash
pip install -U scikit-learn
```
- os
- os.path
- datetime
- requests
- json
- time

# config.py
Your config file should include the following:

```python
api_token = '**** YOUR STOCK NEWS API ****'
alpha_token = '**** YOUR ALPHA VANTAGE API ****'

```
# Usage
Once you have your data in a file called 'data', all you have to do is use processor.py to create your features and targets, then use learner.py to fit and train a learner for classification. Example can be seen in the "Testing" section in the learner.py file.

## Data Form
In order to use these files, you must collect your own data (news and any historical/technical data on stocks). The news collected from the StockNews API were in the form of JSON files as follows:

```json
{
    "data": [
        {
            "news_url": "example.com",
            "image_url": "example.com/image.jpg",
            "title": "example title",
            "text": "example text",
            "source_name": "source",
            "date": "Fri, 12 Jun 2020 09:05:00 -0400",
            "topics": [
                "PressRelease"
            ],
            "sentiment": "Neutral",
            "type": "Article",
            "tickers": [
                "TEST"
            ]
        },
        {
            "news_url": "example.com",
            "image_url": "example.com/image.jpg",
            "title": "example title",
            "text": "example text",
            "source_name": "source",
            "date": "Fri, 12 Jun 2020 09:05:00 -0400",
            "topics": [
                "PressRelease"
            ],
            "sentiment": "Neutral",
            "type": "Article",
            "tickers": [
                "TEST"
            ]
        }
    ]
}
```

and the data on stocks collected from Alpha Vantage in the form of JSON files as follows:
```json
{
    "Meta Data": {
        "1: Symbol": "APEX",
        "2: Indicator": "Moving Average Convergence/Divergence (MACD)",
        "3: Last Refreshed": "2020-06-22",
        "4: Interval": "daily",
        "5.1: Fast Period": 12,
        "5.2: Slow Period": 26,
        "5.3: Signal Period": 9,
        "6: Series Type": "open",
        "7: Time Zone": "US/Eastern"
    },
    "Technical Analysis: MACD": {
        "2020-06-22": {
            "MACD_Signal": "0.0465",
            "MACD": "0.0526",
            "MACD_Hist": "0.0061"
        }
    }
}
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
