from django.shortcuts import render
from WebTool.common.couchdb import CouchbaseManager
from WebTool.common.common import eDataBase

from collections import namedtuple
import json
from  WebTool.common.excel_util import excel_to_json,excel_to_json_new,find_all_excel_file


def NewServerTableVeiw(request):

    cbq = CouchbaseManager.instance()
    cServerInfo = cbq.get_select_server_info()

    lstxlsfile = find_all_excel_file('../NewTable')
    #print(lstxlsfile)
    return render(request, 'WebTool/NewServerTable.html',{"server_name": cServerInfo.name,"server_ip": cServerInfo.IP,"lxs_files":json.dumps(lstxlsfile)})