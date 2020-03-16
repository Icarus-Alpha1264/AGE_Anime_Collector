# -*- coding: utf-8 -*-
import json
import re
import sys

import requests
import urllib3
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AnimeCollector:
    '''AGE动漫首页信息采集器'''

    def get_selector(self):
        '''解析AGE动漫首页并生成选择器'''
        url = 'https://www.agefans.tv/'
        response = requests.get(url=url, verify=False)
        text = response.text
        selector = etree.HTML(text)
        return selector

    def __init__(self):
        '''初始化AGE动漫首页信息采集器'''
        self.__selector = self.get_selector()

    @property
    def selector(self):
        return self.__selector

    def get_recommended_daily_list(self, recommended_daily_list=None):
        '''获取AGE动漫首页每日推荐动漫列表'''
        blockcontent_pattern = '//div[@class="div_left baseblock"]//div[@class="blockcontent"]'
        blockcontent_node = self.selector.xpath(blockcontent_pattern)
        blockcontent_node_first = blockcontent_node.pop(0)
        node_first_pattern = 'ul//li//a[position()=2]'
        recommended_daily = blockcontent_node_first.xpath(node_first_pattern)
        recommended_daily_list=[]
        for anime in recommended_daily:
            title = anime.xpath('div/text()').pop()
            href = 'https://www.agefans.tv/' + anime.xpath('@href').pop()
            title_href_dict = {'title': title, 'href': href}
            recommended_daily_list.append(title_href_dict)
        return recommended_daily_list

    def get_weekly_playlist(self, weekly_playlist=None):
        '''获取AGE动漫首页每周放送列表'''
        js_pattern = '//div[@class="blockcontent"]//script/text()'
        js_content = self.selector.xpath(js_pattern)
        js_string = ''.join(js_content)
        re_pattern = r'var new_anime_list = (.*);$'
        re_match = re.findall(pattern=re_pattern,
                              string=js_string, flags=re.MULTILINE)
        if not re_match:
            sys.exit(-1)
        anime_list = re_match.pop()
        weekly_playlist = json.loads(anime_list)
        return weekly_playlist

    def get_recent_update_left_list(self, recent_update_left_list=None):
        '''获取AGE动漫首页左侧的最近更新动漫列表'''
        return recent_update_left_list

    def get_recent_update_right_list(self, recent_update_right_list=None):
        '''获取AGE动漫首页右侧的最近更新动漫列表'''
        return recent_update_right_list

    def show_recommended_daily_list(self, recommended_daily_list=None):
        '''显示每日推荐列表'''
        print('每日推荐：')
        for anime in recommended_daily_list:
            print(anime['title'], anime['href'])

    def show_weekly_playlist(self, weekly_playlist=None):
        '''显示每周放送列表'''
        date_define_dict = {'周一': 1, '周二': 2, '周三': 3,
                            '周四': 4, '周五': 5, '周六': 6, '周日': 0}
        print('每周放送列表：')
        for key, value in date_define_dict.items():
            print(key + '：')
            for anime in weekly_playlist:
                if anime['wd'] == value:
                    print(anime['name'], anime['namefornew'],
                          'https://www.agefans.tv/detail/' + anime['id'])

    def show_recent_update_left_list(self, recent_update_left_list=None):
        '''显示最近更新列表（左）'''
        pass

    def show_recent_update_right_list(self, recent_update_right_list=None):
        '''显示最近更新列表（右）'''
        pass

    def run(self):
        '''启动AGE动漫首页信息采集器'''
        # 每日推荐
        recommended_daily_list = self.get_recommended_daily_list()
        self.show_recommended_daily_list(recommended_daily_list)
        # 每周放送列表
        # weekly_playlist = self.get_weekly_playlist()
        # self.show_weekly_playlist(weekly_playlist)
        # 最近更新（左）
        # recent_update_left_list = self.get_recent_update_left_list()
        # self.show_recent_update_left_list(recent_update_left_list)
        # 最近更新（右）
        # recent_update_right_list = self.get_recent_update_right_list()
        # self.show_recent_update_right_list(recent_update_right_list)


if '__main__' == __name__:
    # AGE动漫首页信息采集器程序启动入口
    anime_collector = AnimeCollector()
    # 启动AGE动漫首页信息采集器
    anime_collector.run()
