import time, io, re, os
from urllib.parse import urljoin, urlparse
import requests
import pandas as pd
from bs4 import BeautifulSoup

BASE = "https://www.bowwwl.com"
URL  = f"{BASE}/bowling-ball-database"

HEADERS = {"User-Agent": "Mozilla/5.0 (Mac) Safari/605.1.15 (learning project)"}

class Data_Collection:
    def __init__(self, base, url, headers):
        self.base = BASE
        self.url = URL
        self.headers = HEADERS
    def 