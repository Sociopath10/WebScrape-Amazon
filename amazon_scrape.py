import  requests 
from bs4 import BeautifulSoup
from csv import writer
from csv import reader 
import time

# This Script Works To Scrape MRP/Current PRICE/ Title  of Samsung Galaxy Note 9 OCean Blue 128 GB .
response=requests.get("http://amazon.in/dp/B07G8C2SG5")
soup=BeautifulSoup(response.text,"html.parser")
mrp=soup.find(class_="a-text-strike").get_text().strip()
price=soup.find(id="priceblock_ourprice").get_text().strip()
title=soup.find(id="productTitle").get_text().strip()
tme=time.ctime() 
#To calculate Current Time of Script Run
print(title)
print("M.R.P IS -"+mrp)
print("PRICE IS -"+price)
heading=0
with open("amazon_scrape.csv","a") as file:
	time.ctime()
	#do nothing


with open("amazon_scrape.csv") as file:
	file.seek(0)
	first_char=file.read(1)
	if not first_char:
		heading=1



with open("amazon_scrape.csv","a") as file:

	csv_writer=writer(file,dialect="excel")
	if heading is 1:
		csv_writer.writerow(["TIME","Title","M.R.P","PRICE"])
	csv_writer.writerow([tme,title,mrp,price])