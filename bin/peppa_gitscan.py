import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "lib"))
# from utils import email_sender
from lxml import etree
from pyfiglet import Figlet
from peppa_gitscan_utils.logger import Logger
import requests

log = Logger.get_logger(__name__)
per_page = 50


def banner():
    banner_ = Figlet(font='slant')
    print(banner_.renderText('Peppa-GitScan'))
    print("<---------WELCOME TO USE THIS PROGRAM--------->")
    print("<---------v1.0 - Author - nJcx86--------->")
    print("\n")


class GitScan(object):

    def __init__(self, user, pwd):
        self.thread_pool = list()
        self.user = user
        self.pwd = pwd
        self.session = self.login()

    def _get_token(self, text):
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

    def get(self, page=1, keyword='test',data=None, header=None,):
        params = data
        url = 'https://github.com/search?p={page}&q={keyword}&type=Code'.format(page=page,keyword= keyword)
        if not header:
            header = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
            r = self.session.get(url , headers=header, params=params)
        else:
            r = self.session.get(url, headers=header, params=params)

        print(r.content)
        return r.content

    def process(self, page, keyword):

        html = etree.HTML(self.get(page=page, keyword=keyword))
        block = html.xpath("//div[@class='code-list-item "
                           "col-12 py-4 code-list-item-public ']")
        print("[+] Info: get item: %i" % len(block))

        print(block)

        codes = html.xpath(
            "//div[@class='code-list-item col-12 py-4 code-list-item-public ']"
            "/div[@class='file-box blob-wrapper']/table[@class='highlight']"
            "/tr/td[@class='blob-code blob-code-inner']")

        print(codes)

        nums = html.xpath(
            "//div[@class='code-list-item col-12 py-4 code-list-item-public "
            "']/div[@class='file-box blob-wrapper']/table[@class='"
            "highlight']/tr/td[@class='blob-num']/a")

        for i in range(len(nums)):
            try:
                text = etree.tostring(codes[i], method='text')
                print(text)
            except UnicodeEncodeError:
                continue


if __name__ == '__main__':
    banner()
    scanner = GitScan(user='', pwd='')
    print(scanner.process(page=1, keyword='baidu'))

