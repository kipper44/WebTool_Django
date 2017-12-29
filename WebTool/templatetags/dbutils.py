from django.utils.safestring import mark_safe
from django import template

from WebTool.common.couchdb import CouchbaseManager
import json

register = template.Library()


@register.simple_tag()
def get_tree_menu():
    cbq = CouchbaseManager.instance()
    cbq.select_db('GM_GmTool_GM')
    cMenu = cbq.get().get("ToolMenu")
    msg = str(cMenu.value)
    idx = msg.find(":")
    if ( idx != -1 ):
        msg = msg[idx+1:]
        msg = msg[:-1]
    return json.dumps(msg,ensure_ascii=False)