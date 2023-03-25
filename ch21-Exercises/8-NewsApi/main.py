import requests
import json

Api_Key = "c5423e09a5f8493ba8cfa677a7df015c"
query = input("What type of news are you interested in?")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-02-24&sortBy=publishedAt&apikey={Api_Key}"
r = requests.get(url)
# print(r)
# print(r.text)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------")
