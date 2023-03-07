level2 = 0
lvl2 = []
ip = []
summ = 0
while True:
    str1 = str(input("give calculation to solve:  "))
    li = list(str1.split(" "))
    #print(li)
    for i in range(len(li)):
        print(i)
        if i%2!=0:
            if li[i] == "*":
                res = float(li[i-1])*float(li[i+1])
                del(li[i-1])
                del(li[i+1-1])
                li[i-1]=res
            elif li[i] == "/":
                res = float(li[i-1])/float(li[i+1])
                del(li[i-1])
                del(li[i+1-1])
                li[i-1]=res  
    else:
        summ = float(li[0])
        for a in range(2,len(li)):
            if a%2==0:
                if li[a-1]=="+":
                    summ += float(li[a])
                elif li[a-1]=="-":
                    summ -= float(li[a])
    print(f"answer: {summ}")
    level2=0
    lvl2=[]
    ip=[]
    summ=0
    li=[]