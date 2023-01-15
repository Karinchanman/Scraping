#urllibからrequestっていうツールボックスを持ってくる
from urllib import request
from bs4 import BeautifulSoup
import time


def makeSoup(URL):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    #Request型を呼び出す
    hensu_request = request.Request(URL , headers=headers)
    print(hensu_request.headers)
    print(hensu_request.full_url)
    html = request.urlopen(hensu_request)
    #htmlをBeatifulSoupの型になおす
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(1)
    return soup

def scrape_line():
    #LINE占い
    soup_line=makeSoup(URL="https://fortune.line.me/contents/horoscope/")
    resultlist_line=soup_line.select("#__next > div.layout__wrapper > main > article > article > div.zodiac_container__T9OXy > div > a > div.zodiac-item_content__hOFiF > span.zodiac-item_name__c4Ypu")
    #print(resultlist_line[0].text)

    for result in resultlist_line:
        print(result.text)
    result_listの中に入ってる数だけ
    for index in range(len(resultlist_line)):
        print("{}位: {}".format(index+1,resultlist_line[index].text))
    
def scrape_docomo():
    #docomo占い
    soup_docomo=makeSoup(URL="https://service.smt.docomo.ne.jp/portal/fortune/src/fortune_ranking.html")
    #print(soup_docomo)
    resultlist_docomo=soup_docomo.select("body > div.postRank.-bdb.-ico01 > div > div.postRank__list > div > div.postRank__info > div.postRank__infoHead > div.postRank__infoHeadTtl > h3 ")
    resultlist_docomo_under=soup_docomo.select("body > div.postRank.-bdb.-ico01 > div > div.rankTggl > div.toggle-content > div > div > div.postRank__info > div.postRank__infoHead > div.postRank__infoHeadTtl > h3")
    print(resultlist_docomo)
    print(resultlist_docomo_under)
    print(resultlist_docomo[0].text)
    print(resultlist_docomo_under[0].text)
    print("ドコモ")

    for index in range(len(resultlist_docomo)):
        print("{}位：　{}".format(index+1,resultlist_docomo[index].text))
    for index in range(len(resultlist_docomo_under)):
        print("{}位：　{}".format(index+1,resultlist_docomo_under[index].text))
    
def scrape_asahi():
    #朝日新聞占い
    soup_asahi=makeSoup(URL="https://www.asahi.com/uranai/12seiza/")
    resultlist_asahi=soup_asahi.select("#MainInner > div > ol > li > dl > dt > a")
    print(resultlist_asahi)
    for index in range(len(resultlist_asahi)):
        print(resultlist_asahi[index].text)
 
    for result in resultlist_asahi:
         print(result.text)
    #result_listの中に入ってる数だけ
    for index in range(len(resultlist_asahi)):
        print("{}位: {}".format(index+1,resultlist_asahi[index].text)) 



def main():
    #scrape_line()
    #scrape_docomo()
    #scrape_asahi()
    

    
if __name__ == "__main__":
    main()