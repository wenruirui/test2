from scrapy import cmdline

cmdline.execute("scrapy crawl dmoz -o ad.json".split())
