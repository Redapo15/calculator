while True:
    str1 = str(input("give calculation to solve:  "))
    li = list(str1.split(" "))
    sum = int(li[0])
    for a in range(2,len(li)):
        if a%2==0:
            if li[a-1]=="+":
                sum += int(li[a])
            elif li[a-1]=="-":
                sum -= int(li[a])
    print(f"answer: {sum}")