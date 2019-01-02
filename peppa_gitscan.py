from utils import logger
from utils import email_sender
from lxml import etree
from bs4 import BeautifulSoup
import settings
import requests

log = logger.logger(__name__)
TOKEN = settings.TOKEN
per_page = 50




class GitScan(object):

    def __init__(self, user, pwd):
        self.thread_pool = list()
        self.user = user
        self.pwd = pwd
        self.session = self.login()

    def _get_token(self,text):
        html = etree.HTML(text)
        t = html.xpath("//input[@name='authenticity_token']")
        try:
            token = t[0].get('value')
        except Exception as e:
            log.error(e)
        return token

    def login(self,):
        try:
            data = {'commit': 'Sign in', 'login': self.user, 'password': self.pwd}
            session = requests.Session()
            header = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}

            r = session.get("https://github.com/login", headers=header)
            data['authenticity_token'] = self._get_token(r.content)
            r = session.post("https://github.com/session", headers=header, data=data)
            return session
        except Exception as e:
            print(e)
            log.error(e)

    def get(self, page = 1, keyword = 'test',data=None, header=None,):
        params = data
        url = 'https://github.com/search?p={page}&q={keyword}&type=Code'.format(page=page,keyword= keyword)
        if not header:
            header = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
            r = self.session.get(url , headers=header, params=params)
        else:
            r = self.session.get(url, headers=header, params=params)
        return r.content


if __name__ == '__main__':
    scanner = GitScan(user='',pwd='')
    print(scanner.get())

