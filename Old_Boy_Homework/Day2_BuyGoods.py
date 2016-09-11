# -*- coding: utf-8 -*- 

def InputInfo(info=1):
    if info == 1:
        printinfo = '            请输入员工工资:'
    else:
        printinfo = '            请输您要购买的商品编号:'
    
    while True:
        num=raw_input(printinfo)
        if num.isdigit():
            return  int(num)
            break
        else:
            print "您输入的内容错误，请重新输入~~~"

def GoodsInfo():     
    GoodsInfo='''
    **************商  品  价  格  列  表**************
            1、小汽车                                      价格:30000
            2、摩托车                                      价格:8000
            3、苹果电脑                                  价格:6000
            4、电视                                          价格:4000
            5、自行车                                      价格:3000
            6、手机                                          价格:1500
            7、电饭煲                                      价格:500
            8、电风扇                                      价格:300
         '''
    print GoodsInfo
    


def ChooseGoods(wages,Goods_Num):
    if Goods_Num == 1 and wages >= 30000:
        print "购买成功"
        residue = wages - 30000
        return (residue,'小汽车 ')
    elif Goods_Num == 2 and wages >= 8000:
        print "购买成功"
        residue = wages - 8000
        return (residue,'摩托车')
    elif Goods_Num == 3 and wages >= 6000:
        print "购买成功"
        residue = wages - 6000
        return (residue,'苹果电脑 ')
    elif Goods_Num == 4 and wages >= 4000:
        print "购买成功"
        residue = wages - 4000
        return (residue,'电视 ')
    elif Goods_Num == 5 and wages >= 3000:
        print "购买成功"
        residue = wages - 3000
        return (residue,'自行车')
    elif Goods_Num == 6 and wages >= 1500:
        print "购买成功"
        residue = wages - 1500
        return (residue,'手机 ')
    elif Goods_Num == 7 and wages >= 500:
        print "购买成功"
        residue = wages - 500
        return (residue,'电饭煲 ')
    elif Goods_Num == 8 and wages >= 300:
        print "购买成功"
        residue = wages - 300
        return (residue,"电风扇")
    else:
        print("您的余额不足以购买此商品~~~")
        return (wages,0)



def BuyGoods(Wages,goodlist):
    while True:
        #打印可购买物品列表
        GoodsInfo()
        #选择购买的物品
        Goods = InputInfo(2)
        residue = ChooseGoods(Wages,Goods)
        Wages = residue[0]
        print residue[1]
        if residue[1] != 0:
            goodlist.append(residue[1])
        print '您当前的余额为：',Wages
        chooes = raw_input('是否继续购买（y/n）:')
        if chooes == "y" or chooes == "Y":
            continue
        elif chooes == "n" or chooes == "N":
            break
    
    print '您的购物车包含以下物品：'
    for i in goodlist:
        print i
        
        
if __name__ == "__main__":
    #用户存放已经购买了的商品
    goodslist=[]  
    #获取员工工资
    Wages = InputInfo()
    
    BuyGoods(Wages,goodslist)
    