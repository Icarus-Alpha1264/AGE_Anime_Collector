# -*- coding: utf-8 -*-
import re
import urllib3
import requests
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AnimeCollector:
    """每日推荐动漫列表采集器"""

    def __init__(self, url="https://www.agefans.tv/recommend", selector=None):
        self.__url = url
        self.__selector = selector
        self.update_selector(url=self.url)

    @property
    def url(self):
        return self.__url

    @property
    def selector(self):
        return self.__selector

    @selector.setter
    def selector(self, selector=None):
        self.__selector = selector

    def update_selector(self, url=None):
        response = requests.get(url=url, verify=False, timeout=5)
        text = response.text
        selector = etree.HTML(text)
        self.selector = selector

    def get_last_page_numer(self):
        """获取每日推荐的最后一页的页码"""
        flip_bar_list = self.selector.xpath('//div[@class="blockcontent"]//div')
        up_flip_bar = flip_bar_list[0]
        last_page_href = up_flip_bar.xpath('li//a/@href')[-1]
        last_page_number_string = re.findall(pattern=r'\d+', string=last_page_href)[0]
        last_page_number = int(last_page_number_string)
        return last_page_number

    def parse_current_page_anime_list(self):
        """解析当前页面的动漫列表"""
        all_anime = self.selector.xpath('//ul//li')
        for anime in all_anime:
            title = anime.xpath('a//img/@alt')[0]
            try:
                extra_info = anime.xpath('a//img/@title')[0]
            except IndexError:
                extra_info = ''
            url = 'https://www.agefans.tv' + anime.xpath('a/@href')[0]
            print("title:", title, "extra_info:", extra_info, "url:", url)

    def parse_recommended_daily_anime_list(self, last_page_number):
        """解析每日推荐动漫列表"""
        for page_number in range(1, last_page_number + 1):
            url = 'https://www.agefans.tv/recommend?page=' + str(page_number)
            self.update_selector(url=url)
            self.parse_current_page_anime_list()

    def parse(self):
        """每日推荐动漫列表采集器启动程序"""
        last_page_number = self.get_last_page_numer()
        self.parse_recommended_daily_anime_list(last_page_number=last_page_number)
