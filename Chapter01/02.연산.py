# 1. 대입연산


# 2. 산술연산
x = 5
y = 2
print( x + y)
print( x - y)
print( x * y)
print( x / y)
print( x // y)  # 몫
print( x % y)  # 나머지
print( x ** y) # 제곱
print('제곱값:', 5 ** 4) 

# 문자열 연산
tag1 = "#동해물과"
tag2 = "#백두산이"
tag = tag1 + tag2
print(tag)

print('"(((동해물과 백두산이)))"')

# 1. 비교연산
print("- 비교연산 문제")
print(2 > 3) # False
print(15 < 30) # True
print(1.5 >= 0) # True
print(3 <= 3) # True
print("팙팗팚" == "팙팗팗") # False
print("1111111111111111111" != "111111111111111111") # True

# 2. 논리연산
print("- 논리연산 문제")
print(4 < 6 and 10 >= 10) # True and True -> True
print("포기하지말아요" != "포기하지말아요" or "나는 할 수 있다" == "나는 할 수 있다") # False or True -> True
print(not 5==5) # not True -> False

# 3. 멤버십 연산
print("- 멤버십 연산 문제")
print("a" in "abc") # 포함되어 있다면 True
print("d" not in "abc") # 포함되어 있지 않다면 True