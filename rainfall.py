rainT = 0
monthCount = 0

numYears = int(input("How many years of data do you want to enter? "))

for y in range(numYears):
    print("\nYear", y + 1)

    for m in range(12):
        rain = float(input(f"Rainfall in inches for month {m + 1}: "))
        rainT += rain
        monthCount += 1

avgRain = rainT / monthCount


print("Months counted:", monthCount)
print("Total rainfall:", rainT)
print("Average per month in inches:", round(avgRain, 2))
