import json
from elasticsearch import Elasticsearch
es = Elasticsearch()

def es_insert(index,doc_type,body,refresh=True):
	res = es.index(index=index, doc_type=doc_type, body=body)
	if refresh==True:
		es.indices.refresh(index=index)
	if "_id" in res:
		return res["_id"]
	else:
		return False

def es_delete(index,doc_type,doc_id,refresh=True):
	res = es.delete(index=index, doc_type=doc_type, id=doc_id)
	if refresh==True:
		es.indices.refresh(index=index)

def es_update(index,doc_type,doc_id,body,refresh=False):
	es.update(index=index,doc_type=doc_type,id=doc_id,body=body)
	if refresh==True:
		es.indices.refresh(index=index)
		
def es_search(db_query,filter_source=False,size=1000):
	res = es.search(body=db_query,size=size)
	if filter_source==False:
		return res['hits']
	else:
		return getSource(res['hits'])


def getSource(res):
	ans = []
	if res["total"]>0:
		res = res["hits"]
		for item in res:
			ans.append(item["_source"])
	return ans


def show(res):
	print(json.dumps(res, indent=2, sort_keys=True))
