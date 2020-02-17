limit = input("What is your limit? ")

for i in range(0, limit):
    squared_i = i*i
    print(i, squared_i)
    if squared_i >= 200:
        print("You've reached 200 or more. Ending loop.")
        break
