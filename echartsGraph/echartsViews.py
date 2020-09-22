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



# 按单位统计分析未完成治理量

def statisticForUnitUncomplete(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
    dsl = {
            "size" : 0,
            "query": {
                "match": {
                    "是否消除": "是"
                }
            },
            "aggs" : {
                "popular_colors" : {
                    "terms" : {
                      "field" : "发现人单位.keyword"
                    }
                }
            }
        }

    result = obj.search(index='lishikai_index000', body=dsl)
    returnJson = result['aggregations']['popular_colors']['buckets']

    print(returnJson)
    return HttpResponse(json.dumps(returnJson), content_type="application/json")




# 是否治理完成分析
def statisticForIfZLcomplete(request):
    print(request)
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
    dsl = {
            "size" : 0,
            "aggs" : {
                "popular_colors" : {
                    "terms" : {
                      "field" : "是否消除.keyword"
                    }
                }
            }
        }

    result = obj.search(index='lishikai_index000', body=dsl)
    returnJson = result['aggregations']['popular_colors']['buckets']
    print(returnJson)
    return HttpResponse(json.dumps(returnJson), content_type="application/json")

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
    print(returnJson)
    return HttpResponse(json.dumps(returnJson), content_type="application/json")


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

    return HttpResponse(json.dumps(returnJson), content_type="application/json")

    # keyget = ''
    # dataGraphlist = []
    #
    # for key in returnJson:
    #     dataGraph = {}
    #     test = ''
    #     key1=key['key']
    #     keyget += '\''+key1+'\''+','
    #     value = key['doc_count']
    #     dataGraph['name']=key1
    #     dataGraph['value'] = value
    #     test = dataGraph
    #     dataGraphlist.append(test)
    #
    #
    #
    # print(keyget)
    # print(dataGraphlist)
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

    return HttpResponse(json.dumps(returnJson), content_type="application/json")


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
              "field" : "发现人单位.keyword",
                "order": {
                "_key": "desc"
                }
            }
        }
    }
        }
    }
}


    result = obj.search(index='lishikai_index000', body=dsl)
    returnJson = result['aggregations']['popular_colors']['buckets']
    print(returnJson)
    return HttpResponse(json.dumps(returnJson), content_type="application/json")


if __name__ == '__main__':
    # statisticForIfZLcomplete(111)
    # statisticForUnitUncomplete(111)
    hiddenHistoricalTrend(111)
    # hiddenReason(123)
    # hiddenFrom(123)
    # hiddenOfficeFrom(123)