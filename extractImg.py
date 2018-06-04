import os
import sys

def list_file(path, sub):
    tail = '.img'
    if sub == '1':
        tail =  'img.tar.bz2'
    elif sub == '2':
        tail = '.img'
    
    parents = os.listdir(path)
    
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            list_file(child, sub)
        else:
            if child.endswith(tail):
                print("%s" %child)
            
import os
import sys

def list_file(path, sub, isDele):
    tail = '.img'
    if sub == '1':
        tail =  'img.tar.bz2'
    elif sub == '2':
        tail = '.img'
    
    parents = os.listdir(path)
    
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            list_file(child, sub, isDele)
        else:
            if child.endswith(tail):
                print("%s" %child)
                if isDele == "T":
                    print("Remove %s" %child)
                    os.remove(child)
            

if __name__ == "__main__":
    print("Usage: python 1/2 T/other  [1: img.tar.bz2, 2: .img, T: remove file]")
    sub = sys.argv[1]
    isDele = sys.argv[2]

    list_file(os.getcwd(), sub, isDele)
    #list_file(r'C:\Users\Desktop\BUG', sub, isDele)
    #os.system('pause')
    
    
    
    
if __name__ == "__main__":
    print("1: img.tar.bz2, 2: .img")
    sub = sys.argv[1]
    list_file(r'C:\Users\Desktop\BUG', sub)
    os.system('pause')