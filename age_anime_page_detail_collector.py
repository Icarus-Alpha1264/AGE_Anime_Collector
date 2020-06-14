# -*- coding: utf-8 -*-
import urllib3
from urllib.parse import urljoin
import requests
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AnimeCollector:
    """AGE动漫详情页采集器"""

    def __init__(self, target_url="https://www.agefans.tv/detail/20090002", selector=None):
        self.__target_url = target_url
        self.__selector = selector
        self.update_selector(url=self.target_url)

    @property
    def target_url(self):
        return self.__target_url

    @property
    def selector(self):
        return self.__selector

    @selector.setter
    def selector(self, selector=None):
        if selector is not None:
            self.__selector = selector

    def update_selector(self, url=None):
        if url is not None:
            response = requests.get(url=url, verify=False, timeout=5)
            text = response.text
            selector = etree.HTML(text=text)
            self.selector = selector

    def parse_anime_name(self, blockcontent_node=None):
        """解析动漫的名字"""
        if blockcontent_node is not None:
            name = blockcontent_node.xpath("h4[@class='detail_imform_name']/text()")[0]
            print("动漫名称：", name)

    def parse_anime_brief_introduction(self, blockcontent_node=None):
        """解析动漫简介"""
        if blockcontent_node is not None:
            brief_introduction = "".join(blockcontent_node.xpath("div[@class='detail_imform_desc_pre']//p/text()"))
            print("动漫简介：", brief_introduction)

    def parse_anime_network_disk_resources(self, blockcontent_node=None):
        """解析动漫网盘资源"""
        if blockcontent_node is not None:
            print("网盘资源：")
            span_nodes = blockcontent_node.xpath("span[@class='res_links']")
            if span_nodes:
                nodes_count = len(span_nodes)
                for index in range(nodes_count):
                    span_node = span_nodes[index]
                    title = span_node.xpath("a[@class='res_links_a']/text()")[0]
                    url = "https://www.agefans.tv" + span_node.xpath("a[@class='res_links_a']/@href")[0]
                    try:
                        extraction_code = span_node.xpath("span[@class='res_links_pswd']/text()")[0][:4]
                    except IndexError:
                        extraction_code = ""
                    print("网盘资源名称：", title)
                    print("网盘资源地址：", url)
                    print("网盘资源提取码：", extraction_code)

    def parse_anime_relevant_recommendations(self, blockcontent_node=None):
        """解析动漫相关推荐"""
        if blockcontent_node is not None:
            print("相关推荐：")
            div_recommend_block = blockcontent_node.xpath("div[@id='recommend_block']")[0]
            ul_node = div_recommend_block.xpath("ul[@class='ul_li_a4']")[0]
            li_nodes = ul_node.xpath("li[@class='anime_icon1']")
            li_nodes_count = len(li_nodes)
            for li_node_index in range(li_nodes_count):
                li_node = li_nodes[li_node_index]
                a_nodes = li_node.xpath("a")
                a_nodes_count = len(a_nodes)
                for a_node_index in range(a_nodes_count):
                    a_node = a_nodes[a_node_index]
                    if a_node_index == 0:
                        anime_url = "https://www.agefans.tv" + a_node.xpath("@href")[0]
                        image_node = a_node.xpath("img")[0]
                        anime_image_url = "https:" + image_node.xpath("@data-src")[0]
                        print("动漫详情页地址：", anime_url)
                        print("动漫封面图片地址：", anime_image_url)
                    elif a_node_index == 1:
                        div_anime_name_node = a_node.xpath("div[@class='anime_icon1_name']")[0]
                        anime_name = div_anime_name_node.xpath("text()")[0]
                        print("动漫名称：", anime_name)

    def parse_anime_cover_image(self, baseblock_node=None):
        """解析动漫封面图片"""
        if baseblock_node is not None:
            blockcontent_node = baseblock_node.xpath("div[@class='blockcontent']")[0]
            cover_image_url = "https:" + blockcontent_node.xpath("img/@src")[0]
            print("动漫封面图片地址：", cover_image_url)

    def parse_anime_essential_information(self, baseblock_node=None):
        """解析动漫基本信息"""
        if baseblock_node is not None:
            print("基本信息：")
            div_blockcontent_node = baseblock_node.xpath("div[@class='blockcontent']")[0]
            baseblock2_node = div_blockcontent_node.xpath("div[@class='baseblock2']")[0]
            ul_blockcontent_node = baseblock2_node.xpath("ul[@class='blockcontent']")[0]
            li_nodes = ul_blockcontent_node.xpath("li[@class='detail_imform_kv']")
            if li_nodes:
                nodes_count = len(li_nodes)
                for index in range(nodes_count):
                    li_node = li_nodes[index]
                    info_value = li_node.xpath("span[@class='detail_imform_value']/text()")[0]
                    if index == 0:
                        region = info_value
                        print("地区：", region)
                    elif index == 1:
                        animation_category = info_value
                        print("动画种类：", animation_category)
                    elif index == 2:
                        original_name = info_value
                        print("原版名称：", original_name)
                    elif index == 3:
                        other_name = info_value
                        print("其它名称：", other_name)
                    elif index == 4:
                        original = info_value
                        print("原作：", original)
                    elif index == 5:
                        production_company = info_value
                        print("制作公司：", production_company)
                    elif index == 6:
                        premiere_time = info_value
                        print("首播时间：", premiere_time)
                    elif index == 7:
                        play_status = info_value
                        print("播放状态：", play_status)
                    elif index == 8:
                        plot_type = info_value
                        print("剧情类型：", plot_type)
                    elif index == 9:
                        tag = info_value
                        print("标签：", tag)
                    elif index == 10:
                        official_website = info_value
                        print("官方网站：", official_website)

    def parse_anime_related_anime(self, baseblock_node=None):
        """解析动漫相关动漫"""
        if baseblock_node is not None:
            print("相关动漫：")
            div_blockcontent_node = baseblock_node.xpath("div[@class='blockcontent']")[0]
            baseblock2_node = div_blockcontent_node.xpath("div[@class='baseblock2']")[0]
            ul_blockcontent_node = baseblock2_node.xpath("ul[@class='blockcontent']")[0]
            li_nodes = ul_blockcontent_node.xpath("li[@class='relates_series']")
            if li_nodes:
                nodes_count = len(li_nodes)
                for index in range(nodes_count):
                    li_node = li_nodes[index]
                    anime_title = li_node.xpath("a/text()")[0]
                    anime_url = urljoin(base="https://www.agefans.tv/", url=li_node.xpath("a/@href")[0])
                    print("动漫名称：", anime_title)
                    print("动漫详情页地址：", anime_url)

    def parse_left_node_elements(self):
        """解析页面左侧节点元素"""
        div_left_node = self.selector.xpath("//div[@class='div_left']")[0]
        div_baseblock_nodes = div_left_node.xpath("div[@class='baseblock']")
        baseblock_nodes_count = len(div_baseblock_nodes)
        for index in range(baseblock_nodes_count):
            baseblock_node = div_baseblock_nodes[index]
            if index == 0:
                self.parse_anime_cover_image(baseblock_node=baseblock_node)
            elif index == 1:
                self.parse_anime_essential_information(baseblock_node=baseblock_node)
            elif index == 2:
                self.parse_anime_related_anime(baseblock_node=baseblock_node)

    def parse_right_node_elements(self):
        """解析页面右侧节点元素"""
        div_right_node = self.selector.xpath("//div[@class='div_right']")[0]
        div_baseblock_nodes = div_right_node.xpath("div[@class='baseblock']")
        baseblock_nodes_count = len(div_baseblock_nodes)
        for index in range(baseblock_nodes_count):
            if index in [0, 1, 3, 5]:
                baseblock_node = div_baseblock_nodes[index]
                blockcontent_node = baseblock_node.xpath("div[@class='blockcontent']")[0]
                if index == 0:
                    self.parse_anime_name(blockcontent_node=blockcontent_node)
                elif index == 1:
                    self.parse_anime_brief_introduction(blockcontent_node=blockcontent_node)
                elif index == 3:
                    self.parse_anime_network_disk_resources(blockcontent_node=blockcontent_node)
                elif index == 5:
                    self.parse_anime_relevant_recommendations(blockcontent_node=blockcontent_node)

    def parse(self):
        """解析页面详情内容"""
        print("动漫详情页地址:", self.target_url)
        self.parse_left_node_elements()
        self.parse_right_node_elements()
