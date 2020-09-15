import os
from kgextacttrip import LTP_Python_Interface_before
class LtpParser:
    def __init__(self):
        # LTP_DIR = "./ltp_data"
        self.model = LTP_Python_Interface_before.LTP_MODEL()
        # self.segmentor = model.segment(input_list='')
        # # self.segmentor.load(os.path.join(LTP_DIR, "cws.model"))
        # self.postagger = model.postagger()
        # # self.postagger.load(os.path.join(LTP_DIR, "pos.model"))
        # self.parser = model.Parser()
        # # self.parser.load(os.path.join(LTP_DIR, "parser.model"))
        # self.recognizer = model.NamedEntityRecognizer()
        # # self.recognizer.load(os.path.join(LTP_DIR, "ner.model"))
        # self.labeller = model.SementicRoleLabeller()
        # # self.labeller.load(os.path.join(LTP_DIR, 'pisrl.model'))

    '''语义角色标注'''
    def format_labelrole(self, words, postags):
        arcs = self.model.Parse(words)
        # arcs = self.parser.parse(words, postags)
        # roles = self.labeller.label(words, postags, arcs)
        roles = self.model.SementicRoleLabeller([words])
        roles_dict = {}
        for role in roles:
            for role1 in role:
                for role2 in role1:
                    for arg in role2['arg']:
                        roles_dict[role2['index']]={role2['name']:[role2['name'],arg['@beg'],arg['@end']]}
            # roles_dict[role.index] = {arg[0][0]:[arg.name,arg.range.start, arg.range.end] for arg in role}
        return roles_dict

    '''句法分析---为句子中的每个词语维护一个保存句法依存儿子节点的字典'''
    def build_parse_child_dict(self, words, postags, arcs):
        child_dict_list = []
        format_parse_list = []
        for index in range(len(words)):
            child_dict = dict()
            for arc_index in range(len(arcs)):
                if arcs[arc_index]['head'] == index+1:   #arcs的索引从1开始
                    if arcs[arc_index]['relation'] in child_dict:
                        child_dict[arcs[arc_index]['relation']].append(arc_index)
                    else:
                        child_dict[arcs[arc_index]['relation']] = []
                        child_dict[arcs[arc_index]['relation']].append(arc_index)
            child_dict_list.append(child_dict)
        rely_id = [arc['head'] for arc in arcs]  # 提取依存父节点id
        relation = [arc['relation'] for arc in arcs]  # 提取依存关系
        heads = ['Root' if id == 0 else words[id - 1] for id in rely_id]  # 匹配依存父节点词语
        for i in range(len(words)):
            # ['ATT', '李克强', 0, 'nh', '总理', 1, 'n']
            a = [relation[i], words[i], i, postags[0][i][1], heads[i], rely_id[i]-1, postags[0][rely_id[i]-1]][1]
            format_parse_list.append(a)

        return child_dict_list, format_parse_list

    '''parser主函数'''
    def parser_main(self, sentence):
        words = list(self.model.segment(sentence))
        postags = list(self.model.postagger(sentence))
        arcs = list(self.model.Parse(sentence[0]))
        # arcs = self.parser.parse(words, postags)
        # self.build_parse_child_dict(words, postags, arcs)
        # child_dict_list  = self.model.build_parse_child_dict(words, postags, arcs)
        child_dict_list, format_parse_list = self.build_parse_child_dict(words, postags, arcs)
        roles_dict = self.format_labelrole(sentence[0], postags)
        return words, postags, child_dict_list, roles_dict, format_parse_list


if __name__ == '__main__':
    parse = LtpParser()
    # model = LTP_Python_Interface.LTP_MODEL()  这个分明是sentence_parse.py
    sentence = ['李克强总理今天来我家了,我感到非常荣幸']
    test = sentence[0]
    words, postags, child_dict_list, roles_dict, format_parse_list = parse.parser_main(sentence)
    print(words, len(words))
    print(postags, len(postags))
    print(child_dict_list, len(child_dict_list))
    print(roles_dict)
    print(format_parse_list, len(format_parse_list))