import requests
from bs4 import BeautifulSoup
import json


#first we will set up json data
#then we will compare them
#then print them


symbols=[]
stock_data=[]

def getData(symbols):

    for symbol in symbols:
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
        url=f'https://finance.yahoo.com/quote/{symbol}'

        r=requests.get(url)

        soup=BeautifulSoup(r.text,"html.parser")



        stock={
            "symbol": symbol,
            "name": soup.find("h1",attrs={"class":"D(ib) Fz(18px)"}).text,
            "price" : soup.find("div",attrs={"class":"D(ib) Mend(20px)"}).find_all("span")[0].text,
            "change" : soup.find("div",attrs={"class":"D(ib) Mend(20px)"}).find_all("span")[1].text
        }

        stock_data.append(stock)

def getList(choice):

    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
    decision=""
    if choice==1:
        decision="cryptocurrencies"
    elif choice==2:
        decision="currencies"
    elif choice==3:
        decision="gainers"
    elif choice==4:
        decision="losers"
    elif choice==5:
        decision="most-active"

    url=f'https://finance.yahoo.com/{decision}'

    r=requests.get(url)

    soup=BeautifulSoup(r.text,"html.parser")

    #find_all("tr")[ this is the part where you are gonna change]
    for i in range(len(soup.find("tbody").find_all("tr"))):
        name=soup.find("tbody").find_all("tr")[i].find_all("td")[0]
        symbols.append(name.text)

    

choice=int(input("What market would you like to scrape right now? \n1.Cryptocurrencies \n2.Currencies \n3.Stocks: Gainers \n4.Stocks: Losers \n5.Stocks: Most Active  \nPick Your Decision(1-5):"))

getList(choice)
getData(symbols)



for i in stock_data:
    print("Name:",i["name"])
    print("Price:",i["price"])
    print("Change:",i["change"])
    print("")


with open("stockdata.json","w") as f:
    json.dump(stock_data,f)
