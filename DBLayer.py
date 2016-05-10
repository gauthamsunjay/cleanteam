import pymongo

from DBConfig import *

def write_co_ords(docs) :
    return insert_docs(CO_ORDS_DB, CO_ORDS_COLL, docs)
    
def read_co_ords() :
    return get_docs(CO_ORDS_DB, CO_ORDS_COLL, docs)

def write_locs(docs) :
    return insert_docs(LOCS_DB, LOCS_COLL, docs)

def read_locs() :
    return get_docs(LOCS_DB, LOCS_COLL, docs)
    
def write_clusters(docs) :
    return insert_docs(CLUSTERS_DB, CLUSTERS_COLL, docs)

def read_clusters() :
    return get_docs(CLUSTERS_DB, CLUSTERS_COLL, docs)

def write_initial_route(docs) :
    return insert_docs(INITIAL_ROUTE_DB, INITAL_ROUTE_COLL, docs)

def read_initial_route() :
    return get_docs(INITIAL_ROUTE_DB, INITAL_ROUTE_COLL, docs)

def write_final_route(docs) :
    return insert_docs(FINAL_ROUTE_DB, FINAL_ROUTE_COLL, docs)

def read_final_route() :
    return get_docs(FINAL_ROUTE_DB, FINAL_ROUTE_COLL, docs)


"""
    Generic Fns To Interact With Mongo
"""
def insert_doc(db_, coll_, doc_) :
    client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[str(db_)]
    coll = db[str(coll_)]
    res = coll.insert_one(doc_)
    client.close()
    return res

def insert_docs(db_, coll_, docs_) :
    client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[str(db_)]
    coll = db[str(coll_)]
    res = coll.insert_many(docs_)
    client.close()
    return res

def get_docs(db_, coll_) :
    client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[str(db_)]
    coll = db[str(coll_)]
    res = list(coll.find())
    client.close()
    return res

def remove_docs(db_, coll_) :
    client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[str(db_)]
    coll = db[str(coll_)]
    res = coll.remove({})
    client.close()
    return res
