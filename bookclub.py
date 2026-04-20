booksBought = int(input("Books purchased this month: "))

if booksBought == 0:
    pts = 0
elif booksBought >= 8:
    pts = 60
elif booksBought >= 6:
    pts = 30
elif booksBought >= 4:
    pts = 15
elif booksBought >= 2:
    pts = 5
else:
    pts = 0

print("Points you earned:", pts)
