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


# 参数传递方法封装
from elasticsearch.helpers import bulk

from kgextacttrip.LTP_Python_Interface_before import LTP_MODEL


def kgprocess(request):
    model = LTP_MODEL()
    json_result = json.loads(request.body)
    # json_result = json.dumps(json_result,ensure_ascii=False)
    # print(json_result['hits'][1])
    svoses = []
    for json_item in json_result['hits']:
        input_sentence = json_item['_source']['事故隐患内容']
        print(type(input_sentence))
        svos = model.extractTripleGroups(input_sentence)
        # print(input_sentence)
        # Subjective_guest, Dynamic_relation, Guest, Name_entity_relation = model.triple_extract(input_sentence)
        # for e in Subjective_guest[0]:
        #     print(e, end=' ')
        # print("\n")
        # # for e in Dynamic_relation[0]:
        # #     print(e, end=' ')
        # # for e in Guest[0]:
        # #     print(e)
        print('-------------------------------------')
        svoses += [svos]

    # print(json_result['total'])
    print(svoses)
    return HttpResponse(svoses)

if __name__ == '__main__':
    # CRUDParamMethod(1)
    # sent_json_to_elasticsearch()
    kgprocess(1)