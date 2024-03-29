from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import requests
import json
import simplejson
from elasticsearch import Elasticsearch, TransportError
import os
import shutil
from elasticsearchservice import traverse
from djangodemo import settings


# 参数传递方法封装
from elasticsearch.helpers import bulk


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

    headers ={'content-type': 'application/json'}
    url = settings.REQUEST_ES_RUL
    # ret = requests.post("http://127.0.0.1:9200/lishikai_index007/_search",data=json.dumps(payload),headers=headers)
    ret = requests.post(url,data=json.dumps(payload),headers=headers)
    # reqparam = request.body.decode('utf-8')  json解析完成
    reqparam =simplejson.loads(request.body.decode('utf-8'))
    print(reqparam['query']['match']['发现人'])  #
    return HttpResponse(ret.text)

# 修改
def CRUDParamMethod(request):
    print(request)
    ipPort = settings.REQUEST_ES_IP_PORT
    obj = Elasticsearch(ipPort)

    dsl = {
        'query': {
            'match_phrase': {
                'username': '李仕凯'
            }
        }
    }

    result = obj.search(index='users', body=dsl)

    data = {
        'username': '美国留给伊拉克的是个烂摊子吗',
        'password': '123',
    }
    data1 = {'_index': 'users',
            '_id': 'xaJSHG8B0WQk4EfReCWF',
            '_source': data,        # 实现更新操作-------更新用户名或者密码
            '_op_type': 'index'}
    result = bulk(obj, actions=[data1])
    result = obj.delete(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF')
    # result = obj.update(index='users', doc_type='_doc', id='xaJSHG8B0WQk4EfReCWF', body=json.dumps(data))
    print(result)
    return '你好世界！！';


# 用户新增创建一个关于用户单独的索引，维护对于用户的增删改查等操作  根据什么唯一确定一个用户。用户名和啥



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

def upload_file(request):
    print(request.FILES)
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("file", None)    # 获取上传的文件，如果没有文件，则默认为None
        print(myFile)
        if not myFile:
            print(myFile.name)
            return HttpResponse("no files for upload!")
        #  todo 需要修改地址或者改成全局变量容易修改
        destination = open(os.path.join(settings.uploadDir,myFile.name),'wb+')    # C:\Users\22934\PycharmProjects\djangodemo\upload打开特定的文件夹进行二进制的写操作
        # destination = open(os.path.join("C:\\Users\\22934\\PycharmProjects\\djangodemo\\upload",myFile.name),'wb+')    # C:\Users\22934\PycharmProjects\djangodemo\upload打开特定的文件夹进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        print(destination)

        traverse.traverse_dir(settings.uploadDir)
        # traverse.traverse_dir('C:/Users/22934/PycharmProjects/djangodemo/upload')
        # elasticsearch 调用logstash，或者按行读取发送数据到elasticsearch、哪个简单

        # 清空文件内容加载最后删除文件中

        # 关闭文件
        destination.close()
        deleteAllTheFile()
        return HttpResponse("upload over!")
def sent_json_to_elasticsearch(request):
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
    # # 創建索引index:索引的名字,body:數據,ignore:狀態碼
    # result = obj.indices.create(index="users", body={"username": "李仕凯", "password": "123"}, ignore=400)
    # 判断是否存在文件
    file = open("processtologstash/data-end.txt","r+",encoding="utf-8")
    # file = open("C:\\Users\\22934\\PycharmProjects\\djangodemo\\processtologstash\\data-end.txt")
    print('进入发送json数据给elasticsearch')
    # try:
    # while 1:
    line = file.readline()

    while line:
        if not line:
            continue
        result = obj.index(index='lishikai_index000', doc_type='_doc', body=line,ignore=400)
        print(result)
        # print(line, end = '')　      # 在 Python 3 中使用
        line = file.readline()

    # except TransportError as e:
    #     print(e.info)
    # while 1:
    #     lines = file.readlines(10)
    #     if not lines:
    #         break
    #     for line in lines:
    #         result = obj.index(index='testadd', doc_type='_doc', body=line)
    #         print(result)
    print('读取结束')
    # 清空文件内容
    file.close()
    shutil.rmtree(settings.processToTogstashDirTest)
    # shutil.rmtree("C:\\Users\\22934\\PycharmProjects\\djangodemo\\processtologstash")

    os.mkdir(settings.processToTogstashDirTest)
    # os.mkdir("C:\\Users\\22934\\PycharmProjects\\djangodemo\\processtologstash")
    return HttpResponse("upload over!")
def processHandleInput(request):
    obj = Elasticsearch(settings.REQUEST_ES_IP_PORT)
    # todo 处理请求过来的json数据
    # print(request.content_params)
    # print(request.body)
    print(request.body)
    json_result = json.loads(request.body)
    print(json_result)
    result = obj.index(index='users', doc_type='_doc', body=json_result, ignore=400)
    print(result)
    return HttpResponse('handle over!')
def deleteAllTheFile():

    # 处理完之后删除文件/先上传再清空
    # os.remove("C:\\Users\\22934\\PycharmProjects\\djangodemo\\upload")
    shutil.rmtree(settings.uploadDir)
    # shutil.rmtree("C:\\Users\\22934\\PycharmProjects\\djangodemo\\upload")
    os.mkdir(settings.uploadDir)
    # os.mkdir("C:\\Users\\22934\\PycharmProjects\\djangodemo\\upload")
    # todo 删除文件夹再新建文件夹的形式
    # shutil.rmtree("C:\\Users\\22934\\PycharmProjects\\djangodemo\\processtologstash")
    # os.mkdir("C:\\Users\\22934\\PycharmProjects\\djangodemo\\processtologstash")
    return HttpResponse("upload over!")


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
