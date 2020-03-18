# AGE Anime Collector（AGE动漫采集器）
----
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
具体格式类型如下所示：
```
{'isnew': False, 'id': '20190054', 'wd': 1, 'name': '海盗战记', 'mtime': '2019-12-30 00:12:36', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190218', 'wd': 1, 'name': '非洲的动物上班族', 'mtime': '2019-12-23 00:38:32', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190203', 'wd': 1, 'name': '我不是说了能力要平均值么！', 'mtime': '2019-12-23 23:02:41', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190220', 'wd': 1, 'name': 'STAND MY HEROES PIECE OF TRUTH', 'mtime': '2019-12-23 23:11:27', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190261', 'wd': 1, 'name': '巴比伦', 'mtime': '2020-01-28 12:24:13', 'namefornew': '[TV 01-12]'}
......
```
----
## AGE动漫每日推荐采集器：age_anime_recommended_daily_collector.py
### 主要功能：
1. 实时自动采集AGE动漫每日推荐动漫列表。
### 环境需求：
1. Python 3.
2. lxml, requests.
### 使用教程：
1. 详细使用方法请参见age_anime_recommended_daily_collector.py。
2. 简洁使用方法如下所示：
```python
# -*- coding: utf-8 -*-
from age_anime_recommended_daily_collector import AnimeCollector
anime_collector = AnimeCollector()
anime_collector.run()
```
3. 提供一个用于获取AGE动漫首页每周放送列表的接口。
```python
# -*- coding: utf-8 -*-
from age_anime_recommended_daily_collector import AnimeCollector
anime_collector = AnimeCollector()
"""
你可以在age_anime_recommended_daily_collector.py中注释掉run()方法中的第73行代码self.show_recommended_daily_anime_list()，
以此来节约格式化显示每日推荐动漫列表的时间，直接获得可迭代的每日推荐动漫列表。
"""
anime_collector.run()
recommended_daily_list = anime_collector.recommended_daily_list
```
具体格式类型如下所示：
```
{'title': '魔法使的新娘', 'extra_info': '[TV 01-24+WEB00-02]', 'url': 'https://www.agefans.tv/detail/20170107'}
{'title': '青之驱魔师', 'extra_info': '', 'url': 'https://www.agefans.tv/detail/20110014'}
{'title': 'Comic Girls', 'extra_info': '[TV 01-12]', 'url': 'https://www.agefans.tv/detail/20180057'}
{'title': '11eyes -罪与罚与赎的少女-', 'extra_info': '[TV 01-12+OVA]', 'url': 'https://www.agefans.tv/detail/20090020'}
{'title': '少女与战车', 'extra_info': '[TV 01-12+OVA+SP]', 'url': 'https://www.agefans.tv/detail/20120035'}
......
```
