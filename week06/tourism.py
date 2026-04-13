# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "200281100206dd4ac6cdacf7d0e3a9061cf1502ccd847851812036590082c162"

"""### [CODE 0]"""

def main():
    jsonResult = []
    result = []

    print("<< 국내 입국한 외")