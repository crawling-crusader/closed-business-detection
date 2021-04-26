import serpscrap

url = "https://www.acehardware.com/store-details/14286"

config = serpscrap.Config()
uscrape = serpscrap.UrlScrape(config.get())
result = uscrape.scrap_url(url)
uscrape.url_threads

print(result)