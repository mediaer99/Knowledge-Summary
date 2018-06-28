import os
import sys
import subprocess

#global variable
ret_lib = ''
branch = ''
############################################################
def git_add_commit_chmod():
    global branch
    gitCmd = ''
    #get result of 'git status'
    status0,srcCmd = subprocess.getstatusoutput("git status")
    if status0 != 0:
        print("git status failed!")
        exit() 
    print("********* %s ********* \n%s" % ("git status",srcCmd))
    #get every line of srcCmd
    Src = srcCmd.split('\n')
    #remove modified:
    for line in Src:
        if 'modified:' in line:
            gitCmd = gitCmd + ' ' + line.replace('modified:', '')
        if 'new file:'  in  line:
             gitCmd = gitCmd + ' ' + line.replace('new file:', '')
            
    while True:
        cmd = input('Input your git command(\'q\' to quit): ')
        if cmd == 'q':
            break
        
        cmd_init = cmd
        cmd = cmd + ' ' + gitCmd + '\n'
        #print(cmd)
        status1 = os.system(cmd)
        if status1 == 0:
            print('%s Executing successed!' % cmd_init)
        
    print("\nSure push your code ? [y/n]\n")
    while True:
        ret = input()
        if ret == 'n':
           exit()
        elif ret == 'y':
            cmd_push = 'git push gerrit HEAD:refs/for/' + branch
            print(cmd_push)
            #omx_git_cmd(cmd_push)
            break
        else:
            print("please input again: [y/n]")

############################################################
#change word-dir
def omx_chdir(dir):
    status = os.chdir(dir)
    if status == 0:
        print("coming into directory(%s) failed!" % dir)
        exit()
    print("\n>>> coming into directory(%s) <<<\n" % os.getcwd())

############################################################
#excute git command
def omx_git_cmd(cmd):
    status, srcCmd = subprocess.getstatusoutput(cmd)
    print("********* %s ********* \n%s" % (cmd,srcCmd))
    if status != 0:
        print("%s failed!" % cmd)
        exit()
    if 'git push' in cmd:
        print('%s Executing successed!' % cmd)
        exit()

############################################################
#excute git command
def omx_git_cmd_lib(cmd):
    status, srcCmd = subprocess.getstatusoutput(cmd)
    global ret_lib
    ret_lib = srcCmd.split('\n')
    print("come into omx_git_cmd_lib......")
    print("********* %s ********* \n%s" % (cmd,srcCmd))
    if status != 0:
        print("%s failed!" % cmd)
        exit()

############################################################          
def get_branch_loop():
        #print(Src)
        global branch
        for line in ret_lib:
            if 'On branch' in line:
                branch = line.replace('On branch ', '')
                status,srcCmd = subprocess.getstatusoutput("git checkout " + branch)
                cmd = 'git checkout ' + branch
                if status != 0:
                    print("\n%s failed!\n" % cmd)
                    exit()
                print('\n********* git checkout ********* \n%s Executing successed!\n' % cmd)
############################################################  
def omx_so_push(version, product):
    #Blow omx_so_name is mainly for version 8.0/8.1
    omx_so_name = "libdatachunkqueue_alt.so libfpscalculator_alt.so libomx_av_core_alt.so libomx_clock_utils_alt.so libomx_framework_alt.so libomx_timed_task_queue_alt.so libomx_worker_peer_alt.so libOmxBase.so libOmxCore.so libOmxVideo.so libstagefrighthw.so  libthreadworker_alt.so libOmxAudio.so libOmxCoreSw.so"
    
    #current directory
    curr_init_dir = os.getcwd()
    #directory to commit omx so
    push_cd_dir = curr_init_dir + '/vendor/xxx/prebuilt/libstagefrighthw/lib/'
    #directory to produce omx so
    compil_lib_dir = curr_init_dir + "/out/target/product/" + product + "/vendor/lib"
    
    omx_chdir(push_cd_dir)
    #get result of 'git status'
    omx_git_cmd_lib("git status")
    print("\nGoing on ? [y/n]\n")
    while True:
        ret = input()
        if ret == 'n':
            exit()
        elif ret == 'y':
            get_branch_loop()
            break
        else:
            print("please input again: [y/n]")
        
    #get result of 'git pull'
    omx_git_cmd("git pull")

    if version == '8.1':
        omx_chdir(compil_lib_dir)
        omx_git_cmd("cp  " + omx_so_name + "  " + push_cd_dir)
        omx_chdir(push_cd_dir)
        git_add_commit_chmod()



if __name__ == '__main__':
    #add argv check
    print("\nUsage argv[1]: version(8.1)  argv[2]: product(p212)\n")
    if sys.argv[1] == None:
        print("please input version info(7.1/8.0/8.1/...)")
        exit()
    elif sys.argv[2] == None:
        print("please input product info(p212/p241/...)")
        exit()
    #get version info
    version = sys.argv[1]
    product = sys.argv[2]
    omx_so_push(version, product)