from django.shortcuts import render
from WebTool.common.couchdb import CouchbaseManager
from WebTool.common.common import eDataBase

from collections import namedtuple
import json
from django.http import JsonResponse,HttpResponse

def SaveModeData(request):
    data = request.POST.get('table')
    cModeTable = json.loads(data)
    cbq = CouchbaseManager.instance()
    cbq.select_db(eDataBase.GAME_EVENT)
    cbq.get().upsert("ModeTable_Python",cModeTable)
    return JsonResponse({'Result': "true"}, safe=False)

def PostProcess(request):
    iType = request.POST.get('call_type')
    if iType == '0' :
        return SaveModeData(request)

    return JsonResponse({'Result': "true"}, safe=False)

def ModeView(request):
    if request.method =='POST' :
        return PostProcess(request)

    cbq = CouchbaseManager.instance()
    cServerInfo = cbq.get_select_server_info()

    return render(request, 'WebTool/GameMode.html',{"server_name": cServerInfo.name,"server_ip": cServerInfo.IP})