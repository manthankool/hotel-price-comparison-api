# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import place
import requests
from flask_jwt import jwt_required
from flask_restful import Resource


class Item(Resource):

    @jwt_required()
    def get(self,city):

        url=place.search(city)
        resp=requests.get(url)
        respdata=resp.text



        soup=BeautifulSoup(respdata,'html.parser')



        all=soup.find_all("div",{"class":"prw_rup prw_meta_hsx_responsive_listing bottom-sep"})


        u=list()

        for item in all:
            l={}



            try:
                l["Hotel"]=item.find("a",{"class":"property_title prominent"}).text
            except:
                l["Hotel"]=None


            j=item.find("div",{"class":"price-wrap"})
            try:
                l["Best-price"]=j.text.replace("₹"," -₹")
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
                r=item.find("div",{"class":"prw_rup prw_common_responsive_rating_and_review_count linespace is-shown-at-mobile"})
                r=str(r.find("span"))
                l["ratings"]=(r[11:19]).replace("b","")+" - Rating"
            except:
                l["ratings"]=None

            try:
                l["no. of reviews"]=item.find("a",{"class":"review_count"}).text
            except:
                l["no. of reviews"]=None







            u.append(l)


        return{'comparison':u}
