import re
import os
import sys


def get_In_Out_Pts(filename,in_out):
    if in_out == 'out':
        file_pts = 'out_pts.txt'
    elif in_out == 'in':
        file_pts = 'in_pts.txt'

    file_awesome = 'awesome.txt'
        
    with open(filename, 'r', encoding='UTF-8') as f0:
        with open(file_pts, 'w') as f1, open(file_awesome, 'w') as f2:
            if in_out == 'out': 
                key = re.compile('Out PTS: (.*)..vf')
            elif in_out == 'in':
                key = re.compile('In PTS (\d+),')

            for line in f0.readlines():
                #write AmlogicVideoDecoderAwesome to awesome.txt
                if 'AmlogicVideoDecoderAwesome' in line:
                    f2.write(line)
                        
                value = re.search(key, line)
                if value != None:
                    ret = value.group().strip()
                    if in_out == 'out':
                        ret = re.sub(r'\D+', "", ret)
                        f1.write(ret+'\n')
                    elif in_out == 'in':
                        ret = re.sub(r'\D+', "", ret)
                        f1.write(ret+'\n')

if __name__ == '__main__':
    print("Use:  filename  in(out)")
    filename = sys.argv[1]
    in_out = sys.argv[2]
    get_In_Out_Pts(filename,in_out)




