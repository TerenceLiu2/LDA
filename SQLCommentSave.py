#coding=utf-8
import MySQLdb

def SaveComments(cbo_id):
    connO=MySQLdb.connect(host="192.168.235.55",user="root",passwd="iiip",db="Seeing_future",charset="utf8")
    curO=connO.cursor()
    curO.execute("select content from douban_comment where movie_id=%s;"%cbo_id)
    comments=curO.fetchall()
    for comment in comments:
        with open("data/comment/"+str(cbo_id),"a") as wf:
            wf.write(comment[0].encode("utf-8")+"\n")
