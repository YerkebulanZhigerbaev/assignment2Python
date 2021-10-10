from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver

class ParseArticle:
    def retrieveInfo(self,nameOfCurrency):

        URL='https://coinmarketcap.com/currencies/'+nameOfCurrency+'/news/'
        r = requests.get(URL, 'html.parser').text
        soup= BeautifulSoup(r,'lxml')
        header=soup.h2.text
        print(header,'\n')
        totalText=soup.text.strip()
        counting=0
        for i in range(len(totalText)):
            print(totalText[i],end='')
            if totalText[i]==' ':
                counting+=1
            if counting==4:
                print('\n',end='')
                counting=0
        print()

        print('\n\n')