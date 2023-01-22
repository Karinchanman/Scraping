# urllibからrequestっていうツールボックスを持ってくる
from urllib import request
from bs4 import BeautifulSoup
import time

def makeSoup(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    # Request型を呼び出す
    request_parameter = request.Request(url , headers=headers)
    html = request.urlopen(request_parameter)
    # htmlをBeautifulSoupの型になおす
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(1)

    return soup


def scrape_line():
    # LINE占い
    print("LINE占いの情報を取得しています...")
    soup = makeSoup(url = "https://fortune.line.me/contents/horoscope/")
    result_list_raw = soup.select("#__next > div.layout__wrapper > main > article > article >"
                                " div.zodiac_container__T9OXy > div > a > div.zodiac-item_content__hOFiF > span.zodiac-item_name__c4Ypu")
    # result_list_rawをひとつずつみてテキストだけとっている
    result_list = [result.text for result in result_list_raw]

    return result_list

    
def scrape_docomo():
    # docomo占い
    print("docomo占いの情報を取得しています...")
    soup = makeSoup(url = "https://service.smt.docomo.ne.jp/portal/fortune/src/fortune_ranking.html")
    result_list_top3_raw = soup.select("body > div.postRank.-bdb.-ico01 > div > div.postRank__list > div >"
                                    " div.postRank__info > div.postRank__infoHead > div.postRank__infoHeadTtl > h3 ")
    result_list_4th_raw = soup.select("body > div.postRank.-bdb.-ico01 > div > div.rankTggl > div.toggle-content > div >"
                                    " div > div.postRank__info > div.postRank__infoHead > div.postRank__infoHeadTtl > h3")
    result_list_top3 = [result.text for result in result_list_top3_raw]
    result_list_4th = [result.text for result in result_list_4th_raw]
    result_list = result_list_top3 + result_list_4th

    return result_list


def scrape_asahi():
    # 朝日新聞占い
    print("朝日新聞占いの情報を取得しています...")
    soup = makeSoup(url = "https://www.asahi.com/uranai/12seiza/")
    result_list_raw = soup.select("#MainInner > div > ol > li > dl > dt > a")
    result_list = [result.text for result in result_list_raw]

    return result_list


def main():
    zodiac_sign_list = ["てんびん座", "さそり座", "おひつじ座", "いて座", "おとめ座", "やぎ座", "うお座", "しし座", "かに座", "みずがめ座", "おうし座", "ふたご座"]

    line_result = scrape_line()
    docomo_result = scrape_docomo()
    asahi_result = scrape_asahi()

    # 星座とランキングを辞書型にしてる
    line_dict = {line_result[index]: index + 1 for index in range(len(line_result))}
    docomo_dict = {docomo_result[index]: index + 1 for index in range(len(docomo_result))}
    asahi_dict = {asahi_result[index]: index + 1 for index in range(len(asahi_result))}
        
    print("数字を入力してください")
    for index in range(len(zodiac_sign_list)):
        print("{}: {}".format(str(index).zfill(2), zodiac_sign_list[index]))

    input_string = input(">>")

    # zodiacに選んだ星座の名前を格納
    zodiac = zodiac_sign_list[int(input_string)]
    rank_list = [line_dict[zodiac] , docomo_dict[zodiac] , asahi_dict[zodiac]]
    average = round((sum(rank_list)) / len(rank_list),2)

    print("LINEでは {} 位です！".format(line_dict[zodiac]))
    print("docomoでは {} 位です！".format(docomo_dict[zodiac]))
    print("朝日新聞では {} 位です！".format(asahi_dict[zodiac]))
    print("平均 {} 位です！".format(average))
    
     
if __name__ == "__main__":
    main()