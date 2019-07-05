# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs
import pymongo
from scrapy.conf import settings

#settings = get_project_settings()

#from scrapy.conf import settings

class CeshiPipeline(object):
    def __init__(self):
        port = settings['MONGODB_PORT']
        host = settings['MONGODB_HOST']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings['MONGODB_COLL']]

    def process_item(self, item, spider):
        book_info = dict(item)
        self.post.insert(book_info)
        return item
    #def process_item(self, item, spider):
         
        #return item
'''
        base_dir = os.getcwd()
        filename = base_dir + '/items.txt'
     
        with open(filename, 'a') as f:
            f.write(item['title']+'\n')
            f.write(item['link']+'\n')
            f.write(item['data']+'\n')
            f.write(item['desc']+'\n')


           



'''        
       
