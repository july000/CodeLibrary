import re
import reprlib

RE_WORD = re.compile('\w+')     #将正则表达式编译成正则表达式对, \w的功能是匹配付费特殊的字符, 即大小写字母、数字、下划线、汉字

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)      #findall函数是找到所有的匹配的子串，结果作为一个列表返回, 可迭代

    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' %reprlib.repr(self.text)      #用于生成大型数据结构的简略字符串表示形式, 默认情况下，reprlib.repr 函数生成的字符串最多有 30 个字符
    
# python 从可迭代的对象中获取迭代器
# StopIteration异常表明迭代器到头了
# 标准的迭代器接口有两个方法：__next__， __iter__