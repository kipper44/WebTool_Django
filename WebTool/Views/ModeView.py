from django.shortcuts import render
from WebTool.common.couchdb import CouchbaseManager
from WebTool.common.common import eDataBase

from collections import namedtuple
import json
from django.http import JsonResponse,HttpResponse


def ModeView(request):

    return render(request, 'WebTool/GameMode.html')