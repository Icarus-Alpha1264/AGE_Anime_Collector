# -*- coding: utf-8 -*-
import re
import urllib3
import requests
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AnimeCollector:
    """每日推荐动漫列表采集器"""

    def __init__(self, selector=None, recommended_daily_list=[]):
        self.__selector = selector
        self.__recommended_daily_list = recommended_daily_list
        self.selector = 'https://www.agefans.tv/recommend'

    @property
    def selector(self):
        return self.__selector

    @property
    def recommended_daily_list(self):
        return self.__recommended_daily_list

    @selector.setter
    def selector(self, url=None):
        """通过改变url的方式来自动更新选择器"""
        response = requests.get(url=url, verify=False, timeout=5)
        text = response.text
        selector = etree.HTML(text)
        self.__selector = selector

    @recommended_daily_list.setter
    def recommended_daily_list(self, recommended_daily_list=[]):
        """通过向列表追加的方式新增列表元素"""
        self.__recommended_daily_list.append(recommended_daily_list)

    def get_last_page_numer(self):
        """获取每日推荐的最后一页的页码"""
        flip_bar_list = self.selector.xpath('//div[@class="blockcontent"]//div')
        up_flip_bar = flip_bar_list.pop(0)
        last_page_href = up_flip_bar.xpath('li//a/@href').pop()
        last_page_number_string = re.findall(pattern=r'\d+', string=last_page_href).pop()
        last_page_number = int(last_page_number_string)
        return last_page_number

    def parse_current_page_anime_list(self):
        """解析当前页面的动漫列表"""
        all_anime = self.selector.xpath('//ul//li')
        for anime in all_anime:
            title = anime.xpath('a//img/@alt').pop()
            extra_info = anime.xpath('a//img/@title').pop()
            url = 'https://www.agefans.tv' + anime.xpath('a/@href').pop()
            anime_dict = {'title': title, 'extra_info': extra_info, 'url': url}
            self.recommended_daily_list = anime_dict

    def parse_recommended_daily_anime_list(self, last_page_number=None):
        """解析每日推荐动漫列表"""
        for page_number in range(1, last_page_number + 1):
            self.selector = 'https://www.agefans.tv/recommend?page=' + str(page_number)
            self.parse_current_page_anime_list()

    def show_recommended_daily_anime_list(self):
        """格式化显示每日推荐动漫列表"""
        for anime in self.recommended_daily_list:
            print(anime['title'], anime['extra_info'], anime['url'])

    def run(self):
        """每日推荐动漫列表采集器启动程序"""
        last_page_number = self.get_last_page_numer()
        self.parse_recommended_daily_anime_list(last_page_number=last_page_number)
        # self.show_recommended_daily_anime_list()

if '__main__' == __name__:
    anime_collector = AnimeCollector()
    anime_collector.run()
    for anime in anime_collector.recommended_daily_list:
        print(anime)
