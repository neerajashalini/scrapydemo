import scrapy
import re
class demopro(scrapy.Spider):
	name = "my_scraper"
	     start_urls = ["https://www.bbc.com/food/recipes/search?cuisines[]=british"]
	n pages = 1
	for i in range(1,15):
		start_urls.append("https:/www.bbc.com/food/recipes/search?page="+str(i)+"")
		def parse(self,response):
			for href in response.xpath("//div[contains(@class,'left')]/h3//@href"):
				url = "https://www.bbc.com"+href.extract()
				yield scrapy.request(url,callback=self.parse_dir_contents)
		def parse_dir_contents(self,response):
			item = demoproItem()
			
			item['name'] = response.xpath("//h1[contains(@class,'gel-trafalgar content-title__text')]/text()").extract()
			
			item['images'] = response.xpath("//div[contains(@class,'responsive-image-container__16/9')]/img[contains(@class,'recipe-media__image')]//@src").extract()
           
            item['preparation_time'] = response.xpath("//p[contains(@class,'recipe-metadata__prep-time')]/text()").extract()
            
            item['cooking_time'] = response.xpath("//p[contains(@class,'recipe-metadata__cook-time')]/text()").extract()[0].strip()
            
            item['serves'] = response.xpath("//p[contains(@class,'recipe-metadata__serving')]/text()").extract()[0].strip()
            
            item['methods'] = response.xpath("//li[contains(@class,'recipe-method__list-item')]/descendant::text()").extract()
            
            item['description'] = response.xpath("//div[contains(@class,'recipe-description')]/descendant::text()").extract()
            
ingredients_list = response.xpath("//li[contains(@class,'recipe-ingredients__list-item')]/descendant::text()").extract()
ingredients_list = [x.strip() for x in ingredients_list if len(x.strip())>0]
item['ingredients'] = "".join(ingredients_list)
            
chefs_name = response.xpath("//div[contains(@class,'chef__name')]//a[contains(@class,'chef__link')]/descendant::text()").extract()
chefs_url = response.xpath("//div[contains(@class,'chef__name')]//a[contains(@class,'chef__link')]//@href").extract()
program_name = response.xpath("//div[contains(@class,'chef__programme-name')]//a[contains(@class,'chef__link')]/descendant::text()").extract()
program_url = response.xpath("//div[contains(@class,'chef__programme-name')]//a[contains(@class,'chef__link')]//@href").extract()
item['chef_details'] = "".join(chef__name)" ".join(chefs_url)" ".join(program_name)" ".join(program_url)
yield item

		 

		 