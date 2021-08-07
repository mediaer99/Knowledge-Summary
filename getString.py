import re
import os
import sys

'''
提取某两个字符串之间的内容并保存
示例提取 us HW之间的字符串
'''
def getStr(filename):
    file_pts = 'output.txt'
        
    with open(filename, 'r', encoding='UTF-8') as f0:
        with open(file_pts, 'w') as f1:
            key = re.compile('us (.*?) HW')

            for line in f0.readlines():
                        
                value = re.search(key, line)
                if value != None:
                    ret = value.group().strip()
                    ret = ret.replace("us", "").replace("HW", "")
                    f1.write(ret+'\n')

if __name__ == '__main__':
    print("Use:  filename")
    inputFile = sys.argv[1]
    getStr(inputFile)




