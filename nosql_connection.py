from pymongo import MongoClient
import redis

MONGODB_HOST = "106.14.107.75"
MONGODB_PORT = 27017
MONGODB_DATABASE = "mymongo"
REDIS_HOST = "106.14.107.75"
REDIS_PORT = 6379
REDIS_AUTH = "123456"


# mongodb            获取指定集合对象
def mongodbConnection(collectionName):
    myclient = MongoClient(MONGODB_HOST, MONGODB_PORT)
    mydb = myclient[MONGODB_DATABASE]
    collection = mydb[collectionName]
    return collection


# redis              获取指定数据库(0~15)连接对象
def redisConnection(databaseNum):
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_AUTH, db=databaseNum,
                                decode_responses=True)
    mycon = redis.Redis(connection_pool=pool)
    return mycon
