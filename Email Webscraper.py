import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
import os.path


def webscrape_onesite(original_url): 

    unscraped = deque([original_url])  

    scraped = set()  

    emails = set()  

    while len(unscraped):
        url = unscraped.popleft()  
        scraped.add(url)

        parts = urlsplit(url)

        base_url = "{0.scheme}://{0.netloc}".format(parts)
        if '/' in parts.path:
          path = url[:url.rfind('/')+1]
        else:
          path = url

        print("Crawling URL %s" % url)
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I))
        emails.update(new_emails) 


        soup = BeautifulSoup(response.text, 'lxml')

        for anchor in soup.find_all("a"):

          if "href" in anchor.attrs:
            link = anchor.attrs["href"]
            if link.startswith('mailto:'):
                print(link[7:])
                emails.update({link[7:]})
          else:
            link = ''

            if link.startswith('/'):
                link = base_url + link



            elif not link.startswith('http'):
                link = path + link

            if not link.endswith(".gz"):
              if not link in unscraped and not link in scraped:
                  unscraped.append(link)
    print(emails)
    df = pd.DataFrame(emails, columns=["Email"])
    if(len(df.Email.value_counts()) == 0):
        return
    if(os.path.isfile("C:/Users/kohji/OneDrive/Documents/GitHub/Occutrack/email.csv")):
        df.to_csv('C:/Users/kohji/OneDrive/Documents/GitHub/Occutrack/email.csv', index=False,mode='a')
    else:
        df.to_csv("C:/Users/kohji/OneDrive/Documents/GitHub/Occutrack/email.csv",sep='|',index=False)

        
#################################################################################################################
url = input("Enter the website url: ")
webscrape_onesite(url)
#################################################################################################################
#################################################################################################################
for i in range(1500):
    original_url = f"https://researchers.masseyeandear.org/details/{i}"
    webscrape_onesite(original_url)
#################################################################################################################

