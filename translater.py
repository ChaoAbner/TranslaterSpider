# encoding = 'UTF-8'
__author__ = '_chao'


import requests
from colorama import init,Fore

from urllib import request
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3346.9 Safari/537.36'
}


def get_info(url):
        response = requests.get(url,headers = headers)
        soup = BeautifulSoup(response.text,'lxml')
        tra_word = soup.select('li.clearfix')
        juzi = soup.select('div.in-base-top.clearfix > div')
        if tra_word:
            for i in range(len(tra_word)):
                # 获取文本内容
                translation = tra_word[i].get_text()
                # 去掉字符串开头和结尾的空行
                print(Fore.CYAN + translation.strip())
                # 华丽的分割线
                print(Fore.RED + '=' * 30)
        elif juzi:
            tra_word = soup.select('div.in-base-top.clearfix > div')[0].text
            print(Fore.CYAN + tra_word)
            print(Fore.RED + '=' * 30)
        else:
            print(Fore.GREEN + 'Not Find!')
            print(Fore.RED + '=' * 30)


if __name__ == '__main__':
    print('+'*50)
    print('='*18 + '欢迎使用艾超翻译' + '='*18)
    print('+' * 50)
    init(autoreset=True)
    yuan_yin = [
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    ]
    while True:
        url = 'http://www.iciba.com/{}'
        input_word = input('Please enter your word: (enter q to exit) ')
        if str([i for i in yuan_yin]) not in input_word:
            input_word = request.quote(input_word)
        if input_word == 'q':
            exit(Fore.BLUE + '欢迎再次使用！')
        else:
            pass
        url = url.format(input_word)
        get_info(url)


