# -*- coding: utf-8 -*- 

#记录是否登录成功
LoginState=True
#密码输入次数
count = 0
#保存正常用户名和密码
UserName = []
PassWord = []
#保存锁定用户名和密码
LockedUser = []
#记录正常用户信息
Normal_User_Info_File="D:\\Normal_User_Accounts_Info.txt"
#记录被锁定用户信息
Locked_User_Info_File="D:\\Locked_User_Account_Info.txt"
#打开正常用户信息保存文件
Normal_Info=file(Normal_User_Info_File,'rb')
#打开锁定用户信息保存文件
Locked_Info=file(Locked_User_Info_File,'rb')

#从文件中将正常用户信息读取到元组里面
for line in Normal_Info.readlines():
    UserName.append(line.split()[0])
    PassWord.append(line.split()[1])
#从文件中将锁定用户信息读取到元组里面
for line in Locked_Info.readlines():
    LockedUser.append(line.split()[0])
#关闭文件
Normal_Info.close()
Locked_Info.close()

while LoginState:
    InputName = raw_input("请输入登录用户名:")
    #输入用户名在锁定用户里面，直接退出
    if LockedUser.count(InputName)!=0:
        print "当前用户已经被锁定，登录失败"
        break
    #输入用户名不在正常用户里面，判断是否重新进行输入
    elif UserName.count(InputName)==0:
        choice = raw_input("您输入的用户不存在，是否注册用户或退出（y/n）:")
        if choice == "y" or choice == "Y":
            NewPwd1 = raw_input("请输入登录密码:")
            NewPwd2 = raw_input("请再次输入登录密码:")
            if NewPwd1!=NewPwd2:
                print "两次输入的密码不一致，程序退出"
                break
            else:
                #将该用户追加到用户信息文件中
                lines=InputName + " " + NewPwd2 + "\n"
                Normal_Info=file(Normal_User_Info_File,'a+')
                Normal_Info.write(lines)
                Normal_Info.close()
                print "用户录入成功，请退出后重新登录~~~"
                break
        elif choice == "n" or choice == "N":
            LoginState = False
            print "程序退出~~~"
            break
        else:
            continue
    #输入用户在正常登陆用例列表里面
    elif UserName.count(InputName)!=0:
        while count < 3:
            InputPwd = raw_input("请输入登录密码：")
            #输入密码与保存密码不符合
            if InputPwd != PassWord[UserName.index(InputName)]:
                print "输入的密码错误，请重新输入~~~剩余输入次数为:",str(2-count),"次"
                count+=1
                if count==3:
                    print "输入次数超过三次，您的账户已经被锁定"
                    #记录用户在元组中的位置
                    IndexNum= UserName.index(InputName)
                    #将用户从正常用户中移除，并加入到锁定用户元组中
                    LockedUser.append(UserName.pop(IndexNum))
                    #将用户密码从正常用户中移除
                    PassWord.pop(IndexNum)
                    #将正常用户写入文件中
                    Normal_Info=file(Normal_User_Info_File,'w')
                    for i in range(len(UserName)):
                        lines = UserName[i] + " " + PassWord[i]+ "\n"
                        Normal_Info.write(lines)
                    #将锁定用户写入文件中
                    set(LockedUser)
                    Locked_Info=file(Locked_User_Info_File,'w')
                    for i in range(len(LockedUser)):
                        lines = LockedUser[i] + "\n"
                        Locked_Info.write(lines)
                    #关闭文件
                    Normal_Info.close()
                    Locked_Info.close()
                    #设置循环开关为关闭
                    LoginState = False
                    break
            elif InputPwd == PassWord[UserName.index(InputName)]:
                print "登录成功~~"
                LoginState = False
                break   
'''
#!usr/bin/env python 
#_*_ coding: utf-8 _*_
import sys
retry_limit = 3
retry_count = 0
account_file = "D:\\Normal_User_Accounts_Info.txt"
lock_file = "D:\\Locked_User_Account_Info.txt"

while retry_count < retry_limit: #只要重试不超过3次就不断循环
    
    username = raw_input('\033[32;1mUsername:\033[0m')
    lock_check = file(lock_file)  #当用户输入用户名后，打开LOCK 文件 以检查是否此用户已经LOCK了

    for line in lock_check.readlines(): #循环LOCK文件 
        line = line.split()
        if username == line[0]:
            sys.exit('\033[31;1mUser %s is locked!\033[0m' % username ) #如果LOCK了就直接退出
            
    password = raw_input('\033[32;1mPassword:\033[0m')
    
    f = file(account_file,'rb') #打开帐号文件 
    match_flag = False   # 默认为Flase,如果用户match 上了，就设置为 True 
    for line in f.readlines(): 
        user,passwd = line.strip('\n').split() #去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user,passwd两个变量
        if username == user and  password == passwd:  #判断用户名和密码是否都相等
            print 'Match!', username
            match_flag = True #相等就把循环外的match_flag变量改为了True
            break  #然后就不用继续循环了，直接 跳出，因为已经match上了
    f.close()
    if match_flag == False: #如果match_flag还为False,代表上面的循环中跟本就没有match上用户名和密码，所以需要继续循环
        print 'User unmatched!'
        retry_count +=1
    else: 
        print "Welcome login OldBoy Learning system!"

else:
    print 'Your account is locked!'
    f = file(lock_file,'ab')
    f.write(username)
    f.close()
        
        
        
    

'''