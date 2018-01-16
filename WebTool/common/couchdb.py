from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from WebTool.common.Singleton import  SingletonInstance
from couchbase.n1ql import N1QLQuery
from WebTool.common.common import eDataBase

class CouchbaseManager(SingletonInstance) :

    def clear(self):
        self.mapDbPool ={}
        self.selectKey =1
        self.mapServerInfo = {}
        self.selectServer=""
        self.strLoginUser =""

    def __init__(self):
        self.mapDbPool ={}
        self.selectKey =1
        self.mapServerInfo = {}
        self.selectServer=""
        self.strLoginUser =""
    def __str__(self):
        return self.mapDbPool.__str__()
    def Get_DBPool_Size(self):
        return len(self.mapDbPool)

    def AddServerInfo(self,name,objInfo):
        self.mapServerInfo[name] = objInfo;

    def SetLoginUser(self,strUserName):
        self.strLoginUser =strUserName

    def SelectServer(self,servername):
        cSelectServer = self.mapServerInfo[servername]
        Index = eDataBase.GAME_EVENT;
        for bucket in cSelectServer.DB:
            ip = bucket.uri[7:]
            ip = ip[:-11]
            self.Add(Index,bucket.bucket,ip,bucket.User,bucket.bucketPassword,bucket.bucket)
            Index += 1
        self.selectServer = servername

    def Add(self,idx, name, ip, username, passwd, bucket):
        cluster = Cluster('couchbase://' + ip)
        authenticator = PasswordAuthenticator(username, passwd)
        cluster.authenticate(authenticator)
        cBucket = cluster.open_bucket(bucket)
        self.mapDbPool[idx] = cBucket;

    def get(self):
        return self.mapDbPool[self.selectKey];

    def get_bucket(self,bucket_idx):
        #print(self.mapDbPool)
        return self.mapDbPool[bucket_idx]

    def select_db(self,iSelectKey):
        self.selectKey = iSelectKey;

    def get_server_list(self):
        cBucket = self.mapDbPool[self.selectKey]
        query = N1QLQuery("select name,IP,Port,DB from GmTool_GM where strType ='server'")
        return cBucket.n1ql_query(query)

    def RunQuery(self,strQuery):
        #print(self.selectKey)
        print(self.mapDbPool)
        cSelectPool = self.mapDbPool[self.selectKey]
        #print(cSelectPool)
        query = N1QLQuery(strQuery)
        return cSelectPool.n1ql_query(query)

    def get_select_server_name(self):
        return self.selectServer

    def get_select_server_info(self):
        return self.mapServerInfo[self.selectServer]