from urllib import request, parse

# from kgextacttrip.LTP_Python_Interface import LTP_MODEL


def request_ltpserver():
    # uri_base = "http://192.168.43.245:8080/ltp"
    #
    # data = {
    #     's': '我爱北京天安门',
    #     'x': 'n',
    #     't': 'all'}
    #
    # request = urllib.Request(uri_base)
    # params = urllib.urlencode(data)
    # response = urllib.urlopen(request, params)
    # content = response.read().strip()
    # print(content)
    #
    url = 'http://192.168.43.245:8080/ltp'

    # Dictionary of query parameters (if any)
    parms = {
        's': '我爱北京天安门',
        'x': 'n',
        't': 'all'
    }


    # Encode the query string
    querystring = parse.urlencode(parms)

    # Make a POST request and read the response
    u = request.urlopen(url, querystring.encode('UTF-8'))
    resp = u.read().strip()
    turn_string = str(resp, 'utf-8')
    # 转码
    print(turn_string)

if __name__ == '__main__':
    # input_sentence = "中国，是以华夏文明为源泉、中华文化为基础，并以汉族为主体民族的多民族国家，通用汉语、汉字，汉族与少数民族被统称为“中华民族”，又自称为炎黄子孙、龙的传人"
    # model = LTP_MODEL()
    # Subjective_guest, Dynamic_relation, Guest, Name_entity_relation = model.triple_extract(input_sentence)
    # for e in Subjective_guest[0]:
    #     print
    #     e,
    # print
    # "\n"
    # for e in Dynamic_relation[0]:
    #     print
    #     e,
    print("hello word")
    request_ltpserver()