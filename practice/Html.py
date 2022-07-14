from bs4 import BeautifulSoup
import argparse
import requests

ap = argparse.ArgumentParser()
ap.add_argument("-U", "--url", help="邮件发送者地址")
args = vars(ap.parse_args())


def DownHtml(url):
    print(url)
    htmldocment = requests.get(url)
    soup = BeautifulSoup(htmldocment.text, 'html.parser')
    imglist = soup.find_all('img')
    for item in imglist:
        uri=item.get('src')
        print(uri)


DownHtml(args["url"])
