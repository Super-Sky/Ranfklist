from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from users.models import *
import os
import pandas as pd
from sqlalchemy import create_engine


USERPORT = "sqlite:///"+os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3')



def means_from_db(sql, schema_name):
    cnx = create_engine(schema_name)
    try:
        cnx.execute(sql)
        df = "success"
    except:
        df = "fail"
    return df

def package_from_db(sql, schema_name):
    cnx = create_engine(schema_name, encoding="utf-8", echo=False)
    df = pd.read_sql(sql, con=cnx)
    return df

# Create your views here.
def fractionupload(request):
    post=request.POST
    tempclientID = post.get("name")
    tempfraction = post.get("fraction")
    uodatasqlstr = "UPDATE users_userprofile SET fraction = {tempfraction} WHERE name = {tempclientID}".format(tempfraction=tempfraction,tempclientID=tempclientID)
    result = means_from_db(uodatasqlstr,USERPORT)
    return JsonResponse({'message':result})

def fractionquery(request):
    post=request.POST
    tempclientID = post.get("name")
    try:
        startname = post.get("startname")
    except:
        startname = 0
    try:
        stopname = post.get("stopname")
    except:
        stopname = 10
    if startname == None:
        startname = 0
    if stopname == None:
        stopname = 10
    selectsqlstr = "SELECT (SELECT COUNT(fraction) FROM users_userprofile WHERE s.fraction <= fraction) AS Rank, s.name, s.fraction AS fraction FROM users_userprofile s ORDER BY s.fraction DESC"
    resultall = package_from_db(selectsqlstr,USERPORT)
    resulttemp = resultall[startname:stopname]
    selectmysqlstr = "select * from (SELECT (SELECT COUNT(fraction) FROM users_userprofile WHERE s.fraction <= fraction) AS Rank, s.name, s.fraction AS fraction FROM users_userprofile s ORDER BY s.fraction DESC) where name = {tempclientID}".format(tempclientID=tempclientID)
    resultmy = package_from_db(selectmysqlstr,USERPORT)
    result = resulttemp.append(resultmy)
    result = result.reset_index(drop=True)
    resultdict = result.to_dict()
    return JsonResponse(resultdict)

