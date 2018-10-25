#!/usr/bin/env python
import os, time

host_list=open('./host').readlines()
host_dict = {}

def color_style(content):
    return '\033[1;32m' + '%s' + '\033[0m' % content 

# choice 
while True:
    print("="*60)
    print("    Host list   ")
    for index,host_cmd in enumerate(host_list):
        host_dict[str(index)]=host_cmd
        print("\033[1;32m        [%i]: %s\033[0m" % (index,host_cmd))
    print("End of input 'q' or 'quit' or 'exit'. ")
    print("="*60)
    n = raw_input("\033[1;32mChoice: \033[0m")
    if n == 'q' or n == 'quit' or n=='exit':
        exit(0)
    elif n not in host_dict:
        print("\033[1;31mPlease select the correct serial number.\033[0m")
        continue
    else:
        cmd = host_dict[n]
        os.system(cmd)  
    time.sleep(1)

