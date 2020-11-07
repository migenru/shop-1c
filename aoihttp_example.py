import aiohttp
import asyncio
import re

from loguru import logger

# regex for ip-address
# str = '''109.160.76.209:8080	HTTP !	NOA	Болгария !	15% (4) -	26:10:20 20:16:48
# 5.58.50.5:8080	HTTP !	NOA	Украина	34% (166) -	26:10:20 20:14:56
# 103.78.252.65:8080	HTTPS !	NOA	Бангладеш !	40% (2) -	26:10:20 20:12:06
# 117.204.255.151:8080	HTTP !	NOA	Индия	38% (3) +	26:10:20 20:10:37
# 171.97.131.203:8080	HTTP !	NOA	Таиланд	21% (8) -	26:10:20 20:07:26
# 140.227.11.26:3128	HTTP	HIA	Япония	18% (13) -	26:10:20 19:40:54
# 101.108.172.74:8080	HTTPS !	NOA	Таиланд	новый -	26:10:20 19:34:44
# 136.228.165.138:8080	HTTP !	NOA	Мьянма	32% (67) -	26:10:20 19:29:15
# 103.214.113.28:8080	HTTP !	NOA	Индонезия	20% (13) -	26:10:20 19:28:04
# 160.238.251.142:3128	HTTP !	NOA	Бразилия	30% (56) -	26:10:20 19:25:39
# 5.58.88.175:8080	HTTPS !	NOA	Украина	38% (215) -	26:10:20 19:25:23
# 193.192.176.249:8080	HTTPS !	NOA	Польша !	43% (3) -	26:10:20 19:24:08
# 14.207.85.231:8080	HTTPS !	NOA	Таиланд	новый -	26:10:20 19:23:11
# 118.174.232.181:8080	HTTPS !	NOA	Таиланд	39% (58) -	26:10:20 19:23:01
# 179.222.94.2:8080	HTTPS !	NOA	Бразилия	50% (1) -	26:10:20 19:21:12
# 168.90.121.44:8080	HTTPS !	NOA	Бразилия	75% (3) +	26:10:20 19:18:03
# 103.126.218.138:8080	HTTP !	NOA	Бангладеш !	33% (1) -	26:10:20 19:16:56
# 183.88.224.206:8080	HTTP	HIA	Таиланд	13% (10) -	26:10:20 19:16:00
# 182.253.246.187:8080	HTTPS !	NOA	Индонезия	новый +	26:10:20 19:15:09
# 177.106.55.20:3128'''
#
# regestr = re.compile(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,4}')
# result = regestr.findall(str)
# print(result)

list_proxy = ['109.160.76.209:8080', '5.58.50.5:8080', '103.78.252.65:8080', '117.204.255.151:8080',
              '171.97.131.203:8080', '140.227.11.26:3128', '101.108.172.74:8080', '136.228.165.138:8080',
              '103.214.113.28:8080', '160.238.251.142:3128', '5.58.88.175:8080', '193.192.176.249:8080',
              '14.207.85.231:8080', '118.174.232.181:8080', '179.222.94.2:8080', '168.90.121.44:8080',
              '103.126.218.138:8080', '183.88.224.206:8080', '182.253.246.187:8080', '177.106.55.20:3128']


async def fetch_proxy(url: str) -> tuple:
    logger.info(f'parse url{url}')
    try:
        async with aiohttp.ClientSession() as session:
            logger.info(f'parse url{url}')
            async with session.get(f'http://ya.ru', proxy=f'{url}') as response:
                logger.info(f'Status {response.status}')
                return url, response.status
    except ValueError:
        return "", 500


async def fetch_fastest_proxy() -> str:
    futures = [fetch_proxy(url) for url in list_proxy]

    done, pending = await asyncio.wait(
        futures
    )
    best_url = ""
    valid_proxy = []
    for fut in pending:
        fut.cancel()

    for fut in done:
        status_code, best_url = fut.result()
        logger.info(f'return status: {status_code}, url {url}')
    return best_url

loop = asyncio.get_event_loop()
res = loop.run_until_complete(fetch_fastest_proxy())
loop.close()

logger.info(f'best url {res}')