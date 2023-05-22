import requests

cookies = {
    'OJSSID': 'a658d2049d09fc0109265ca66a5672c1',
    '_ga_PDDBSXG8KH': 'GS1.1.1684731775.1.0.1684731775.0.0.0',
    '_ga': 'GA1.2.1538399755.1665134395',
    '_gid': 'GA1.2.997449010.1684731776',
    '_gat_gtag_UA_66624851_1': '1',
}

headers = {
    'authority': 'so01.tci-thaijo.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,th-TH;q=0.8,th;q=0.7,es;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'OJSSID=a658d2049d09fc0109265ca66a5672c1; _ga_PDDBSXG8KH=GS1.1.1684731775.1.0.1684731775.0.0.0; _ga=GA1.2.1538399755.1665134395; _gid=GA1.2.997449010.1684731776; _gat_gtag_UA_66624851_1=1',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://so01.tci-thaijo.org/index.php/GraduatePSRU/article/download/90661/71186',
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
#? write file to pdf
with open('test.pdf', 'wb') as f:
    f.write(response.content)