from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_exchange(country):
    url = "https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_{}KRW".format(
        country
    )
    page = urlopen(url)

    contents = BeautifulSoup(page, "html.parser")
    exchanges = contents.find("p", class_="no_today")

    if exchanges:
        # 요소가 존재하는 경우에만 text 속성에 접근
        exchanges = exchanges.text.replace("\n", "")
        return exchanges
    else:
        return "환율 정보를 찾을 수 없습니다."
