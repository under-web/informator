import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class Spider(object):

    def __int__(self, url, tag_1, tag_2, status):
        self.url = url
        self.tag_1 = tag_1
        self.tag_2 = tag_2
        self.status = status

    def get_stat_no_headles(self, url):
        r = requests.get(url)
        return r

    def get_list_block(self, url, tag1, tag2, tag3, tag4):
        list_result = []
        ua = UserAgent()
        headers = {'UserAgent': ua.Firefox}
        r = requests.get(url, headers=headers)
        if r.status_code == 403:
            print('Не пускает сервер 403')
            return []
        soup = BeautifulSoup(r.text, 'lxml')
        block = soup.find_all(tag1, tag2)

        for i in block:
            list_result.append(i.find(tag3, tag4).text)
        return list_result