# 편안한 여행을 위한 환율정보 알림봇

## **Prerequisites**

사용한 라이브러리

- pip install discord
- pip install requests
- pip install bs4
- pip install datetime

```python
import discord, asyncio
from discord.ext import commands
from get_exchanges import get_exchange
from discord import Embed
from datetime import datetime

from bs4 import BeautifulSoup
from urllib.request import urlopen
```

### 사용 API

![Untitled]([https://file.thisisgame.com/upload/nboard/news/2018/08/10/20180810170552_4334.jpg])

Discord Bot API를 이용하여 웹에서 환율 정보를 크롤링해서 받아온 정보를 디코에서 바로 받아볼 수 있게 하는 봇을 개발함.

## 네이버 금융 사이트에서 환율 정보 가져오기

https://finance.naver.com/marketindex/

네이버 금융 증권 사이트에서 각 나라별 환율을 크롤링함

### 파싱

```python
url = "https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_{}KRW".format(
        country
    )
 page = urlopen(url)

 contents = BeautifulSoup(page, "html.parser")
 exchanges = contents.find("p", class_="no_today")
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/8e2df0eb-1ad3-4acb-a162-511b7b9230ed/924689ca-cab2-4ce6-9eee-a85f123cf5e9/Untitled.png)

## 소개

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/8e2df0eb-1ad3-4acb-a162-511b7b9230ed/130ae965-b31d-443a-98fe-9e9fa8071035/Untitled.png)

## 기능

### !환율

환율 정보를 확인할 수 있는 나라들을 전부 볼 수 있습니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/8e2df0eb-1ad3-4acb-a162-511b7b9230ed/b8bab029-4c3b-417d-b256-98d8b4855e50/Untitled.png)

### !환율_나라명

입력한 나라의 환율 정보와 사이트를 현재 시간과 함께 볼 수 있습니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/8e2df0eb-1ad3-4acb-a162-511b7b9230ed/14567ebd-e4cc-4916-9179-a95904d16c1a/Untitled.png)

## 참고

디스코드 봇 생성하기 : https://youtu.be/mw0Zmcg8V44?si=euYo10InQNKhcnZ9

디스코드 임베드 적용 방법 : [Discord Embed Creator (dan.onl)](https://embed.dan.onl/)

Beautifulsoup 사용 방법, 함수 사용 방법 :
