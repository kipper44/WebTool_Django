from django.utils.safestring import mark_safe
from django import template

from WebTool.common.couchdb import CouchbaseManager
import json
from WebTool.common.common import eDataBase
register = template.Library()


@register.simple_tag()
def get_tree_menu():
    cbq = CouchbaseManager.instance()
    cbq.select_db(eDataBase.GM_Tool)
    cMenu = cbq.get().get("ToolMenu_Python")
    msg = str(cMenu.value)
    idx = msg.find(":")
    if ( idx != -1 ):
        msg = msg[idx+1:]
        msg = msg[:-1]
    return json.dumps(msg,ensure_ascii=False)

@register.simple_tag()
def GetModeTable():
    cbq = CouchbaseManager.instance()

    cbq.select_db(eDataBase.GAME_EVENT)
    cResult = cbq.RunQuery("select  mode  from eventdb_dev where   strType = 'Mode'")
    for row in cResult:

        #strJson = str(row)[9:]
        #strJson =strJson[:-1]
        strJson = str(row).replace("'","\"")
        strJson = strJson.replace("True", "\"True\"")
        print(strJson )

        cModeTable = json.loads(strJson)
        print(cModeTable)
        #list_values = [v for v in cModeTable.values()]
        return json.dumps(cModeTable, ensure_ascii=False)