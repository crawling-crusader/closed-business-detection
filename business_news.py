import serpscrap

'''
crazy stuff yo; gives you urls and some content extracted from url
a- use it to trigger specific scrapers
b- need to be smart with key words
'''
keywords = ["retails closing in chicago"]
config = serpscrap.Config()
config.set('scrape_urls', True)

scrap = serpscrap.SerpScrap()
scrap.init(config=config.get(), keywords=keywords)
results = scrap.run()
for result in results:
    print(result)
