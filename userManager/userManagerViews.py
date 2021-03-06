from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import requests
import json
import simplejson
from elasticsearch import Elasticsearch
import os
import shutil
from elasticsearchservice import traverse
from djangodemo import settings


# 参数传递方法封装
from elasticsearch.helpers import bulk

userMapData = []

def index(request):
# 参数进入
    payload = {   "query": {
    "bool": {


        "must": [
             { "match_phrase": { "事故隐患内容": "古马66千伏" }}
        ]
    }
  }
}
#为什么使用post请求的方式才能成功？因为post请求可以传输json值
    headers ={'content-type': 'application/json'}
    url = settings.REQUEST_ES_RUL
    # ret = requests.post("http://127.0.0.1:9200/lishikai_index007/_search",data=json.dumps(payload),headers=headers)
    ret = requests.post(url,data=json.dumps(payload),headers=headers)
    print('----------------')
    print(ret.text)
    print('----------------')
    # reqparam = request.body.decode('utf-8')  json解析完成
    reqparam =simplejson.loads(request.body.decode('utf-8'))
    print(reqparam['query']['match']['发现人'])  #请求解析成功实现-------下一步进行前端后台整个流程的书写
    return HttpResponse(ret.text)

# 修改----只提供对于规章制度、 python包操作elasticsearch
def CRUDParamMethod(request):
    print(request)
    ipPort = settings.REQUEST_ES_IP_PORT
    obj = Elasticsearch(ipPort)
    # # 創建索引index:索引的名字,body:數據,ignore:狀態碼
    # result = obj.indices.create(index="users", body={"username": "李仕凯", "password": "123"}, ignore=400)
    # result = obj.indices.delete(index='users', ignore = [400, 404])
    # data = {"username": "李仕凯", "password": "123"}
    # data2 = {"username": "李人", "password": "123"}
    # # result = obj.create(index="users", doc_type="doc_", id=1, body=data)
    # # 创建用户user索引
    # result = obj.index(index='users', doc_type='_doc', body=data)
    # result = obj.index(index='users', doc_type='_doc', body=data2)
    # 检索数据
    dsl = {
        'query': {
            'match_phrase': {
                'username': '李仕凯'
            }
        }
    }

    result = obj.search(index='users', body=dsl)
    print(result)
    # 修改用户信息--例如密码  --传入id
    data = {
        'username': '美国留给伊拉克的是个烂摊子吗',
        'password': '123',
    }
    data1 = {'_index': 'users',
            '_id': 'xaJSHG8B0WQk4EfReCWF',
            '_source': data,        # 实现更新操作-------更新用户名或者密码
            '_op_type': 'index'}
    result = bulk(obj, actions=[data1])
    # bulk()
    # 删除操作---完成
    result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
    # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
    print(result)
    return '你好世界！！';


# 用户新增创建一个关于用户单独的索引，维护对于用户的增删改查等操作  根据什么唯一确定一个用户。用户名和啥



def requestUserAdd(request):
    data = request.body
    userMapData.append(data)
    print(userMapData)

def requestUserDelete(request):
    data = request.body
    userMapData.append(data)
    print(userMapData)
def requestUserUpdate(request):
    data = request.body
    userMapData.append(data)
    print(userMapData)
def requestUserAll(request):

    print(userMapData)
    return HttpResponse(userMapData)

if __name__ == '__main__':
    # CRUDParamMethod(1)
    # sent_json_to_elasticsearch()
    print(os.path.abspath(os.curdir))
    print(os.path.dirname(__file__))
    print(settings.BASE_DIR)
    print(settings.XMLFILES_FOLDER)
    uploadDir = os.path.join(settings.BASE_DIR, '../upload')
    if os.path.exists(uploadDir):
        shutil.rmtree(os.path.join(settings.BASE_DIR, '../upload'))
    else:
        os.mkdir(uploadDir)
    processToTogstashDirTest = os.path.join(settings.BASE_DIR, '../processtologstash')
    data_end_txt = processToTogstashDirTest + '/data-end.txt'
    # file = open("C:\\Users\\22934\\PycharmProjects\\djangodemo\\processtologstash\\data-end.txt")
    print(os.path.isfile(data_end_txt))
