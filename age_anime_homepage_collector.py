# -*- coding: utf-8 -*-
import json
import re
import sys

import requests
import urllib3
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AnimeCollector:
    """AGE动漫详情页采集器"""

    def __init__(self, url="https://www.agefans.tv", selector=None):
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

    def parse_common_part(self, message=None, div_blockcontent_node=None):
        """公共解析部分"""
        print(message)
        ul_node = div_blockcontent_node.xpath("ul[@class='ul_li_a5']")[0]
        li_nodes = ul_node.xpath("li[@class='anime_icon1']")
        nodes_count = len(li_nodes)
        for index in range(nodes_count):
            li_node = li_nodes[index]
            a_node = li_node.xpath("a")[0]
            url = "https://www.agefans.tv/" + a_node.xpath("@href")[0]
            image_node = a_node.xpath("img[@class='anime_icon1_img']")[0]
            title = image_node.xpath("@alt")[0]
            try:
                extra_info = image_node.xpath("@title")[0]
            except IndexError:
                extra_info = ""
            image_url = "https:" + image_node.xpath("@src")[0]
            print("url:", url, "title:", title, "extra info:", extra_info, "image url:", image_url)

    def parse_left_elements(self):
        """页面左侧元素解析"""
        div_left_baseblock_node = self.selector.xpath("//div[@class='div_left baseblock']")[0]
        div_blockcontent_nodes = div_left_baseblock_node.xpath("div[@class='blockcontent']")
        nodes_count = len(div_blockcontent_nodes)
        for index in range(nodes_count):
            div_blockcontent_node = div_blockcontent_nodes[index]
            if index == 0:
                message = "recommended daily:"
            else:
                message = "recent updates left:"
            self.parse_common_part(message=message, div_blockcontent_node=div_blockcontent_node)

    def parse_weekly_release(self, message=None, div_blockcontent_node=None):
        """每周放送列表解析"""
        print(message)
        javascript_original_content = div_blockcontent_node.xpath("script/text()")
        javascript_string_content = "".join(javascript_original_content)
        re_match = re.findall(pattern=r"var new_anime_list = (.*);", string=javascript_string_content,
                              flags=re.MULTILINE)
        if not re_match:
            sys.exit(-1)
        anime_list = re_match[0]
        weekly_release_list = json.loads(anime_list)
        weekly_release_list_count = len(weekly_release_list)
        for index in range(weekly_release_list_count):
            print(weekly_release_list[index])

    def parse_recent_updates_right(self, message=None, div_blockcontent_node=None):
        """最近更新（右）解析"""
        print(message)
        ul_node = div_blockcontent_node.xpath("ul[@id='anime_update']")[0]
        li_nodes = ul_node.xpath("li[@class='one_new_anime']")
        nodes_count = len(li_nodes)
        for index in range(nodes_count):
            li_node = li_nodes[index]
            title = li_node.xpath("a[@class='one_new_anime_name']/text()")[0]
            url = "https://www.agefans.tv" + li_node.xpath("a[@class='one_new_anime_name']/@href")[0]
            update_time = li_node.xpath("span[@class='anime_update_date asciifont']/text()")[0]
            print("title:", title, "url:", url, "update time:", update_time)

    def parse_right_elements(self):
        """页面右侧元素解析"""
        div_right_baseblock_node = self.selector.xpath("//div[@class='div_right baseblock']")[0]
        div_blockcontent_nodes = div_right_baseblock_node.xpath("div[@class='blockcontent']")
        div_blockcontent_nodes_count = len(div_blockcontent_nodes)
        for index in range(div_blockcontent_nodes_count):
            div_blockcontent_node = div_blockcontent_nodes[index]
            if index == 0:
                message = "weekly release:"
                self.parse_weekly_release(message=message, div_blockcontent_node=div_blockcontent_node)
            else:
                message = "recent updates right:"
                self.parse_recent_updates_right(message=message, div_blockcontent_node=div_blockcontent_node)

    def parse(self):
        """解析主函数"""
        self.parse_left_elements()
        self.parse_right_elements()
