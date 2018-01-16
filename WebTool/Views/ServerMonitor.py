from django.shortcuts import render
from WebTool.common.couchdb import CouchbaseManager
from WebTool.common.common import eDataBase

from collections import namedtuple
import json
from django.http import JsonResponse,HttpResponse

def ServerMonitorView(request):

    cbq = CouchbaseManager.instance()
    cServerInfo = cbq.get_select_server_info()

    return render(request, 'WebTool/ServerMonitor.html',{"server_name": cServerInfo.name,"server_ip": cServerInfo.IP})