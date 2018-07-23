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
Then do the segment. Save the result into `data/seg` <br>
Finally run the main program. Save the result into `data/topics` 

