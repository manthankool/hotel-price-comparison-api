# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import place
import requests
from flask_jwt import jwt_required,current_identity
from flask_restful import Resource
from flask_limiter import Limiter


from app import limiter

class Item(Resource):




    decorators = [limiter.limit( "7000/month;250/day")]
    @jwt_required()

    def get(self,city):
        user = current_identity
        kind = user.is_active
        if kind == True:
            url='https://www.tripadvisor.in/Search?q=delhi#&ssrc=a&o=30'
            resp=requests.get(url)
            respdata=resp.text



            soup=BeautifulSoup(respdata,'html.parser')



            all=soup.find_all("div",{"class":"result LODGING"})


            u=list()

            for item in all:
                l={}



                try:
                    l["Hotel"]=item.find("div",{"class":"title"}).text
                except:
                    l["Hotel"]=None


                j=item.find("div",{"class":"provName"})
                try:
                    l["Best-price"]=j.text
                except:
                    l["Best-price"]=None


                try:
                    l["vendor1"]=item.find_all("div",{"class":"no_cpu offer text-link "})[0].text.replace("₹"," -₹")

                except:
                    l["vendor1"]=None




                try:
                    l["vendor2"]=item.find_all("div",{"class":"no_cpu offer text-link "})[1].text.replace("₹"," -₹")

                except:
                    l["vendor2"]=None



                try:
                    l["vendor3"]=item.find_all("div",{"class":"no_cpu offer text-link "})[2].text.replace("₹"," -₹")

                except:
                    l["vendor3"]=None


                try:

                    r=item.find("div",{"class":"prw_rup prw_common_location_rating_simple"})
                    l["ratings"]='3.8'
                except:
                    l["ratings"]=None

                try:
                    l["no. of reviews"]=item.find("span",{"class":"review-count"}).text
                except:
                    l["no. of reviews"]=None







                u.append(l)


            return{'comparison':u}
        return {"message":"you are a free user"}
