from django.shortcuts import render,redirect
from WebTool.common.couchdb import CouchbaseManager
from types import SimpleNamespace as Namespace
import json
from django.http import JsonResponse,HttpResponseRedirect
from WebTool.common.common import eDataBase
#import os

#from django.contrib.auth.models import User
#from django.contrib.auth import login


def InitCouchBase( ):
    json_data = open('./WebTool/Config.json').read()
    data = json.loads(json_data)
    #print(data)

    #print(data["Config"][0])
    cbq = CouchbaseManager.instance()
    cbq.Add(data["Config"][0]["index"], data["Config"][0]["name"], data["Config"][0]["ip"], data["Config"][0]["user"], data["Config"][0]["pass"], data["Config"][0]["name"])
    cbq.Add(data["Config"][1]["index"], data["Config"][1]["name"], data["Config"][1]["ip"], data["Config"][1]["user"], data["Config"][1]["pass"], data["Config"][1]["name"])
    cbq.Add(data["Config"][2]["index"], data["Config"][2]["name"], data["Config"][2]["ip"], data["Config"][2]["user"], data["Config"][2]["pass"], data["Config"][2]["name"])

    #dir = os.getcwd()
    #print(dir)


def LoginProcess(request):

    cbq = CouchbaseManager.instance()
    cBucket = cbq.get_bucket(eDataBase.GM_Tool)
    userid = request.POST.get('id')
    userpasswd = request.POST.get('userpass')
    strServer = request.POST.get('Select_Server')
    bReturn = False

    try:
        ret = cBucket.get(userid).value
        cUser = json.loads(ret, encoding="utf-8", object_hook=lambda d: Namespace(**d))
        if cUser.passwd == userpasswd:
            cbq.SelectServer(strServer)
            cbq.SetLoginUser(userid)
            bReturn = True
            #request.COOKIES["LoginUser"] = userid
            request.session['LoginUser'] = userid
        else: pass
    except Exception as e:
        print(str(e))
    else:
        pass
    return JsonResponse({'Result':bReturn}, safe=False)

def Index(request):

    InitCouchBase()

    if request.method =='POST' :
        return LoginProcess(request)

    #login_user = request.COOKIES.get('LoginUser', 'None')
    login_user = request.session.get('LoginUser', 'None')
    if 'None' != login_user :
        return LoginMain(request)

    cbq = CouchbaseManager.instance()

    cbq.select_db(eDataBase.GM_Tool)
    list = []
    cresult = cbq.get_server_list()
    for row in cresult:
        strjson = str(row)
        cMessage = json.JSONEncoder().encode(row)
        objServer = json.loads(cMessage, object_hook=lambda d: Namespace(**d))
        list.append(objServer.name)
        cbq.AddServerInfo(objServer.name, objServer)

    return render(request,'WebTool/Index.html',{'server_list':json.dumps(list)})

def LoginMain(request):
    cbq = CouchbaseManager.instance()
    cServerInfo = cbq.get_select_server_info()

    return render(request, 'WebTool/LoginMain.html',{"server_name": cServerInfo.name,"server_ip": cServerInfo.IP})