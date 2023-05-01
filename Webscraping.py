import pandas as pd
from selenium.webdriver.chrome.service import service
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
from colorama import Fore
import matplotlib.pyplot as plt
import numpy as np
Driver_Path="C:/Users/surface/PycharmProjects/ChromeDriver/chromedriver"
def AssignmentA():
        URL="https://accentsathome.ca/"
        browser=webdriver.Chrome(Driver_Path)
        browser.get(URL)
        time.sleep(3)
        searchTerm="chair"
        button=browser.find_element(By.CSS_SELECTOR,".js-no-transition")
        button.click()
        search=browser.find_element(By.CSS_SELECTOR,".site-header__search-input")
        search.send_keys(searchTerm)
        button=browser.find_element(By.CSS_SELECTOR,".site-header__search-btn--submit")
        button.click()
        time.sleep(3)
        pageNum=1
        rawString=''
        data=[]
        for i in range(0,3):
            content=browser.find_elements(By.CSS_SELECTOR,".grid-product__title--body")
            print("Count: ", str(i))
            for e in content:
                    start=e.get_attribute("innerHTML")
                    soup=BeautifulSoup(start,features='lxml')
                    rawString=soup.get_text().strip()
                    rawString=re.sub(r"[\n\t]*","",rawString)
                    rawString=re.sub('[ ]{2,}',"*",rawString)
                    print(rawString)
                    print('***')
                    data.append(rawString)
            pageNum += 1
            URL_NEXT = "https://accentsathome.ca/search?page="+str(pageNum)+\
                        "&q="+searchTerm+'%2A&type=product'


            browser.get(URL_NEXT)

            time.sleep(3)
        print("done loop")
        df=pd.DataFrame(data,columns=['Chair_model'])
        df.to_csv('scrapedweb.csv', index=False)
        new_df=pd.read_csv('scrapedweb.csv')
        print(Fore.BLUE+"\nTwo first data rows:\n")
        print(new_df.head(2))
        print(Fore.BLUE+"\nTwo last data rows \n")
        print(new_df.tail(2))

def AssignmentB():

        URL = 'https://www.imdb.com/chart/top/'
        browser = webdriver.Chrome(Driver_Path)
        browser.get(URL)
        time.sleep(3)
        content = browser.find_elements(By.CSS_SELECTOR, "strong")
        content2 = browser.find_elements(By.CSS_SELECTOR, '.secondaryInfo')
        review_data = []
        for e in content:
            start = e.get_attribute('innerHTML')
            soup = BeautifulSoup(start, features='lxml')
            rawString = soup.get_text().strip()
            rawString = re.sub(r"[\n\t()]*", '', rawString)
            rawString = re.sub('[ ]{2,}', '*', rawString)
            print(Fore.LIGHTWHITE_EX,rawString)
            print('***')
            review_data.append(rawString)
        df = pd.DataFrame(review_data, columns=['Rank'])
        model_data = []
        for e in content2:
            start = e.get_attribute('innerHTML')
            soup = BeautifulSoup(start, features='lxml')
            rawString = soup.get_text().strip()
            rawString = re.sub(r"[\n\t()]*", '', rawString)
            rawString = re.sub('[ ]{2,}', '*', rawString)
            print(rawString)
            print('***')
            model_data.append(rawString)

        df['Movieyear'] = model_data
        dfAgg = df.groupby('Movieyear')['Rank'].max().reset_index()
        print(df)
        print(dfAgg)
        for i in range(0, len(dfAgg)):
            plt.bar(dfAgg.loc[i, 'Movieyear'], dfAgg.loc[i, 'Rank'])

        plt.xticks(np.arange(6, len(dfAgg), 8))
        plt.xlabel('Year')
        plt.ylabel('Rank')
        plt.title('Rated Years Movie')
        plt.show()


part=input("To run Assignment part A please enter A \n To run Assignment part B please enter B \n If you would like to run both please enter AB").upper()
print('\n')
if part =='A':
    AssignmentA()
elif part== 'B':
    AssignmentB()
elif part=='AB':
    AssignmentA()
    AssignmentB()




