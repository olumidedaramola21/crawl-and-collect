import requests
import pandas as pd
import time
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime



api_key = "225d170dd24bb7b6899d8b82f5ae7875"

city_name = "Lagos"

api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(api_url).json()

print(json.dumps(response, indent=2))

