import re
import os
import sys


def get_In_Out_Pts(filename,in_out):
    if in_out == 'out':
        file_pts = 'out_pts.txt'
    elif in_out == 'in':
        file_pts = 'in_pts.txt'
        
    with open(filename, 'r') as f0:
            with open(file_pts, 'w') as f1:
                if in_out == 'out': 
                    key = re.compile('Out PTS: (.*)..vf')
                elif in_out == 'in':
                    #key = re.compile('In PTS (.*),  ')
                    key = re.compile('In PTS (.*),\\t')
                
                for line in f0.readlines():
                    value = re.search(key, line)
                    if value != None:
                        ret = value.group().strip()
                        if in_out == 'out':
                            if True:
                                #method one
                                ret = re.sub(r'\D+', "", ret)
                            else:
                                #method two
                                ret = ret.replace('Out PTS: ','')
                                ret = ret.replace('vf','')
                                ret = ret.replace('.','')
                            f1.write(ret+'\n')
                        elif in_out == 'in':
                            if True:
                                ret = re.sub(r'\D+', "", ret)
                            else:
                                ret = ret.replace('In PTS ','')
                                ret = ret.replace(',','')
                            f1.write(ret+'\n')

if __name__ == '__main__':
    print("Use:  filename  in(out)")
    filename = sys.argv[1]
    in_out = sys.argv[2]
    get_In_Out_Pts(filename,in_out)




