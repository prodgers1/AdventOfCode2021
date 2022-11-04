import sys
import os
import requests
from bs4 import BeautifulSoup
sys.path.append('./')

for i in range(1,26):
  day = i
  response = requests.get(f"https://adventofcode.com/2021/day/{day}")
  
  if i < 10:
    day = f"0{i}"
  dir_path = os.path.dirname(os.path.realpath(__file__)) + f"\\Day{day}"

  soup = BeautifulSoup(response.content, features="html.parser")
  description = soup.find('article', {'class': 'day-desc'}).text

  with open(f'{dir_path}\\README.md', 'w') as fp:
    fp.write(description)
    pass
