# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


"""class RecifeItem(Item):
    school_link = Field()"""

class RecifeItem(Item):
	school_name = Field()
	street_address = Field()
	address_locality = Field()
	address_region = Field()
	postal_code = Field()
	address_email = Field()
	telephone = Field()
	childrens_education = Field()
	elementary_school1 = Field()
	elementary_school2 = Field()
	high_school = Field()
	childrens_education_cost = Field()
	elementary_school_cost = Field()
	high_school_cost = Field()
