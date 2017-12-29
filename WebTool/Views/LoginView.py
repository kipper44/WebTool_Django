from django.shortcuts import render
from WebTool.common.couchdb import CouchbaseManager
from types import SimpleNamespace as Namespace
import json
from django.http import JsonResponse,HttpResponse

#from django.contrib.auth.models import User
#from django.contrib.auth import login


def InitCouchBase( ):
    cbq = CouchbaseManager.instance()
    cbq.Add("GM_GmTool_GM", "10.80.40.71", "gmtool", "exgames1030**", "GmTool_GM")
    cbq.Add("GM_eventdb_GM", "10.80.40.71", "gmtool", "exgames1030**", "eventdb_GM")
    cbq.Add("GM_gm_trace_GM", "10.80.40.71", "gmtool", "exgames1030**", "gm_trace_GM")


def LoginProcess(request):
    cbq = CouchbaseManager.instance()
    cBucket = cbq.get_bucket('GM_GmTool_GM')
    userid = request.POST.get('id')
    userpasswd = request.POST.get('userpass')
    bReturn = False

    try:
        ret = cBucket.get(userid).value
        cUser = json.loads(ret, encoding="utf-8", object_hook=lambda d: Namespace(**d))
        if cUser.passwd == userpasswd:
            #print(cUser)
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

    cbq.select_db('GM_GmTool_GM')
    list = []
    cresult = cbq.get_server_list()
    for row in cresult:
        strjson = str(row)
        cMessage = json.JSONEncoder().encode(row)
        objServer = json.loads(cMessage, object_hook=lambda d: Namespace(**d))
        list.append(objServer.name)

    return render(request,'WebTool/Index.html',{'server_list':json.dumps(list)})

def LoginMain(request):
    return render(request, 'WebTool/LoginMain.html')