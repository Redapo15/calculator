level2 = 0
lvl2 = []
while True:
    str1 = str(input("give calculation to solve:  "))
    li = list(str1.split(" "))
    #print(li)
    for i in range(1,len(li)):
        
        if i%2!=0:
            if li[i] == "*":
                level2 += 1
            elif li[i] == "/":
                level2 += 1
    if level2 > 0:
        print("test")
    else:
        sum = int(li[0])
        for a in range(2,len(li)):
            if a%2==0:
                if li[a-1]=="+":
                    sum += int(li[a])
                elif li[a-1]=="-":
                    sum -= int(li[a])
    print(f"answer: {sum}")