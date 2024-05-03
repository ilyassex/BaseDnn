import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


class SocialDeanon:
    def __init__(self):
        self.nickname = input('\n [+] Enter nickname: ')
        self.nickname = self.nickname.replace('@', '')

        self.red = Fore.RED
        self.green = Fore.GREEN
        self.magenta = Fore.MAGENTA

        self.output()

    def availability(self):
        req_list = [
            'https://www.instagram.com/',
            'https://github.com/',
            'https://rt.pornhub.com/users/',
            'https://ok.ru/',
            'https://vk.com/',
            'https://soundcloud.com/',
            'https://www.tumblr.com/blog/view/',
            'https://twitter.com/',
            'https://ask.fm/',
            'https://znanija.com/app/profile/',
            'https://www.deviantart.com/',
            'https://ru.linkedin.com/in/',
            'https://www.pinterest.com/',
            'https://www.reddit.com/r/',
            'https://www.reddit.com/user/'
        ]

        req_answer = []

        for req_url in req_list:
            social_req = req_url + self.nickname

            try:
                res = requests.get(social_req)
                if res:
                    print(self.green, ' ', social_req)
                    req_answer.append(social_req)
                else:
                    print(self.red, ' ', social_req)
            except:
                print(self.magenta, ' ', social_req)
        print(Style.RESET_ALL)

        return req_answer

    def output(self):
        req_answer = self.availability()

        len_design = 2 + 33 + len(self.nickname)

        a = len(req_answer)
        if a >= 1:
            print(' ' + '=' * len_design)
            print('  Результат:')
            for i in req_answer:
                print('  ' + i)
        else:
            print('\n Этот ник в социальных сетях не найден!')

        print(' ' + '=' * len_design)

        input()
