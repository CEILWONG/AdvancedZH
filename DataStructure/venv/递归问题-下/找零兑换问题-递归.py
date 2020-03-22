
#寻找不管是那种货币体系，肯定能找到一种最优算法的算法



def retnum(coinlist,change):


    mincoins=change
    if change in coinlist:
        return 1
    else:
        for i in [c for c in coinlist if c<change]:
            numcoin=1+retnum(coinlist,change-i)

            if numcoin<mincoins:
                mincoins=numcoin

        return mincoins

print(retnum([1,5,10,25],63))


#上面那个算法的效率很低，根本原因在于里面有太多的重复计算；
#这种递归其实就是用试了很多种情况，所谓的递归思想只是让我写了尽可能少的代码
#可以在原有递归的思想上用查表的方式来减少计算次数
#下面是改进算法
'''


def retnum(coinlist,change,knowlist):
    mincoins=change

    if change in coinlist:
        knowlist[change]=1
        return 1
    elif knowlist[change]>0:
        return knowlist[change]
    else:
        
        for i in (c for c in coinlist if c<change):
            numcoins=1+retnum(coinlist,change-i,knowlist)
            
            if numcoins<mincoins:
                mincoins=numcoins
                knowlist[change]=mincoins
        return mincoins


'''
