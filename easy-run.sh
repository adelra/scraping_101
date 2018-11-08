#!/bin/bash
# file: easy-run.sh
echo Thi file will run a crawler which is located in the folder scrapy/dataset/dataset/spiders
echo Checking dependencies
scrapy version
echo running Crawler
cd scrapy/dataset/dataset/spiders
scrapy crawl general
