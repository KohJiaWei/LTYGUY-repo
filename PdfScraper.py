from pypdf import PdfReader
import pandas as pd
import numpy as np
import csv
import os.path
import re

NO_OF_PAGES_IN_PDF = 213

emails = set()
reader = PdfReader("C:/Users/kohji/Downloads/2022 RANZCO-Abstract-Handbook.pdf") #pdf path
print(reader)
i = 0
# page = reader.pages[4]
# print(page)

# page.extract_text()


while (i < NO_OF_PAGES_IN_PDF):
    page = reader.pages[i]
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", page.extract_text(0),re.I))
    emails.update(new_emails) 
    print(new_emails)
    i = i+1
    df = pd.DataFrame(emails, columns=["Email"])
    if(len(df.Email.value_counts()) == 0):
        continue

if(os.path.isfile("C:/Users/kohji/OneDrive/Documents/GitHub/Occutrack/RANZCO.csv")):
    df.to_csv('C:/Users/kohji/OneDrive/Documents/GitHub/Occutrack/RANZCO.csv', index=False,mode='a')
else:
    df.to_csv("C:/Users/kohji/OneDrive/Documents/GitHub/Occutrack/RANZCO.csv",sep='|',index=False)
