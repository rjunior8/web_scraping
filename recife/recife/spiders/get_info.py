# -*- coding: utf-8 -*-

import scrapy
from recife.items import RecifeItem
import re
import sys
import cfscrape

class SchoolInfo(scrapy.Spider):
	name = "school_info"
	allowed_domains = ["melhorescola.com.br"]
	start_urls = []
	with open("~/py_venv/python36/recife/recife/recife.csv", 'r') as f:
		for i in f.readlines():
			start_urls.append(i.replace("\n", ''))

	def __init__(self):
		self.scraper = cfscrape.create_scraper()

	def parse(self, response):
		try:
			body = self.scraper.get(response.url).content
			title = "".join(response.css("title::text").extract())
			name = title.split('-')[0]
			item = RecifeItem()
			s = str(body)
			item["school_name"] = name
			street_address = re.compile(r'"streetAddress":"(.*)"\\n    },\\n    "description":"')
			item["street_address"] = street_address.findall(s)
			address_locality = re.compile(r'"addressLocality":"(\w+)')
			item["address_locality"] = address_locality.findall(s)
			address_region = re.compile(r'"addressRegion":"(\w+)')
			item["address_region"] = address_region.findall(s)
			postal_code = re.compile(r'"postalCode":"(\d+\-\d+)')
			item["postal_code"] = postal_code.findall(s)
			address_email = re.compile(r'"email":"(.*)",\\n    "address":{\\n')
			item["address_email"] = address_email.findall(s)
			telephone = re.compile(r'"telephone":"(\(\d+\)\s\d+\-\d+)')
			item["telephone"] = telephone.findall(s)
			childrens_education = re.compile(r'Ensino Infantil: <strong class="orange">(\d+)')
			item["childrens_education"] = childrens_education.findall(s)
			elementary_school1 = re.compile(r'Ensino Fundamental I: <strong class="orange">(\d+)')
			item["elementary_school1"] = elementary_school1.findall(s)
			elementary_school2 = re.compile(r'Ensino Fundamental II: <strong class="orange">(\d+)')
			item["elementary_school2"] = elementary_school2.findall(s)
			high_school = re.compile(r'dio: <strong class="orange">(\d+)')
			item["high_school"] = high_school.findall(s)
			ce_value = re.compile(r'Mensalidades\*\</h2\>\\n<p class="grey">Ensino Infantil: <strong class="orange">R\$ (\d+\,\d+)')
			item["childrens_education_cost"] = ce_value.findall(s)
			es_value = re.compile(r'Mensalidades\*\</h2\>\\n<p class="grey">Ensino Fundamental: <strong class="orange">R\$ (\d+\,\d+)')
			item["elementary_school_cost"] = es_value.findall(s)
			hs_value = re.compile(r'dio: <strong class="orange">R\$ (\d+\,\d+)')
			item["high_school_cost"] = hs_value.findall(s)
			yield item
		except Exception as e:
			print("\n\n{}\nError on line: {}\n\n".format(e, sys.exc_info()[-1].tb_lineno))

