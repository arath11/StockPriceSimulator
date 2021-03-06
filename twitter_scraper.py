import twint
import csv


def scraper(username: str,
            limit: int = 3500,
            output_name: str = "output.csv",
            store_csv: bool = False,
            hide_output: bool = True):

    c = twint.Config()
    c.Username = username
    c.limit = limit
    c.Store_csv = True
    c.Hide_output = True
    c.Output = output_name
    twint.run.Search(c)


def get_csv_attribute(path: str, attribute: str) -> list[str]:
    with open(path, "r",  encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        lines = [row[attribute] for row in reader]
        return lines
    return []


def match(words_to_search: list[str], tweets: list[str]) -> list[str]:
    return [word for tweet in tweets for word in words_to_search if word.lower() in tweet.lower()]


scraper("elonmusk", limit=30000, store_csv=True)
tweets = get_csv_attribute("output.csv", "tweet")
stocks_to_search = get_csv_attribute("stocks.csv", "Name")
symbols = get_csv_attribute("stocks.csv", "Symbol")
dict_stocks = {name: symbol for symbol, name in zip(symbols, stocks_to_search)}
trends = set(match(stocks_to_search, tweets))
trends_symbols = [dict_stocks[trend] for trend in trends if trend in dict_stocks]