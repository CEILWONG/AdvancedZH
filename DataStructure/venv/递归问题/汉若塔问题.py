
def harot(hight,fromit,withit,toit):
    if hight>=1:
        harot(hight-1,fromit,toit,withit)
        print("move %d form %d to %d"%(hight,fromit,toit))
        harot(hight-1,withit,fromit,toit)



harot(4,1,2,3)