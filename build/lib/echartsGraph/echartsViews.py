from array import array

from django.shortcuts import render

# Create your views here.
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

def statisticForEcharts(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
            "size" : 0,
            "aggs" : {
                "popular_colors" : {
                    "terms" : {
                      "field" : "专业分类.keyword"
                    }
                }
            }
        }

    result = obj.search(index='lishikai_index000', body=dsl)
    # print(result)
    # 修改用户信息--例如密码  --传入id
    # data = {
    #     'username': '美国留给伊拉克的是个烂摊子吗',
    #     'password': '123',
    # }
    # data1 = {'_index': 'users',
    #         '_id': 'xaJSHG8B0WQk4EfReCWF',
    #         '_source': data,        # 实现更新操作-------更新用户名或者密码
    #         '_op_type': 'index'}
    # result = bulk(obj, actions=[data1])
    # # bulk()
    # # 删除操作---完成
    # result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
    # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
    returnJson = result['aggregations']['popular_colors']['buckets']
    print(returnJson)
    return HttpResponse(json.dumps(returnJson), content_type="application/json")
    # return returnJson;
def hiddenHistoricalTrend(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
  "size": 0,
  "aggs": {
    "popular_colors": {
      "terms": {
        "field": "发现人单位.keyword"
      },
      "aggs": {
        "test": {
          "date_histogram": {
            "field": "发现日期",
            "interval": "month",
            "format": "yyyy-MM-dd"
          }
        }
      }
    }
  }
}

    result = obj.search(index='lishikai_index000', body=dsl)
    # print(result)
    # 修改用户信息--例如密码  --传入id
    # data = {
    #     'username': '美国留给伊拉克的是个烂摊子吗',
    #     'password': '123',
    # }
    # data1 = {'_index': 'users',
    #         '_id': 'xaJSHG8B0WQk4EfReCWF',
    #         '_source': data,        # 实现更新操作-------更新用户名或者密码
    #         '_op_type': 'index'}
    # result = bulk(obj, actions=[data1])
    # # bulk()
    # # 删除操作---完成
    # result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
    # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
    returnJson = result['aggregations']['popular_colors']['buckets']
    keyget = ''
    for key in returnJson:
        key1=key['key']
        keyget += '\''+key1+'\''+','
    dataget = ''
    for key in returnJson:
        key1=key['test']['buckets']
        # name = key['key']
        # keyget += '\''+key1+'\''+','
        for key2 in key1:
            dataget += '\''+key2['key_as_string']+'\''+','

        break;
    graphGet = ''
    graphdata={}
    for key in returnJson:
        key1=key['test']['buckets']
        name = key['key']
        # keyget += '\''+key1+'\''+','
        list = []
        # graphGet1 = '['
        for key2 in key1:
            # graphGet += key2['doc_count']
            list.append(key2['doc_count'])
        # graphGet1 += ']'
        graphdata[name]= list
    print(keyget)
    print(dataget)
    print('--------------')
    print(graphdata)
    print(returnJson)
    # return HttpResponse(json.dumps(returnJson), content_type="application/json")
    # return returnJson;

    def hiddenHistoricalTrend(request):
        print(request)
        obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
            "size": 0,
            "aggs": {
                "popular_colors": {
                    "terms": {
                        "field": "发现人单位.keyword"
                    },
                    "aggs": {
                        "test": {
                            "date_histogram": {
                                "field": "发现日期",
                                "interval": "month",
                                "format": "yyyy-MM-dd"
                            }
                        }
                    }
                }
            }
        }

        result = obj.search(index='lishikai_index000', body=dsl)
        # print(result)
        # 修改用户信息--例如密码  --传入id
        # data = {
        #     'username': '美国留给伊拉克的是个烂摊子吗',
        #     'password': '123',
        # }
        # data1 = {'_index': 'users',
        #         '_id': 'xaJSHG8B0WQk4EfReCWF',
        #         '_source': data,        # 实现更新操作-------更新用户名或者密码
        #         '_op_type': 'index'}
        # result = bulk(obj, actions=[data1])
        # # bulk()
        # # 删除操作---完成
        # result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
        # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
        returnJson = result['aggregations']['popular_colors']['buckets']
        keyget = ''
        for key in returnJson:
            key1 = key['key']
            keyget += '\'' + key1 + '\'' + ','
        dataget = ''
        for key in returnJson:
            key1 = key['test']['buckets']
            # name = key['key']
            # keyget += '\''+key1+'\''+','
            for key2 in key1:
                dataget += '\'' + key2['key_as_string'] + '\'' + ','

            break;
        graphGet = ''
        graphdata = {}
        for key in returnJson:
            key1 = key['test']['buckets']
            name = key['key']
            # keyget += '\''+key1+'\''+','
            list = []
            # graphGet1 = '['
            for key2 in key1:
                # graphGet += key2['doc_count']
                list.append(key2['doc_count'])
            # graphGet1 += ']'
            graphdata[name] = list
        print(keyget)
        print(dataget)
        print('--------------')
        print(graphdata)
        print(returnJson)
        # return HttpResponse(json.dumps(returnJson), content_type="application/json")
        # return returnJson;
def hiddenReason(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
    "size" : 0,
    "aggs" : {
        "popular_colors" : {
            "terms" : {
              "field" : "隐患原因.keyword"
            }
        }
    }
}

    result = obj.search(index='lishikai_index000', body=dsl)
    # print(result)
    # 修改用户信息--例如密码  --传入id
    # data = {
    #     'username': '美国留给伊拉克的是个烂摊子吗',
    #     'password': '123',
    # }
    # data1 = {'_index': 'users',
    #         '_id': 'xaJSHG8B0WQk4EfReCWF',
    #         '_source': data,        # 实现更新操作-------更新用户名或者密码
    #         '_op_type': 'index'}
    # result = bulk(obj, actions=[data1])
    # # bulk()
    # # 删除操作---完成
    # result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
    # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
    returnJson = result['aggregations']['popular_colors']['buckets']
    print(returnJson)

    keyget = ''
    dataGraphlist = []

    for key in returnJson:
        dataGraph = {}
        test = ''
        key1=key['key']
        keyget += '\''+key1+'\''+','
        value = key['doc_count']
        dataGraph['name']=key1
        dataGraph['value'] = value
        test = dataGraph
        dataGraphlist.append(test)



    # 使用dict键值对不能重复
    # keyget = ''
    # dataGraph = {}
    # for key in returnJson:
    #     key1=key['key']
    #     keyget += '\''+key1+'\''+','
    #     value = key['doc_count']
    #     dataGraph['name']=key1
    #     dataGraph['value'] = value
    # dataget = ''
    # for key in returnJson:
    #     key1=key['test']['buckets']
    #     # name = key['key']
    #     # keyget += '\''+key1+'\''+','
    #     for key2 in key1:
    #         dataget += '\''+key2['key_as_string']+'\''+','
    #
    #     break;
    # graphGet = ''
    # graphdata={}
    # for key in returnJson:
    #     key1=key['test']['buckets']
    #     name = key['key']
    #     # keyget += '\''+key1+'\''+','
    #     list = []
    #     # graphGet1 = '['
    #     for key2 in key1:
    #         # graphGet += key2['doc_count']
    #         list.append(key2['doc_count'])
    #     # graphGet1 += ']'
    #     graphdata[name]= list
    print(keyget)
    print(dataGraphlist)
    # print(dataget)
    # print('--------------')
    # print(graphdata)
    # print(returnJson)
    # return HttpResponse(json.dumps(returnJson), content_type="application/json")
    # return returnJson;
def hiddenFrom(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
    "size" : 0,
    "aggs" : {
        "popular_colors" : {
            "terms" : {
              "field" : "隐患来源.keyword"
            }
        }
    }
}

    result = obj.search(index='lishikai_index000', body=dsl)
    # print(result)
    # 修改用户信息--例如密码  --传入id
    # data = {
    #     'username': '美国留给伊拉克的是个烂摊子吗',
    #     'password': '123',
    # }
    # data1 = {'_index': 'users',
    #         '_id': 'xaJSHG8B0WQk4EfReCWF',
    #         '_source': data,        # 实现更新操作-------更新用户名或者密码
    #         '_op_type': 'index'}
    # result = bulk(obj, actions=[data1])
    # # bulk()
    # # 删除操作---完成
    # result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
    # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
    returnJson = result['aggregations']['popular_colors']['buckets']
    print(returnJson)

    keyget = ''
    dataGraphlist = []

    for key in returnJson:
        dataGraph = {}
        test = ''
        key1=key['key']
        keyget += '\''+key1+'\''+','
        value = key['doc_count']
        dataGraph['name']=key1
        dataGraph['value'] = value
        test = dataGraph
        dataGraphlist.append(test)

        dataGraphlist2 = [['score', 'amount', 'product']]

        for key in returnJson:
            dataGraph = []
            test = ''
            key1 = key['key']
            keyget += '\'' + key1 + '\'' + ','
            value = key['doc_count']
            dataGraph.append(82)
            dataGraph.append(value)
            dataGraph.append(key1)
            test = dataGraph
            dataGraphlist2.append(test)

    print(dataGraphlist2)

    # 使用dict键值对不能重复
    # keyget = ''
    # dataGraph = {}
    # for key in returnJson:
    #     key1=key['key']
    #     keyget += '\''+key1+'\''+','
    #     value = key['doc_count']
    #     dataGraph['name']=key1
    #     dataGraph['value'] = value
    # dataget = ''
    # for key in returnJson:
    #     key1=key['test']['buckets']
    #     # name = key['key']
    #     # keyget += '\''+key1+'\''+','
    #     for key2 in key1:
    #         dataget += '\''+key2['key_as_string']+'\''+','
    #
    #     break;
    # graphGet = ''
    # graphdata={}
    # for key in returnJson:
    #     key1=key['test']['buckets']
    #     name = key['key']
    #     # keyget += '\''+key1+'\''+','
    #     list = []
    #     # graphGet1 = '['
    #     for key2 in key1:
    #         # graphGet += key2['doc_count']
    #         list.append(key2['doc_count'])
    #     # graphGet1 += ']'
    #     graphdata[name]= list
    print(keyget)
    print(dataGraphlist)
    # print(dataget)
    # print('--------------')
    # print(graphdata)
    # print(returnJson)
    # return HttpResponse(json.dumps(returnJson), content_type="application/json")
    # return returnJson;
def hiddenOfficeFrom(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
    "size" : 0,
    "aggs" : {
        "popular_colors" : {
            "terms" : {
              "field" : "隐患来源.keyword"
            },
            "aggs" : {
        "popular_colors" : {
            "terms" : {
              "field" : "发现人单位.keyword"
            }
        }
    }
        }
    }
}


    result = obj.search(index='lishikai_index000', body=dsl)
    # print(result)
    # 修改用户信息--例如密码  --传入id
    # data = {
    #     'username': '美国留给伊拉克的是个烂摊子吗',
    #     'password': '123',
    # }
    # data1 = {'_index': 'users',
    #         '_id': 'xaJSHG8B0WQk4EfReCWF',
    #         '_source': data,        # 实现更新操作-------更新用户名或者密码
    #         '_op_type': 'index'}
    # result = bulk(obj, actions=[data1])
    # # bulk()
    # # 删除操作---完成
    # result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
    # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
    returnJson = result['aggregations']['popular_colors']['buckets']
    print(returnJson)

    keyget = ''
    dataGraphlist = []

    for key in returnJson:
        dataGraph = {}
        test = ''
        key1=key['key']
        keyget += '\''+key1+'\''+','
        dataGraphlist.append(key1)
        list = []
        for key2 in key['popular_colors']['buckets']:
            list.append(key2['doc_count'])
        dataGraphlist.append(list)




        # value = key['doc_count']
        # dataGraph['name']=key1
        # dataGraph['value'] = value
        # test = dataGraph
        # dataGraphlist.append(test)
        #
        # dataGraphlist2 = [['score', 'amount', 'product']]

        # for key in returnJson:
        #     dataGraph = []
        #     test = ''
        #     key1 = key['key']
        #     keyget += '\'' + key1 + '\'' + ','
        #     value = key['doc_count']
        #     dataGraph.append(82)
        #     dataGraph.append(value)
        #     dataGraph.append(key1)
        #     test = dataGraph
        #     dataGraphlist2.append(test)

    print(keyget)
    print(dataGraphlist)

    # 使用dict键值对不能重复
    # keyget = ''
    # dataGraph = {}
    # for key in returnJson:
    #     key1=key['key']
    #     keyget += '\''+key1+'\''+','
    #     value = key['doc_count']
    #     dataGraph['name']=key1
    #     dataGraph['value'] = value
    # dataget = ''
    # for key in returnJson:
    #     key1=key['test']['buckets']
    #     # name = key['key']
    #     # keyget += '\''+key1+'\''+','
    #     for key2 in key1:
    #         dataget += '\''+key2['key_as_string']+'\''+','
    #
    #     break;
    # graphGet = ''
    # graphdata={}
    # for key in returnJson:
    #     key1=key['test']['buckets']
    #     name = key['key']
    #     # keyget += '\''+key1+'\''+','
    #     list = []
    #     # graphGet1 = '['
    #     for key2 in key1:
    #         # graphGet += key2['doc_count']
    #         list.append(key2['doc_count'])
    #     # graphGet1 += ']'
    #     graphdata[name]= list
    print(keyget)
    print(dataGraphlist)
    # print(dataget)
    # print('--------------')
    # print(graphdata)
    # print(returnJson)
    # return HttpResponse(json.dumps(returnJson), content_type="application/json")
    # return returnJson;
if __name__ == '__main__':
    # statisticForEcharts(111)
    # hiddenHistoricalTrend(111)
    # hiddenReason(123)
    # hiddenFrom(123)
    hiddenOfficeFrom(123)