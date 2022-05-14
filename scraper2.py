from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)