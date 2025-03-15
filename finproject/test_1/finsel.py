import requests

search_query = "AAPL"
response = requests.get(f"https://api.investing.com/search?q={search_query}")
print(response.json())