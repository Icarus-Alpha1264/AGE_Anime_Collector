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
具体格式类型如下所示：
```json
{'isnew': False, 'id': '20190054', 'wd': 1, 'name': '海盗战记', 'mtime': '2019-12-30 00:12:36', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190218', 'wd': 1, 'name': '非洲的动物上班族', 'mtime': '2019-12-23 00:38:32', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190203', 'wd': 1, 'name': '我不是说了能力要平均值么！', 'mtime': '2019-12-23 23:02:41', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190220', 'wd': 1, 'name': 'STAND MY HEROES PIECE OF TRUTH', 'mtime': '2019-12-23 23:11:27', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190261', 'wd': 1, 'name': '巴比伦', 'mtime': '2020-01-28 12:24:13', 'namefornew': '[TV 01-12]'}
{'isnew': False, 'id': '20190342', 'wd': 1, 'name': '超级小白', 'mtime': '2020-03-16 00:41:11', 'namefornew': '00:00 第23话'}
{'isnew': False, 'id': '20200044', 'wd': 1, 'name': '异度侵入 ID:INVADED', 'mtime': '2020-03-16 00:34:24', 'namefornew': '00:30 第12话'}
{'isnew': False, 'id': '20200034', 'wd': 1, 'name': '别对映像研出手！', 'mtime': '2020-03-16 01:07:26', 'namefornew': '01:00 第11话'}
{'isnew': False, 'id': '20180105', 'wd': 1, 'name': '智龙迷城 (2018)', 'mtime': '2020-03-17 00:02:56', 'namefornew': '18:25 第101话'}
{'isnew': False, 'id': '20190058', 'wd': 1, 'name': '思维覆写', 'mtime': '2020-03-16 21:50:36', 'namefornew': '20:45 第11话'}
{'isnew': False, 'id': '20200049', 'wd': 1, 'name': '室内露营△', 'mtime': '2020-03-16 22:02:35', 'namefornew': '20:55 第11话'}
{'isnew': False, 'id': '20190124', 'wd': 1, 'name': '梦幻之星online2 EPISODE ORACLE', 'mtime': '2020-03-16 23:54:21', 'namefornew': '23:00 第23话'}
{'isnew': False, 'id': '20200061', 'wd': 1, 'name': '成群结伴！西顿学园', 'mtime': '2020-03-16 23:55:59', 'namefornew': '23:30 第11话'}
{'isnew': False, 'id': '20200087', 'wd': 1, 'name': 'ReBIRTH', 'mtime': '2020-03-08 19:27:31', 'namefornew': '第9话'}
{'isnew': False, 'id': '20180190', 'wd': 2, 'name': '平凡职业成就世界最强', 'mtime': '2020-02-26 20:47:47', 'namefornew': '第OVA2话(完结)'}
{'isnew': False, 'id': '20190074', 'wd': 2, 'name': 'Z/X Code reunion', 'mtime': '2019-12-25 00:02:56', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20200046', 'wd': 2, 'name': 'A3！满开剧团 春&夏', 'mtime': '2020-01-28 05:42:10', 'namefornew': '本周停播 00:30 第3话'}
{'isnew': False, 'id': '20170082', 'wd': 2, 'name': '黑色五叶草', 'mtime': '2020-03-17 18:30:27', 'namefornew': '18:25 第126话'}
{'isnew': False, 'id': '20190133', 'wd': 2, 'name': '钻石王牌 act2', 'mtime': '2020-03-17 18:31:48', 'namefornew': '18:30 第50话'}
{'isnew': False, 'id': '20190067', 'wd': 2, 'name': 'BanG Dream! 第三季', 'mtime': '2020-03-17 19:09:55', 'namefornew': '第11话'}
{'isnew': False, 'id': '20200050', 'wd': 2, 'name': '八十龟酱观察日记 第二季', 'mtime': '2020-02-25 07:07:55', 'namefornew': '第8话'}
{'isnew': False, 'id': '20190211', 'wd': 3, 'name': '神田川JET GIRLS', 'mtime': '2020-01-24 17:09:18', 'namefornew': '第13话(完结)'}
{'isnew': False, 'id': '20190183', 'wd': 3, 'name': '旗扬！兽道', 'mtime': '2019-12-18 22:05:10', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190264', 'wd': 3, 'name': '浦岛坂田船的日常', 'mtime': '2019-12-26 19:09:58', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190092', 'wd': 3, 'name': '这个勇者明明超强却过分慎重', 'mtime': '2019-12-28 03:11:36', 'namefornew': '第12话(完结)'}
{'isnew': True, 'id': '20200033', 'wd': 3, 'name': '异世界四重奏 第二季', 'mtime': '2020-03-18 00:48:51', 'namefornew': '00:45 第10话'}
{'isnew': True, 'id': '20200037', 'wd': 3, 'name': '魔术士欧菲流浪之旅', 'mtime': '2020-03-18 01:01:52', 'namefornew': '01:05 第11话'}
{'isnew': True, 'id': '20190057', 'wd': 3, 'name': '歌牌情缘 第三季', 'mtime': '2020-03-18 02:34:42', 'namefornew': '02:30 第23话'}
{'isnew': True, 'id': '20190152', 'wd': 3, 'name': '七原罪 第三季(诸神的逆鳞)', 'mtime': '2020-03-18 19:10:20', 'namefornew': '18:00 第23话'}
{'isnew': True, 'id': '20190205', 'wd': 3, 'name': '鸭子的天空', 'mtime': '2020-03-18 19:32:46', 'namefornew': '第24话'}
{'isnew': False, 'id': '20190204', 'wd': 3, 'name': '虚空魔法使 第二季', 'mtime': '2020-02-26 19:38:26', 'namefornew': '第21话(完结)'}
{'isnew': False, 'id': '20200008', 'wd': 3, 'name': '因为太怕痛就全点防御力了', 'mtime': '2020-03-11 22:32:08', 'namefornew': '22:30 第10话'}
{'isnew': False, 'id': '20200048', 'wd': 3, 'name': 'number24', 'mtime': '2020-03-11 22:39:32', 'namefornew': '22:35 第10话'}
{'isnew': False, 'id': '20200068', 'wd': 3, 'name': 'Re：从零开始的异世界生活 新编集版', 'mtime': '2020-03-11 23:33:14', 'namefornew': '23:30 第9话'}
{'isnew': False, 'id': '20190117', 'wd': 4, 'name': '叛逆性百万亚瑟王 第二季', 'mtime': '2019-11-09 05:17:21', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190184', 'wd': 4, 'name': '书虫的下克上～为了成为图书管理员而不择手段～', 'mtime': '2020-03-11 02:51:47', 'namefornew': '第14.5话(完结)'}
{'isnew': False, 'id': '20190073', 'wd': 4, 'name': '喜欢本大爷的竟然只有你一个？', 'mtime': '2019-12-26 19:05:36', 'namefornew': '[TV 01-12]'}
{'isnew': False, 'id': '20190036', 'wd': 4, 'name': '放学后桌游俱乐部', 'mtime': '2019-12-19 02:34:13', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190221', 'wd': 4, 'name': 'BEASTARS', 'mtime': '2019-12-26 19:07:59', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190214', 'wd': 4, 'name': '高达创形者Re:RISE', 'mtime': '2019-12-26 19:26:22', 'namefornew': '第13话(完结)'}
{'isnew': False, 'id': '20190122', 'wd': 4, 'name': '超人高中生们即便在异世界也能从容生存！', 'mtime': '2019-12-19 22:05:32', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190040', 'wd': 4, 'name': '碧蓝航线', 'mtime': '2020-03-13 23:15:21', 'namefornew': '第11话'}
{'isnew': False, 'id': '20190208', 'wd': 4, 'name': '刺客守则', 'mtime': '2019-12-26 23:03:02', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20200036', 'wd': 4, 'name': '空挺Dragons', 'mtime': '2020-01-09 01:07:00', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20200039', 'wd': 4, 'name': '星掠者', 'mtime': '2020-03-12 01:10:24', 'namefornew': '01:05 第10话'}
{'isnew': False, 'id': '20190210', 'wd': 4, 'name': '无限之住人', 'mtime': '2020-03-12 02:53:24', 'namefornew': '第22话'}
{'isnew': False, 'id': '20200031', 'wd': 4, 'name': 'NEKOPARA', 'mtime': '2020-03-13 00:11:35', 'namefornew': '第10话'}
{'isnew': False, 'id': '20200029', 'wd': 4, 'name': '奇幻☆怪盗', 'mtime': '2020-03-12 22:43:35', 'namefornew': '22:30 第9话'}
{'isnew': False, 'id': '20200058', 'wd': 4, 'name': 'SHOW BY ROCK!! Mashumairesh!!', 'mtime': '2020-03-12 22:42:10', 'namefornew': '22:30 第10话'}
{'isnew': False, 'id': '20200028', 'wd': 4, 'name': '索玛丽与森林之神', 'mtime': '2020-03-12 23:08:18', 'namefornew': '23:00 第10话'}
{'isnew': False, 'id': '20200011', 'wd': 4, 'name': 'Infinite Dendrogram -无尽连锁-', 'mtime': '2020-03-12 23:11:49', 'namefornew': '23:00 第9话'}
{'isnew': False, 'id': '20190219', 'wd': 5, 'name': '非枪人生', 'mtime': '2019-12-27 02:20:09', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190025', 'wd': 5, 'name': '星合之空', 'mtime': '2019-12-27 15:17:04', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190311', 'wd': 5, 'name': '银河英雄传说 Die Neue These 星乱', 'mtime': '2019-12-13 20:08:15', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190125', 'wd': 5, 'name': '新石纪', 'mtime': '2019-12-13 22:32:28', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190216', 'wd': 5, 'name': '厨病激发BOY', 'mtime': '2019-12-13 23:15:34', 'namefornew': '第11话'}
{'isnew': False, 'id': '20190209', 'wd': 5, 'name': 'NULL & PETA', 'mtime': '2020-02-02 18:33:43', 'namefornew': '第13话(完结)'}
{'isnew': False, 'id': '20200009', 'wd': 5, 'name': '理科生坠入情网故尝试证明', 'mtime': '2020-01-10 23:31:19', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20200043', 'wd': 5, 'name': '宝石商人理查德的谜鉴定', 'mtime': '2020-03-13 00:48:13', 'namefornew': '00:30 第10话'}
{'isnew': False, 'id': '20200038', 'wd': 5, 'name': '家有圆圆？！～我家的圆圆你知道吗～', 'mtime': '2020-03-13 01:32:06', 'namefornew': '01:25 第10话'}
{'isnew': False, 'id': '20200026', 'wd': 5, 'name': '地缚少年花子君', 'mtime': '2020-03-13 15:23:16', 'namefornew': '15:00 第10话'}
{'isnew': False, 'id': '20200005', 'wd': 5, 'name': '神推登上武道馆我就死而无憾', 'mtime': '2020-03-13 15:36:24', 'namefornew': '15:30 第10话'}
{'isnew': False, 'id': '20190366', 'wd': 5, 'name': '恋爱小行星', 'mtime': '2020-03-13 23:07:01', 'namefornew': '23:00 第10话'}
{'isnew': False, 'id': '20190166', 'wd': 6, 'name': '食戟之灵 第四季', 'mtime': '2019-12-28 03:20:46', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190179', 'wd': 6, 'name': '碧蓝幻想 第二季', 'mtime': '2019-12-28 03:25:27', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190176', 'wd': 6, 'name': '炎炎消防队', 'mtime': '2019-12-28 03:37:50', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190200', 'wd': 6, 'name': '厨神小当家', 'mtime': '2019-12-28 03:42:13', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190182', 'wd': 6, 'name': '高分少女 第二季', 'mtime': '2019-12-21 03:03:26', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190226', 'wd': 6, 'name': '泰迦奥特曼', 'mtime': '2019-12-28 11:43:56', 'namefornew': '第26集(完结)'}
{'isnew': False, 'id': '20190213', 'wd': 6, 'name': '战×恋', 'mtime': '2019-12-21 22:50:37', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190069', 'wd': 6, 'name': '科学的超电磁炮T', 'mtime': '2020-02-29 00:09:02', 'namefornew': '本周停播 00:05 第7话'}
{'isnew': False, 'id': '20200024', 'wd': 6, 'name': '达尔文游戏', 'mtime': '2020-03-14 00:35:23', 'namefornew': '00:30 第10话'}
{'isnew': False, 'id': '20200025', 'wd': 6, 'name': '织田肉桂信长', 'mtime': '2020-03-14 01:24:35', 'namefornew': '01:23 第10话'}
{'isnew': False, 'id': '20200055', 'wd': 6, 'name': '排球少年 第四季', 'mtime': '2020-03-14 01:32:01', 'namefornew': '01:30 第10话'}
{'isnew': False, 'id': '20190199', 'wd': 6, 'name': '歌舞伎町夏洛克', 'mtime': '2020-03-14 02:38:24', 'namefornew': '02:10 第22话'}
{'isnew': False, 'id': '20200040', 'wd': 6, 'name': '请在T台上微笑', 'mtime': '2020-03-14 03:00:27', 'namefornew': '02:55 第9话'}
{'isnew': False, 'id': '20180062', 'wd': 6, 'name': '斗罗大陆', 'mtime': '2020-03-14 10:10:05', 'namefornew': '第95话'}
{'isnew': False, 'id': '20200113', 'wd': 6, 'name': '奥特英雄传 赛罗与捷德', 'mtime': '2020-03-14 10:22:33', 'namefornew': '第10集'}
{'isnew': False, 'id': '20190202', 'wd': 6, 'name': '入间同学入魔了', 'mtime': '2020-03-07 19:10:04', 'namefornew': '第23话(完结)'}
{'isnew': False, 'id': '20000005', 'wd': 6, 'name': '名侦探柯南', 'mtime': '2020-03-15 12:02:09', 'namefornew': '19:30 第1029集'}
{'isnew': False, 'id': '20190039', 'wd': 6, 'name': '暗黑破坏神在身边', 'mtime': '2020-03-14 20:03:58', 'namefornew': '20:00 第10话'}
{'isnew': False, 'id': '20190398', 'wd': 6, 'name': '镇魂街 第二季', 'mtime': '2020-01-18 20:09:42', 'namefornew': '第5话'}
{'isnew': False, 'id': '20200023', 'wd': 6, 'name': '22/7', 'mtime': '2020-03-14 23:35:42', 'namefornew': '23:30 第10话'}
{'isnew': False, 'id': '20190331', 'wd': 6, 'name': '偶像活动Parade', 'mtime': '2020-03-14 20:20:54', 'namefornew': '第23话'}
{'isnew': False, 'id': '20200035', 'wd': 6, 'name': '异种族风俗娘评鉴指南', 'mtime': '2020-01-11 23:56:37', 'namefornew': '第10话'}
{'isnew': False, 'id': '20190181', 'wd': 0, 'name': '刀剑神域 Alicization篇 War of Underworld', 'mtime': '2019-12-29 00:36:40', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190206', 'wd': 0, 'name': '我们真的学不来 第二季', 'mtime': '2019-12-29 01:03:26', 'namefornew': '第13话(完结)'}
{'isnew': False, 'id': '20190281', 'wd': 0, 'name': '一弦定音！ 第二季', 'mtime': '2019-12-29 01:35:10', 'namefornew': '第26话(完结)'}
{'isnew': False, 'id': '20190350', 'wd': 0, 'name': '奥特银河格斗：新世代英雄', 'mtime': '2019-12-22 10:33:24', 'namefornew': '第13集(完结)'}
{'isnew': False, 'id': '20190217', 'wd': 0, 'name': '警视厅 特务部 特殊凶恶犯对策室 第七课', 'mtime': '2019-12-29 21:59:56', 'namefornew': '第13话(完结)'}
{'isnew': False, 'id': '20190056', 'wd': 0, 'name': '偶像梦幻祭', 'mtime': '2019-12-22 22:10:34', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190201', 'wd': 0, 'name': '歌塑世界 -Songs Connection-', 'mtime': '2019-12-22 22:37:42', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190263', 'wd': 0, 'name': '美妙射击部', 'mtime': '2020-01-18 22:57:37', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190207', 'wd': 0, 'name': 'Fairy gone 第二季', 'mtime': '2019-12-28 23:20:38', 'namefornew': '第24话(完结)'}
{'isnew': False, 'id': '20190262', 'wd': 0, 'name': '天华百剑 ～欢迎来到铭治馆！～', 'mtime': '2019-12-31 05:29:52', 'namefornew': '第12话(完结)'}
{'isnew': False, 'id': '20190104', 'wd': 0, 'name': 'Star☆Twinkle光之美少女', 'mtime': '2020-01-26 12:11:13', 'namefornew': '第49话(完结)'}
{'isnew': False, 'id': '20190008', 'wd': 0, 'name': 'Fate/Grand Order 绝对魔兽战线 巴比伦尼亚', 'mtime': '2020-03-15 00:03:32', 'namefornew': '00:00 第20话'}
{'isnew': False, 'id': '20190031', 'wd': 0, 'name': '魔法纪录 魔法少女小圆外传', 'mtime': '2020-03-15 00:38:21', 'namefornew': '00:30 第11话'}
{'isnew': False, 'id': '20200010', 'wd': 0, 'name': '虚构推理', 'mtime': '2020-03-15 05:33:51', 'namefornew': '02:00 第10话'}
{'isnew': False, 'id': '20190276', 'wd': 0, 'name': '假面骑士01', 'mtime': '2020-03-15 10:07:33', 'namefornew': '第27集'}
{'isnew': False, 'id': '20190141', 'wd': 0, 'name': '闪亮美妙☆频道 第二季', 'mtime': '2020-03-15 12:15:31', 'namefornew': '第100话'}
{'isnew': False, 'id': '20200114', 'wd': 0, 'name': 'Healin Good 光之美少女', 'mtime': '2020-03-15 12:14:18', 'namefornew': '第7集'}
{'isnew': False, 'id': '20180097', 'wd': 0, 'name': '咯咯咯的鬼太郎 (2018)', 'mtime': '2020-03-15 12:24:16', 'namefornew': '第95话'}
{'isnew': False, 'id': '20000001', 'wd': 0, 'name': '海贼王', 'mtime': '2020-03-15 12:06:22', 'namefornew': '12:00 第924话'}
{'isnew': False, 'id': '20170172', 'wd': 0, 'name': '博人传 火影忍者新时代', 'mtime': '2020-03-15 17:27:52', 'namefornew': '17:30 第148话'}
{'isnew': False, 'id': '20200030', 'wd': 0, 'name': '异兽魔都', 'mtime': '2020-03-15 12:36:48', 'namefornew': '第10话'}
```
