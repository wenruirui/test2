import scrapy


from ceshi.items import DmozItem 


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dytt8.net"]
    start_urls = [
       "http://www.dytt8.net/html/gndy/dyzz/index.html"

            ]

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #print(response.xpath('//div[@class="bd3r"]'))
        
        
        tables = response.xpath('//div[@class="bd3r"]//table')
        for sel in tables:
            item = DmozItem()
            item['title'] = sel.xpath('.//tr//a[@class="ulink"]/text()').extract() 
            item['filmurl'] = 'http://www.dytt8.net' +  sel.xpath('.//tr//a[@class="ulink"]/@href').extract_first()
            item['data'] = sel.xpath(".//tr//font[@color='#8F8C89']/text()").extract_first().replace("\r\n","")            
            item['desc'] = sel.xpath('.//tr//td[@colspan="2"]/text()').extract()

           


         
            yield scrapy.Request(url = item['filmurl'],callback=self.parse_url) 

           
    def parse_url(self,response):
        #for sel2 in response.xpath('//div[@class="bd3r"]//div[@class="co_content8"]'):
        oneitem = DmozItem()
        jianjie = "".join(response.xpath('/html/body/div[1]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul//text()[position()!=1]').extract()).replace("\r\n","") 
       
        
        #jianjie = jianjie[0].strip()
        download = response.xpath('/html/body/div[1]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul//td[@bgcolor="#fdfddf"]/a/@href').extract()
        oneitem['jianjie'] = jianjie.replace(" ","")
        oneitem['download'] = download
        yield oneitem
        
       
       

        


            

            #item['title'] = sel.xpath('normalize-space(.//font[@color="#008800"]//a/text())').extract() 
            #open(filename,'w').write(json.dumps(title, encoding="gb2312", ensure_ascii=False))
            
'''           
            print title
            print link
            print desc
            print data

           
            for sel in tables:
            item = DmozItem()
           item['title'] = sel.xpath('.//tr//a[@class="ulink"]/text()').extract()    
            item['link'] = sel.xpath('.//tr//a[@class="ulink"]/@href').extract()
            item['data'] = sel.xpath(".//tr//font[@color='#8F8C89']/text()").extract()           
            item['desc'] = sel.xpath('.//tr//td[@colspan="2"]/text()').extract()

            yield item

            print item['title'],
            print item['link'],
            print item['data'],
            print item['desc']

             item['title'] = sel.xpath('normalize-space(.//ul//a[@class="ulink"]/text())').extract()
            
            item['link'] = sel.xpath('normalize-space(.//ul//a[@class="ulink"]/@href)').extract()

            item['data'] = sel.xpath("normalize-space(.//ul//font[@color='#8F8C89']/text())").extract()

            
            item['desc'] = sel.xpath('normalize-space(.//tr//td[@colspan="2"]/text())').extract()

           
            
'''
