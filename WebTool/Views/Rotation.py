from django.shortcuts import render
from WebTool.common.couchdb import CouchbaseManager
from WebTool.common.common import eDataBase

from collections import namedtuple
import json
from django.http import JsonResponse,HttpResponse

def SaveRotationData(request):
    data = request.POST.get('table')
    cRotationTable = json.loads(data)
    cbq = CouchbaseManager.instance()
    cbq.select_db(eDataBase.GAME_EVENT)
    cbq.get().upsert("RotationTable_Python",cRotationTable)
    return JsonResponse({'Result': "true"}, safe=False)

def PostProcess(request):
    iType = request.POST.get('call_type')
    if iType == '0' :
        return SaveRotationData(request)

    return JsonResponse({'Result': "true"}, safe=False)
def RotationView(request):
    if request.method =='POST' :
        return PostProcess(request)
    return render(request, 'WebTool/Rotation.html')
