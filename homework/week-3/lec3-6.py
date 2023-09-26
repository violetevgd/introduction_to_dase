score = int(input())
if score < 60:
    print("不合格")
elif score >= 60 and score <= 74:
    print("合格")
elif score >= 75 and score <= 89:
    print("良好")
else:
    print("优秀")