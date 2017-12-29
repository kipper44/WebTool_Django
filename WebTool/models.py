from django.db import models


class ToolUsers( models.Model ):
    userid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    iAssert = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)

#class GmAuthority(models.Model):
#    iAuthority =models.IntegerField()
#    name = models.CharField(max_length=100)