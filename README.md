# 편안한 여행을 위한 환율정보 알림봇

## 개요
### 목적
여행계획을 수립할 때 항상 고려하게 되는 환율에 대해 사람들이 편하게 접근할 수 있는 디스코드 봇을 제작하였음. <br>
다른 국가로 여행할 때 현지 통화의 환율을 알면 예산을 계획하고 여행 경비를 적절하게 관리할 수 있음.



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

## 사용 API

![discord](https://github.com/xxrainow/The_most_efficient_travel_helper/assets/90715224/c9d98c21-4864-4110-aff9-7c7c9a9b0765)


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


## 소개
<img width="377" alt="시작" src="https://github.com/xxrainow/The_most_efficient_travel_helper/assets/90715224/2d89f09e-fbe4-4ce8-9680-50bc85690b88">


## 기능

### !환율
환율 정보를 확인할 수 있는 나라들을 전부 볼 수 있습니다.

<img width="283" alt="환율" src="https://github.com/xxrainow/The_most_efficient_travel_helper/assets/90715224/76bed853-24cd-482f-869b-2cea78a291f5">


### !환율_나라명
입력한 나라의 환율 정보와 사이트를 현재 시간과 함께 볼 수 있습니다.

<img width="431" alt="호주" src="https://github.com/xxrainow/The_most_efficient_travel_helper/assets/90715224/22f459e5-5b98-4f7d-9e11-fc126660d5f0"><br>
<img width="454" alt="환율_스위스" src="https://github.com/xxrainow/The_most_efficient_travel_helper/assets/90715224/c88d257b-805c-40b5-9ad8-729dbfe253de">

## Heroku 서버 호스팅


## 참고

디스코드 봇 생성하기 : https://youtu.be/mw0Zmcg8V44?si=euYo10InQNKhcnZ9

디스코드 임베드 적용 방법 : [Discord Embed Creator (dan.onl)](https://embed.dan.onl/)

Beautifulsoup 사용 방법, 함수 사용 방법 : https://wikidocs.net/85739

HEROKU 서버 호스팅 : https://lektion-von-erfolglosigkeit.tistory.com/97





