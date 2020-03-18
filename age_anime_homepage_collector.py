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
        response = requests.get(url=url, verify=False, timeout=5)
        text = response.text
        selector = etree.HTML(text)
        return selector

    def __init__(self):
        '''初始化AGE动漫首页信息采集器'''
        self.__selector = self.get_selector()

    @property
    def selector(self):
        '''通过构建property来返回选择器'''
        return self.__selector

    def get_recommended_daily_or_recent_updates_left_list(self, index=None):
        '''获取AGE动漫首页左侧的每日推荐和最近更新（左）动漫列表'''
        blockcontent_pattern = '//div[@class="div_left baseblock"]//div[@class="blockcontent"]'
        blockcontent_node = self.selector.xpath(blockcontent_pattern)
        blockcontent_node_index = blockcontent_node.pop(index)
        node_index_pattern = 'ul//li//a[position()=1]'
        anime_index = blockcontent_node_index.xpath(node_index_pattern)
        anime_list = []
        for anime in anime_index:
            title = anime.xpath('img/@alt').pop()
            extra_info = ''
            extra_info_parse = anime.xpath('span/text()')
            if extra_info_parse:
                extra_info = extra_info_parse.pop()
            url = 'https://www.agefans.tv' + anime.xpath('@href').pop()
            title_extra_info_url_dict = {'title': title,
                                         'extra_info': extra_info, 'url': url}
            anime_list.append(title_extra_info_url_dict)
        return anime_list

    def get_weekly_release_list(self):
        '''获取AGE动漫首页右侧的每周放送列表'''
        blockcontent_pattern = '//div[@class="div_right baseblock"]//div[@class="blockcontent"]'
        blockcontent_parse = self.selector.xpath(blockcontent_pattern)
        blockcontent = blockcontent_parse.pop(0)
        js_pattern = 'script/text()'
        js_content = blockcontent.xpath(js_pattern)
        js_string = ''.join(js_content)
        re_pattern = r'var new_anime_list = (.*);'
        re_match = re.findall(pattern=re_pattern,
                              string=js_string, flags=re.MULTILINE)
        if not re_match:
            sys.exit(-1)
        anime_list = re_match.pop()
        weekly_release_list = json.loads(anime_list)
        return weekly_release_list

    def get_recent_updates_right_list(self):
        '''获取AGE动漫首页右侧的最近更新动漫列表'''
        blockcontent_pattern = '//div[@class="div_right baseblock"]//div[@class="blockcontent"]'
        blockcontent_node = self.selector.xpath(blockcontent_pattern)
        blockcontent_node_second = blockcontent_node.pop(1)
        node_second_pattern = 'ul//li'
        recent_update_right = blockcontent_node_second.xpath(
            node_second_pattern)
        recent_update_right_list = []
        for anime in recent_update_right:
            title = anime.xpath('a/text()').pop()
            url = 'https://www.agefans.tv' + anime.xpath('a/@href').pop()
            update_time = anime.xpath('span/text()').pop()
            title_url_update_dict = {'title': title,
                                     'url': url, 'update_time': update_time}
            recent_update_right_list.append(title_url_update_dict)
        return recent_update_right_list

    def show_recommended_daily_or_recent_updates_left_list(self, message=None, anime_list=None):
        '''整合了展示AGE动漫首页左侧的包括每日更新和最近更新（左）动漫列表'''
        print(message)
        for anime in anime_list:
            print(anime['title'], anime['extra_info'], anime['url'])

    def show_weekly_release_list(self, message=None, anime_list=None):
        '''显示每周放送动漫列表'''
        date_define_dict = {'周一': 1, '周二': 2, '周三': 3,
                            '周四': 4, '周五': 5, '周六': 6, '周日': 0}
        print(message)
        for key, value in date_define_dict.items():
            print(key + '：')
            for anime in anime_list:
                if anime['wd'] == value:
                    is_new = ''
                    if anime['isnew'] == True:
                        is_new = 'new!'
                    print(anime['name'], anime['namefornew'], is_new,
                          'https://www.agefans.tv/detail/' + anime['id'])

    def show_recent_updates_right_list(self, message=None, anime_list=None):
        '''显示右侧的最近更新动漫列表'''
        print(message)
        for anime in anime_list:
            print(anime['title'], anime['update_time'], anime['url'])

    def integration_mode_show(self, keyword=None, anime_list=None):
        '''整合模式显示动漫列表'''
        if keyword == 'recommended_daily':
            message = '每日推荐：'
            self.show_recommended_daily_or_recent_updates_left_list(
                message=message, anime_list=anime_list)
        elif keyword == 'weekly_release':
            message = '每周放送列表：'
            self.show_weekly_release_list(
                message=message, anime_list=anime_list)
        elif keyword == 'recent_updates_left':
            message = '最近更新（左）：'
            self.show_recommended_daily_or_recent_updates_left_list(
                message=message, anime_list=anime_list)
        elif keyword == 'recent_updates_right':
            message = '最近更新（右）：'
            self.show_recent_updates_right_list(
                message=message, anime_list=anime_list)
        else:
            pass

    def run(self):
        '''启动AGE动漫首页信息采集器'''
        # 每日推荐
        recommended_daily_list = self.get_recommended_daily_or_recent_updates_left_list(
            index=0)
        self.integration_mode_show(
            keyword='recommended_daily', anime_list=recommended_daily_list)
        # 每周放送列表
        weekly_release_list = self.get_weekly_release_list()
        self.integration_mode_show(
            keyword='weekly_release', anime_list=weekly_release_list)
        # 最近更新（左）
        recent_updates_left_list = self.get_recommended_daily_or_recent_updates_left_list(
            index=1)
        self.integration_mode_show(
            keyword='recent_updates_left', anime_list=recent_updates_left_list)
        # 最近更新（右）
        recent_updates_right_list = self.get_recent_updates_right_list()
        self.integration_mode_show(
            keyword='recent_updates_right', anime_list=recent_updates_right_list)
