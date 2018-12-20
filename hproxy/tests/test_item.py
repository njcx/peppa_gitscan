#!/usr/bin/env python
"""
 Created by howie.hu at 2018/4/24.
"""

import unittest

from hproxy.spider.base_spider import TextField, AttrField, Item

HTML = """
<!DOCTYPE html>
<head>
    <title>豆瓣电影TOP250</title>
</head>
<body>
<ol class="grid_view">
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">1</em>
                    <a href="https://movie.douban.com/subject/1292052/">
                        <img alt="肖申克的救赎" src="https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p480747492.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292052/" class="">
                            <span class="title">肖申克的救赎</span>
                                    <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
                                <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
                        </a>
                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                        </p>

                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.6</span>
                                <span property="v:best" content="10.0"></span>
                                <span>827737人评价</span>
                        </div>
                            <p class="quote">
                                <span class="inq">希望让人自由。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
</body>
</html>
"""


# 定义继承自item的爬虫类
class DoubanItemsSpider(Item):
    target_item = TextField(css_select='div.item')
    title = TextField(css_select='span.title')
    cover = AttrField(css_select='div.pic>a>img', attr='src')
    abstract = TextField(css_select='span.inq')

    def tal_title(self, title):
        if isinstance(title, str):
            return title
        else:
            return ''.join([i.text.strip().replace('\xa0', '') for i in title])


class DoubanItemSpider(Item):
    title = TextField(css_select='head title')

    def tal_title(self, title):
        return title


class TestItem(unittest.TestCase):
    def test_get_items(self):
        items_data = DoubanItemsSpider.get_items(html=HTML)
        self.assertEqual(items_data[0].title, '肖申克的救赎/The Shawshank Redemption')

    def test_get_item(self):
        item_data = DoubanItemSpider.get_item(html=HTML)
        self.assertEqual(item_data['title'], '豆瓣电影TOP250')


if __name__ == '__main__':
    unittest.main()