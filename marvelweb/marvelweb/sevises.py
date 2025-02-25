import pymysql
from pymongo import MongoClient



class MarvelFilmOperations:
    def allmarvelmoviesinsequence(self):
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("select * from movie_sequence")
        data=curs.fetchall()
        print(data)
        con.close()
        return data

    def addsuperhero(self,hero_name,real_name,title,origin_story,species,superpowers,weakness,gadgets,team,description):
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("insert into superheroes (hero_name,real_name,title,origin_story,species,superpowers,weakness,gadgets,team,description) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(hero_name,real_name,title,origin_story,species,superpowers,weakness,gadgets,team,description))
        con.commit()
        con.close()
        return "super hero add susscesfully"

    def displaysuperhero(self,hero_name):
         con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
         curs=con.cursor()
         curs.execute("SELECT * FROM superheroes WHERE hero_name = %s", (hero_name,))
         data=curs.fetchone()
         print(data)
         con.close()
         if data:
             superhero = {
            "id": data[0],
            "name": data[1],
            "real_name": data[2],
            "title": data[3],
            "origin": data[4],
            "species": data[5],
            "powers": data[6],
            "weakness": data[7],
            "gadgets": data[8],
            "team": data[9],
            "description": data[10],
            "image_url": data[11]
        }
             return superhero
         else:
            return None
    

    def submitfanstory(self,title,author,content):
         con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
         curs=con.cursor()
         curs.execute("insert into fan_stories (title,author,content) values ('%s','%s','%s')"%(title,author,content))
         con.commit()
         con.close()
         return "fan story addes succsesfully"

    def downlodmovietourl(self,name):
        try:
            
            client=MongoClient("mongodb+srv://rahuldb:rahul123@rahulcluster.vviud.mongodb.net/?retryWrites=true&w=majority&appName=rahulcluster")
            db=client["marvel_projectdb"]
            coll=db["allmovies"]
            data = coll.find_one({"name": name}) 
            print(data)
            return data

        except :
          return {"error"}

    def upcomeingmarvelmovies(self):
        con=pymysql.connect(host='mysql-python-rahul-python.c.aivencloud.com',port=20349,user='avnadmin',password='AVNS_0IC9WqSB0H-_cdAII8e',database='marvel_project')
        curs=con.cursor()
        curs.execute("select * from  Upcoming_Marvel_Movies")
        data=curs.fetchall()
        print(data)
        con.close()
        return data