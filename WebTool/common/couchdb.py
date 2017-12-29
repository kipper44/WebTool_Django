from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from WebTool.common.Singleton import  SingletonInstance
from couchbase.n1ql import N1QLQuery

class CouchbaseManager(SingletonInstance) :
    def __init__(self):
        self.mapDbPool ={}
        self.selectKey =''

    def Add(self, name, ip, username, passwd, bucket):
        cluster = Cluster('couchbase://' + ip)
        authenticator = PasswordAuthenticator(username, passwd)
        cluster.authenticate(authenticator)
        cBucket = cluster.open_bucket(bucket)

        self.mapDbPool[name] = cBucket;
    def get(self):
        return self.mapDbPool[self.selectKey];
    def get_bucket(self,bucket_name):
        #print(self.mapDbPool)
        return self.mapDbPool[bucket_name]

    def select_db(self,strSelectKey):
        self.selectKey = strSelectKey;
        print(self.selectKey)

    def get_server_list(self):
        aa = self.mapDbPool[self.selectKey]
        query = N1QLQuery("select name,IP,Port,DB from GmTool_GM where strType ='server'")
        return aa.n1ql_query(query)
