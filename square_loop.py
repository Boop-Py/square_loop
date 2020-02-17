try:
    limit = int(input("What is your limit? "))   
except ValueError:
    print("Nope. Try again.")      
else:
    for i in range(0, limit):
        squared_i = i*i
        print(i, squared_i)
        if squared_i >= 200:
            print("You've reached 200 or more. Ending loop.")
            break
