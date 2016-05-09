import pymongo
MONGO_HOST = "localhost"
MONGO_PORT = 27017

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
    
