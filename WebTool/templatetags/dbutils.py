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
    cModeTable = cbq.get().get("ModeTable_Python").value
    #cResult = cbq.RunQuery("select  mode  from eventdb_dev where   strType = 'Mode'")
    #for row in cResult:
       #strJson = str(row)[9:]
       #strJson =strJson[:-1]
    #   strJson = str(row).replace("'","\"")
    #   strJson = strJson.replace("True", "\"True\"")
    #   print(strJson )

    #    cModeTable = json.loads(strJson)
    #    print(cModeTable)
    #    #list_values = [v for v in cModeTable.values()]
    return json.dumps(cModeTable, ensure_ascii=False)


def InitRotationTable():
    strJson = '{\"strType\": \"Rotation\",\"vecRotations\": [  { \"iIndex\": 1,\"strStartDate\": \"2018-01-01 00:00:00\",\"strEndDate\": \"2018-01-31 23:59:59\",\"iTargetIndex_1\": -1,\"iTargetIndex_2\": -1,\"iTargetIndex_3\": -1,\"iTargetIndex_4\": -1,\"iTargetIndex_5\": -1  } ]}'
    return strJson

@register.simple_tag()
def GetRotationTable():
    cbq = CouchbaseManager.instance()
    try:
        cbq.select_db(eDataBase.GAME_EVENT)
        cRotationTable = cbq.get().get("RotationTable_Python").value
        return json.dumps(cRotationTable, ensure_ascii=False)
    except Exception as e :
        return InitRotationTable()


@register.simple_tag()
def GetRotationMerTable():
    cbq = CouchbaseManager.instance()
    cbq.select_db(eDataBase.GAME_EVENT)
    try:
        cMerTable = cbq.get().get("CharacterTable").value
        cSkinTable = cbq.get().get("SkinTable").value

        objServer = json.loads(cMerTable)
        objSkin = json.loads(cSkinTable)
        lstFilter = []
        for key in objSkin["m_mapTableData"]:
            if objSkin["m_mapTableData"][key]["m_iDefaultSkin"] != 1:
                icode = objSkin["m_mapTableData"][key]["m_iSkinCharacterCode"]
                lstFilter.append(icode)
        #print(lstFilter)

        strJson = "[{\"Value\": -1,\"Text\" :\"None\"},"
        for key in objServer["m_mapTableData"]:
            iMercenary = objServer["m_mapTableData"][key]["m_iCode"]
            try:
                i = lstFilter.index(iMercenary)
                if 0 < i:
                    continue
            except Exception as e:
                pass
            strJson += "{"
            strJson += "\"Value\":" + str(objServer["m_mapTableData"][key]["m_iCode"]) + ","
            strJson += "\"Text\" :\"" + str(objServer["m_mapTableData"][key]["m_strCharacterName"]) + "\"},"

        strJson = strJson[:-1]
        strJson += "]"
        print(strJson)
    except Exception as e:
        print("error : " + str(e))
    else:
        pass
    return strJson