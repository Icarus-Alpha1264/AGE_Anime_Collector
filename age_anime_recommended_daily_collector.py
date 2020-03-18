# -*- coding: utf-8 -*-
import sys
import urllib3
import requests
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AnimeCollector:

    def init_selector(self):
        url = 'https://www.agefans.tv/recommend'
        response = requests.get(url=url, verify=False, timeout=5)
        text = response.text
        selector = etree.HTML(text)
        return selector

    def __init__(self):
        self.__selector = self.init_selector()

    @property
    def selector(self):
        return self.__selector

    def parse_current_page_anime_list(self, anime_list=None):

        return anime_list

    def run(self):
        # 先解析当前页面所有的动漫列表信息
        # 再解析当前页面是否包含下一页这个元素，若包含则进入下一页继续解析，若不包含则结束程序。
        pass


if '__main__' == __name__:
    anime_collector = AnimeCollector()
    anime_collector.run()
