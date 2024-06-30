number = int(input("The Number: "))

for result in range(number):
    if result == -1:
        break

    print(result)
    if result <= 10:
        continue
    
    print(result)
