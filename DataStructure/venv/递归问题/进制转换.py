
#任意进制的转换的确有点牛逼了,10进制的转移成任意进制

def tostring(n,base):

    Str="0123456789ABCDEF"

    if n<base:
        return Str[n]
    else:
        return tostring(n//base,base)+Str[n%base]


def main():

    n=int(input("input it:"))

    x=tostring(n,16)

    print(x)

while True:

    main()