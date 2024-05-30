import random
print("사칙연산 프로그램")
op = input("덧셈 1,뺄셈 2, 곱셈 3, 나눗셈 4(종료시 enter):")

while True:
    a = random.randint(1,10)
    b = random.randint(1, 10)

    if op == "1":
        result1 = int(input(f"{a}+{b}="))
        if result1 == a+b:
            print("정답입니다.")
        else:
            print("틀렸습니다.")
    elif op == "2":
        result2 = int(input("f{a}-{b}="))
        if result2 == a-b:
            print("정답입니다.")
        else:
            print("틀렸습니다.")
    elif op == "3":
        result2 = int(input("{a}*{b}="))
        if result2 == a*b:
            print("정답입니다.")
        else:
            print("틀렸습니다.")
    elif op == "4":
        result2 = int(input(f"{a}/{b}="))
        if result2 == a/b:
            print("정답입니다.")
        else:
            print("틀렸습니다.")
    else:
        print("error")
