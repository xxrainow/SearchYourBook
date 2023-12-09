# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio
from discord.ext import commands
from get_exchanges import get_exchange
from discord import Embed
from datetime import datetime


intents = discord.Intents.default()
intents.all()
intents.message_content = True
current_time = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")

bot = commands.Bot(command_prefix="!", intents=intents)
countries = {
    "미국": "USD",
    "유럽연합": "EUR",
    "일본": "JPY",
    "중국": "CNY",
    "홍콩": "HKD",
    "대만": "TWD",
    "영국": "GBP",
    "캐나다": "CAD",
    "스위스": "CHF",
    "스웨덴": "SEK",
    "호주": "AUD",
    "튀르키예": "TRY",
    "몽골": "MNT",
    "덴마크": "DKK",
    "노르웨이": "NOK",
    "태국": "THB",
    "싱가포르": "SGD",
    "필리핀": "PHP",
}


@bot.event
async def on_ready():  # 봇이 실행되면 한 번 실행됨
    print("봇이 준비되었습니다. 디스코드 화면으로 넘어가세요")
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game("환율 정보 업데이트")
    )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!시작"):
        embed = discord.Embed(
            title="환율정보알림봇 도움말",
            description="안녕하세요! 성공적인 해외여행을 위한 환율 정보를 알려드리는 환율정보알림봇입니다! 먼저 어느 나라로 여행을 떠나고 싶으신가요? 떠나고 싶은 여행지에 대한 정보를 모두 알려드립니다!",
            colour=0x00B0F4,
            timestamp=datetime.now(),
        )

        embed.add_field(name="명령어 접두사", value="'!'로 사용하실 수 있습니다", inline=False)
        embed.add_field(
            name="!환율", value="환율 정보를 검색할 수 있는 나라 리스트를 알려드립니다", inline=False
        )
        embed.add_field(
            name="!환율_나라명",
            value="떠나고 싶은 나라의 환율 정보가 궁금하시다면 '!환율_나라명'이라고 입력해주세요",
            inline=False,
        )

        embed.set_image(
            url="https://cdn.travie.com/news/photo/first/201710/img_19975_1.jpg"
        )

        embed.set_footer(text="환율정보알림봇")

        await message.channel.send(embed=embed)

    await bot.process_commands(message)


@bot.command()
async def 환율(ctx):
    embed = discord.Embed(
        title="환율정보알림봇 도움말",
        description="어느 나라의 환율이 궁금하신가요?",
        colour=0xE4F500,
        timestamp=datetime.now(),
    )
    embed.add_field(name="!환율_나라명", value="나라명을 아래에서 골라서 입력해주세요", inline=False)
    for key, value in countries.items():
        if value != "":
            embed.add_field(name=key, value=value, inline=True)
    embed.set_footer(text="환율정보알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_미국(ctx):
    exchange_rate = get_exchange("USD")
    embed = discord.Embed(
        title="미국 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [미국 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_USD.png"
    )

    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_the_United_States_%28DoS_ECA_Color_Standard%29.svg/1280px-Flag_of_the_United_States_%28DoS_ECA_Color_Standard%29.svg.png"
    )

    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_유럽연합(ctx):
    exchange_rate = get_exchange("EUR")
    embed = discord.Embed(
        title="유럽연합 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [유럽연합 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_EURKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/1200px-Flag_of_Europe.svg.png"
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_EUR.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_일본(ctx):
    exchange_rate = get_exchange("JPY")
    embed = discord.Embed(
        title="일본 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [일본 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_JPYKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/225px-Flag_of_Japan.svg.png"
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_JPY.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_중국(ctx):
    exchange_rate = get_exchange("CNY")
    embed = discord.Embed(
        title="중국 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [중국 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_CNYKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_CNY.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/1024px-Flag_of_the_People%27s_Republic_of_China.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_홍콩(ctx):
    exchange_rate = get_exchange("HKD")
    embed = discord.Embed(
        title="홍콩 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [홍콩 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_HKDKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_HKD.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Flag_of_Hong_Kong.svg/225px-Flag_of_Hong_Kong.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_대만(ctx):
    exchange_rate = get_exchange("TWD")
    embed = discord.Embed(
        title="대만 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [대만 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_TWDKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_TWD.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/383px-Flag_of_the_Republic_of_China.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_영국(ctx):
    exchange_rate = get_exchange("GBP")
    embed = discord.Embed(
        title="영국 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [영국 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_GBPKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_GBP.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Flag_of_the_United_Kingdom_%281-2%29.svg/1920px-Flag_of_the_United_Kingdom_%281-2%29.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_캐나다(ctx):
    exchange_rate = get_exchange("CAD")
    embed = discord.Embed(
        title="캐나다 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [캐나다 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_CADKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_CAD.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/225px-Flag_of_Canada_%28Pantone%29.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_스위스(ctx):
    exchange_rate = get_exchange("CHF")
    embed = discord.Embed(
        title="스위스 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [스위스 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_CHFKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_CHF.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/225px-Flag_of_Switzerland.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_스웨덴(ctx):
    exchange_rate = get_exchange("SEK")
    embed = discord.Embed(
        title="스웨덴 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [스웨덴 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_SEKKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_SEK.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Sweden.svg/225px-Flag_of_Sweden.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_호주(ctx):
    exchange_rate = get_exchange("AUD")
    embed = discord.Embed(
        title="호주 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [호주 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_AUDKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_AUD.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/225px-Flag_of_Australia.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_튀르키예(ctx):
    exchange_rate = get_exchange("TRY")
    embed = discord.Embed(
        title="튀르키예 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [튀르키예 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_TRYKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_TRY.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_몽골(ctx):
    exchange_rate = get_exchange("MNT")
    embed = discord.Embed(
        title="몽골 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [몽골 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_MNTKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_MNT.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Mongolia.svg/225px-Flag_of_Mongolia.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_덴마크(ctx):
    exchange_rate = get_exchange("DKK")
    embed = discord.Embed(
        title="덴마크 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [덴마크 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_DKKKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_DKK.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/225px-Flag_of_Denmark.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_노르웨이(ctx):
    exchange_rate = get_exchange("NOK")
    embed = discord.Embed(
        title="노르웨이 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [노르웨이 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_NOKKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_NOK.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/225px-Flag_of_Norway.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_태국(ctx):
    exchange_rate = get_exchange("THB")
    embed = discord.Embed(
        title="태국 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [태국 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_THBKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_THB.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_Thailand.svg/225px-Flag_of_Thailand.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_싱가포르(ctx):
    exchange_rate = get_exchange("SGD")
    embed = discord.Embed(
        title="싱가포르 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [싱가포르 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_SGDKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_SGD.png"
    )
    embed.set_image(url="https://commons.wikimedia.org/wiki/File:Flag_of_Singapore.svg")
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


@bot.command()
async def 환율_필리핀(ctx):
    exchange_rate = get_exchange("PHP")
    embed = discord.Embed(
        title="필리핀 환율정보",
        description=f"> 환율\n```\n{exchange_rate}\n```\n*{current_time}* 기준",
        colour=0x00F552,
        timestamp=datetime.now(),
    )
    embed.add_field(
        name="사이트 바로가기",
        value="더 많은 정보를 원하신다면 [필리핀 환율 사이트 바로가기](https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_PHPKRW)를 눌러주세요",
        inline=False,
    )
    embed.set_thumbnail(
        url="https://ssl.pstatic.net/imgfinance/nfinance/flag/flag_PHP.png"
    )
    embed.set_image(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_the_Philippines.svg/1280px-Flag_of_the_Philippines.svg.png"
    )
    embed.set_footer(text="환율정보 알림봇")
    await ctx.send(embed=embed)


with open("bot_token.txt", "r") as file:
    TOKEN = file.read().strip()

bot.run(TOKEN)
