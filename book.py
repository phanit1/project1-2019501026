import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "F2APGh5Ui3MVQNsMx9XWRQ", "isbns": "9781632168146"})
print(res.json())