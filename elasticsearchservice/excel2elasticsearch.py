
import xlrd
import json
from djangodemo import settings



def writ_from_dirct(filepath):

        # 获取excel文件     从文件夹获取所有的excel遍历操作写入数据中心
        data = xlrd.open_workbook(filepath,encoding_override='utf-8')
        #获取一个excel有多少个sheet
        sheetNames = list(data.sheet_names())
        print(sheetNames)

        # 生成写入文件设置 上一个文件是data22.txt
        # with open('processtologstash/data-end.txt','a') as f:    #设置文件对象
        with open('processtologstash/data-end.txt','a',encoding='utf-8') as f:    #设置文件对象
            # 遍历写入文件
            for name in sheetNames:
                    if (name.__eq__("基础数据")):
                            continue
                    # 获取sheet
                    sheet = data.sheet_by_name(name)
                    # 获取总行数
                    nrows = sheet.nrows
                    print(nrows)
                    # 获取总列数
                    ncols = sheet.ncols
                    print(ncols)
                    # 获取一行的数值
                    #table.row_values(i)
                    # 获取一列的数值
                    key1 = sheet.cell(2, 1).value.strip()
                    value1 = sheet.cell(2, 2).value.strip()
                    json_str = '{"'+key1+'"'+':'+"\""+value1+"\","

                    key1 = sheet.cell(2, 5).value.strip()
                    value1 = sheet.cell(2, 6).value.strip()
                    json_str = json_str +'"'+key1+'"'+':'+"\""+value1+"\","

                    key1 = sheet.cell(2, 8).value.strip()
                    value1 = sheet.cell(2, 9).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","

                    # 这里是一列的循环
                    # key1 = sheet.cell(3, 1).value.strip()
                    # value1 = sheet.cell(3, 2).value.strip()
                    # json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"
                    #
                    # key1 = sheet.cell(4, 1).value.strip()
                    # value1 = sheet.cell(4, 2).value.strip()
                    # json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"
                    #
                    # key1 = sheet.cell(5, 1).value.strip()       #事故隐患内容
                    # value1 = sheet.cell(5, 2).value.strip()
                    # json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"
                    #
                    # key1 = sheet.cell(6, 1).value.strip()         #可能造成后果
                    # value1 = sheet.cell(6, 2).value.strip()
                    # json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"
                    #
                    # key1 = sheet.cell(7, 1).value.strip()
                    # value1 = sheet.cell(7, 2).value.strip()
                    # json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"
                    #
                    # key1 = sheet.cell(8, 1).value.strip()
                    # value1 = sheet.cell(8, 2).value.strip()
                    # json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"
                    #
                    # key1 = sheet.cell(9, 1).value.strip()
                    # value1 = sheet.cell(9, 2).value.strip()
                    # json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"


        # 18
                    for i in range(3, 15):      # 防控措施是15 事故隐患内容是5
                            key1 = sheet.cell(i, 1).value.strip()
                            value1 = sheet.cell(i, 2).value.strip()
                            # key1.replace("\n", "")
                            # key1.replace("\r", "").replace("\n", "")
                            # key1 = [x.strip() for x in key1]
                            key1 = key1.replace('\n', '').replace('\r', '')
                            value1 = value1.replace('\n', '').replace('\r', '')
                            value1  = value1.replace(' ', '')
                            key1  = key1.replace(' ', '')
                            if key1 == "" or value1 == "":
                                continue;
                            json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","

                    # for i in range(10, 14):
                    #         key1 = sheet.cell(i, 1).value.strip()
                    #         value1 = sheet.cell(i, 2).value.strip()
                    #         json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\",\n"

                    for i in range(16, 18):
                            key1 = sheet.cell(i, 1).value.strip()
                            value1 = sheet.cell(i, 2).value.strip()
                            if key1 == "" or value1 == "":
                                continue;
                            json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","

                    for i in range(20, 22):
                            key1 = sheet.cell(i, 1).value.strip().strip()
                            value1 = sheet.cell(i, 2).value.strip()
                            if key1 == "" or value1 == "":
                                continue;
                            json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","

                    for i in range(3, 11):
                            key1 = sheet.cell(i, 3).value.strip()
                            value1 = sheet.cell(i, 4).value.strip()
                            if key1 == "" or value1 == "":
                                continue;
                            json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","
                    # "评估负责人签名": "郑金鹏",
                    for i in range(3, 11):
                            key1 = sheet.cell(i, 5).value.strip()
                            value1 = sheet.cell(i, 6).value.strip()
                            if key1 == "" or value1 == "":
                                continue;
                            json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","


                    key1 = sheet.cell(3,8).value.strip()
                    value1 = sheet.cell(3,9).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","
                    # json_str = '"' + key1 + '"' + ':' + '"' + value1 + '"'

                    # 治理责任人 sheet.cell(11,4)
                    key1 = sheet.cell(11, 4).value.strip()
                    value1 = sheet.cell(11, 5).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","


                    # 治理期限


                    # 治理方案



                    # 治理完成情况 sheet.cell(15,1) sheet.cell(15,2)

                    key1 = sheet.cell(15,1).value.strip()
                    value1 = sheet.cell(15,2).value.strip()
                    key1 = key1.replace('\n', '').replace('\r', '')
                    value1 = value1.replace('\n', '').replace('\r', '')
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","

                    # 隐患治理计划资金(万元) sheet.cell(16,1)  sheet.cell(16,3)
                    key1 = sheet.cell(16, 1).value.strip()
                    value1 = sheet.cell(16, 2).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","
                    # 累计落实治理资金(万元) sheet.cell(16,5)  sheet.cell(16,8)
                    key1 = sheet.cell(16, 5).value.strip()
                    value1 = sheet.cell(16, 8).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","
                    # 负责人 sheet.cell(17,3) sheet.cell(17,4)
                    key1 = sheet.cell(17, 3).value.strip()
                    value1 = sheet.cell(17, 4).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","
                    # 签字日期  sheet.cell(17,5)  sheet.cell(17,6)
                    key1 = sheet.cell(17, 5).value.strip()
                    value1 = sheet.cell(17, 6).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","

                    # 验收组织单位 sheet.cell(18,1) sheet.cell(18,2)
                    key1 = sheet.cell(18, 1).value.strip()
                    value1 = sheet.cell(18, 2).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","


                    # 验收意见 sheet.cell(19,1) sheet.cell(19,2)
                    key1 = sheet.cell(19, 1).value.strip()
                    value1 = sheet.cell(19, 2).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","

                    # 验收日期sheet.cell(21, 5)  sheet.cell(21, 6)
                    key1 = sheet.cell(21, 5).value.strip()
                    value1 = sheet.cell(21, 6).value.strip()
                    json_str = json_str + '"' + key1 + '"' + ':' + "\"" + value1 + "\","
                    # 是否消除
                    sfxc = sheet.cell(20, 5).value.strip()
                    sfxcinput = sheet.cell(20, 6).value.strip()
                    json_str = json_str + '"' + sfxc + '"' + ':' + "\"" + sfxcinput + "\"}\n"



                    # print(json_str)
                    f.write(json_str)
                    print(json_str)

if __name__ == '__main__':
    writ_from_dirct("D:/隐患库/配电.xls")