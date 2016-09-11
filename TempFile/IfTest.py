# -*- coding: utf-8 -*- 
'''
Created on 2016��8��21��

@author: xiong
'''
'''
result = 'this is test message ' if 2 > 1 else "this is second"
print result


s= 'i am {0} {1}'
print  s.format('alex','bii')   

com = compile('1+1','','eval')
print eval(com)
'''
import subprocess

cmd="cmd.exe"
begin=101
end=200
while begin<end:

    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,
                   stdin=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    p.stdin.write("ping 192.168.1."+str(begin)+"\n")

    p.stdin.close()
    p.wait()

    print "execution result: %s"%p.stdout.read()