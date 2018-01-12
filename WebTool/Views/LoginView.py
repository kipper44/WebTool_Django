from django.shortcuts import render
from WebTool.common.couchdb import CouchbaseManager
from types import SimpleNamespace as Namespace
import json
from django.http import JsonResponse,HttpResponse
from WebTool.common.common import eDataBase
#from django.contrib.auth.models import User
#from django.contrib.auth import login


def InitCouchBase( ):
    cbq = CouchbaseManager.instance()
    cbq.Add(eDataBase.GM_Tool, "GM_GmTool_GM", "10.80.40.71", "gmtool", "exgames1030**", "GmTool_GM")
    cbq.Add(eDataBase.GM_Event,"GM_eventdb_GM", "10.80.40.71", "gmtool", "exgames1030**", "eventdb_GM")
    cbq.Add(eDataBase.GM_Trace,"GM_gm_trace_GM", "10.80.40.71", "gmtool", "exgames1030**", "gm_trace_GM")



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
            bReturn = True
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

    return render(request, 'WebTool/LoginMain.html')