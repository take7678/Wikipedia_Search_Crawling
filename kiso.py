print("小問題１")
nums = [1, 2, 3, 4, 5]

for n in nums:
    if n % 2 == 0:
        print(n)

print("小問題２")
names = ["田中", "佐藤", "鈴木"]

for n in names:
    if n == "佐藤":
        print(n)

print("小問題３")
nums3 = [3, 7, 2, 9, 5]
max = 0

for n in nums3:
    if n > max:
        max = n
print(max)

print("小問題４")
users = ["Taro", "Jiro", "Saburo"]
new_users = []

for n in users:
    a = n + "さん"
    new_users.append(a)

print(new_users)

print("小問題５")
words = ["Python", "Java", "AI"]

for n in words:
    search = n + "を検索します"
    print(search)

print("中問題１")
nums_1 = [1, 2, 3, 4, 5]

for n in nums_1:
    if n % 2 == 1:
        a_1 = n * 2
        print(a_1)

print("中問題２")
nums_2 = [3, 7, 2, 9, 5]
sum_2 = 0
count_2 = 0
for n in nums_2:
    sum_2 += n
    count_2 += 1

avg_2 = sum_2 / count_2

for m in nums_2:
    if m > avg_2:
        print(m)

print("中問題３")
users_3 = ["Taro", "Jiro", "Saburo"]
new_user_3 = []

for n in users_3:
    a_3 = n.upper()
    new_user_3.append(a_3)
print(new_user_3)

print("中問題４")
words_4 = ["Python", "Java", "AI"]

for n in words_4:
    if len(n) > 5:
        print(n)

print("中問題５")
scores_5 = {"A": 50, "B": 80, "C": 70}

for name, score in scores_5.items():
    if score >= 80:
        print(name, score)

print("中問題６")
nums_6 = [10, 3, 6, 8, 2]

max_6 = 0
min_6 = 0

for n in nums_6:
    if max_6 == 0 and min_6 == 0:
        max_6 = n
        min_6 = n
    elif n > max_6:
        max_6 = n
    elif n < min_6:
        min_6 = n
print(max_6,min_6)

print("総合問題")

scores_7 = {
    "A": 50,
    "B": 80,
    "C": 70,
    "D": 90
}

sum_7 = 0
count_7 = 0
avg_7 = 0

for name, score in scores_7.items():
    sum_7 += score
    count_7 += 1
avg_7 = sum_7 / count_7

for name, score in scores_7.items():
    if score > avg_7:
        print(name, score)
