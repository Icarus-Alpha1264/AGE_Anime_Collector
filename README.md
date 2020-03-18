# AGE Anime Collector（AGE动漫采集器）
-
## AGE动漫首页采集器：age_anime_homepage_collector.py
### 主要功能：
1. 采集AGE动漫首页每日推荐。
2. 采集AGE动漫首页每周放送列表。
3. 采集AGE动漫首页最近更新（左）。
4. 采集AGE动漫首页最近更新（右）。
### 环境需求：
1. Python 3.
2. lxml, requests.
### 使用教程：
1. 详细使用方法请参见age_anime_homepage_collector.py。
2. 简洁使用方法如下所示：
```python
# -*- coding: utf-8 -*-
from age_anime_homepage_collector import AnimeCollector
anime_collector = AnimeCollector()
anime_collector.run()
```
3. 提供一个用于获取AGE动漫首页每周放送列表的接口。
```python
# -*- coding: utf-8 -*-
from age_anime_homepage_collector import AnimeCollector
anime_collector = AnimeCollector()
# 此接口已json化了源数据格式类型，可直接用来进行迭代。
weekly_release_list = anime_collector.get_weekly_release_list()
```
