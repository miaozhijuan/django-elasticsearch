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


from elasticsearch.helpers import bulk

def statisticForEcharts(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
    returnJson = result['aggregations']['popular_colors']['buckets']
    print(returnJson)
    return HttpResponse(json.dumps(returnJson), content_type="application/json")
    # return returnJson;
def hiddenHistoricalTrend(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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

    def hiddenHistoricalTrend(request):
        print(request)
        obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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
            list = []
            for key2 in key1:
                list.append(key2['doc_count'])
            graphdata[name] = list
        print(keyget)
        print(dataget)
        print('--------------')
        print(graphdata)
        print(returnJson)
def hiddenReason(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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



    print(keyget)
    print(dataGraphlist)
def hiddenFrom(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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

    print(keyget)
    print(dataGraphlist)
def hiddenOfficeFrom(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
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





    print(keyget)
    print(dataGraphlist)
    print(keyget)
    print(dataGraphlist)
if __name__ == '__main__':
    statisticForEcharts(111)
    # hiddenHistoricalTrend(111)
    # hiddenReason(123)
    # hiddenFrom(123)
    # hiddenOfficeFrom(123)