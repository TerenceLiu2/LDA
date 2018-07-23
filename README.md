# LDA
Using LDA model to get topics
# MainCode
- MyLDA.py <br>
Main Code
- Tools.py <br>
 Some Tools
# Operation Environment
- jieba
- lda
- numpy
- MySQLdb
# Data Structure

SQL <br>

 movie_id|com_id|content|
:--:|:--:|:--:
1|1|Good

data/Movie.csv <br>
323,战狼2,2017,343,2017-7-27
.........

# Opration Instruction
Prepare some datas, then run
```python MyLDA.py```

# Sample
Save Comments from Database. The dir is `data/comments` <br>
```
奇门遁甲，我觉得这个演技也是没谁了的。
《奇门遁甲》比我预期要好很多，特效真的太棒了，目前可以说是中国电影里特效的极致了吧。每个角色也都是紧密联系相互依存的，贯穿主线的是周冬雨饰演的小圆圈，特别有笑料，没想到最后还能为这个承担最多笑点的人物而哭，感染力很强。
```
Then do the segment. Save the result into `data/seg` <br>
```
奇门遁甲 觉得 演技 没谁了 
奇门遁甲 预期 特效 太棒了 目前 中国 电影 特效 角色 紧密联系 相互依存
```
Finally run the main program. Save the result into `data/topics` 
```
0: 冬雨 大鹏 演技 倪妮 感觉 演员 喜欢 角色 尴尬
1: 特效 电影 反派 游戏 感觉 前面 问题 部分 视效
2: 特效 动作 徐克 袁和平 导演 设计 没有 剧情 八爷
3: 掌门 小圆 有点 特效 最后 故事 还行 武侠 五大
4: 特效 冬雨 剧情 电影 倪妮 没有 片子 烂片 口型
5: 电影 超级 造型 英雄 奇门遁甲 中国 题材 妖怪 表演
6: 电影 喜欢 好看 徐克 觉得 没有 袁和平 期待 导演
7: 徐克 徐老怪 故事 武侠 妖怪 期待 外星人 喜欢 蜀山
8: 西游 特效 徐克 片子 伏妖 倪妮 降魔 观众 不要
9: 特效 故事 没有 演员 剧情 想象力 港片 好看 片子
10: 电影 武侠 徐克 奇幻 中国 奇门遁甲 袁和平 世界 大片
11: 没有 特效 剧情 有点 感觉 主角 中国 怪兽 奇门遁甲
```

