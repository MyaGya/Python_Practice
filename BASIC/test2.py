# Q1

a = "Life is too short, you need naver_AI_BOOSTCAMP"
if "wife" in a:
    print("wife")
elif "naver_AI_BOOSTCAMP" in a and "you" not in a:
    print("naver_AI_BOOSTCAMP")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# Q2
roof = 0
result = 0
while roof <= 1000:
    if roof % 3 == 0:
        result += roof
    roof += 1

print(result)

# Q3

roof = 1;
while roof < 6:
    print("*"*roof)
    roof += 1



#Q4


for number in range (1,101):
    print(number)

#Q6
numbers = [1, 2, 3, 4, 5]
result = [s for s in numbers if s % 2 == 1]

print(result)