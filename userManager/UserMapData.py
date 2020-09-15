from utils.singleton import singleton


@singleton # 单例测试
class UserMapData():
    def __init__(self):
        self.userMap = []
        self.score = []
    # def __init__(self, server_url="http://39.106.226.131:8080/ltp"):
    def test(self):
        self.userMap.append({"测试":"123"})
        # task 任务的具体形式，可以是分词：'ws'，词性标注：'pos',依存语法分析：'dp'，命名实体识别：ner语义角色标注：'srl',或者全部：'all'

        print(self.userMap)
    def test2(self):
        self.userMap.append({"测试":"1234"})
        # task 任务的具体形式，可以是分词：'ws'，词性标注：'pos',依存语法分析：'dp'，命名实体识别：ner语义角色标注：'srl',或者全部：'all'

        print(self.userMap)
    def test2(self):
        self.userMap.append({"测试":"1234"})
        # task 任务的具体形式，可以是分词：'ws'，词性标注：'pos',依存语法分析：'dp'，命名实体识别：ner语义角色标注：'srl',或者全部：'all'

        print(self.userMap)
    def requestUserAdd(request):
        request
    def userAdd(self,request):
        # self.userMap.append({"测试":"1234"})
        # task 任务的具体形式，可以是分词：'ws'，词性标注：'pos',依存语法分析：'dp'，命名实体识别：ner语义角色标注：'srl',或者全部：'all'
        print(request)
        print(self.userMap)