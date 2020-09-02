
# alist=[x for x in range(10)]
# print(alist)

# t=(x for x in range(10000))
#
# print(next(t))

#生成器函数，有yield的函数
def my_gen():
    i=0
    while i <100000000:
        yield i
        i+=1

t=my_gen()
for i in range(10):
    print(next(t))