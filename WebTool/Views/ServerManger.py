from django.shortcuts import render
from WebTool_Django import settings
from WebTool.common.couchdb import CouchbaseManager
from WebTool.common.common import eDataBase
from django.http import JsonResponse,HttpResponse,FileResponse,Http404
import os
import json
from  WebTool.common.excel_util import excel_to_json,excel_to_json_new,find_all_excel_file


def handle_uploaded_file(path,f,name):
    if not os.path.exists(path):
        os.mkdir(path)

    destination = open(path+f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    #fs = FileSystemStorage()
    #filename = fs.save(f.name, f)

def UploadFile(request):
    for key in request.FILES:
        file = request.FILES[key]
        handle_uploaded_file(settings.BASE_DIR +'/NewTable/',file,file.name)
    return JsonResponse({'Message': "Success"}, safe=False)

def FileDownload(request):
    file_path = os.path.join(settings.BASE_DIR +'/NewTable/',request.path.split('/')[2])
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def NewServerTableVeiw(request):

    cbq = CouchbaseManager.instance()
    cServerInfo = cbq.get_select_server_info()

    lstxlsfile = find_all_excel_file('./NewTable')
    #print(lstxlsfile)
    return render(request, 'WebTool/NewServerTable.html',{"server_name": cServerInfo.name,"server_ip": cServerInfo.IP,"lxs_files":json.dumps(lstxlsfile)})