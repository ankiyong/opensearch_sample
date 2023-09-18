from opensearchpy import OpenSearch
import json
from pprint import pprint

class get_info:
    def __init__(self,host: str,port: str,username: str,password: str):
        self.host: str = host
        self.port: str = port
        self.username: str = username
        self.password: str=password
    
    def get_client(self) -> OpenSearch:
        conn = OpenSearch(
                hosts=[{'host':self.host,'port':self.port}],
                http_auth=(self.username,self.password),
                use_ssl=True,
                verify_certs=False
        )
        return conn
    
    def get_indices(self):
        conn = self.get_client()
        res = conn.cat.indices(s="index",format='json')
        
        indices_info = []
        for result in res:
            data = {
                "health" : result["health"],
                "status" : result["status"],
                "index" : result["index"],
                "pri" : result["pri"],
                "rep" : result["rep"],
                "docs.count" : result["docs.count"],
                "store.size" : result["store.size"]
            }
            indices_info.append(data)
        return indices_info

    def get_idx_info(self,index: str):
        conn = self.get_client()
        idx_info = conn.indices.get(index=index)[index]
        mappings = idx_info["mappings"]
        settings = idx_info["settings"]
        info = {"mappings" : mappings,"settings":settings}
        return info
    
    def search_idx(self,index: str,q: str=None,size: int=1):
        conn = self.get_client()
        search_res = conn.search(index=index,q=q,size=size)["hits"]["hits"][0]["_source"]
        return search_res

if __name__ == "__main__":    
    get_info: get_info = get_info('172.30.1.22','9200','admin','admin')
    # indices_date = get_info.get_indices()    
    index_info = get_info.search_idx("security-auditlog-2023.09.17")
    # pprint(indices_date)
    pprint(index_info)