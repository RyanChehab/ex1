while True:
    try:
        n= int(input("Please enter a number: "))
        break
    except ValueError:
        print("wrong input!")

counter=1

for _ in range(n):
    print('*' * counter)
    counter+=2

counter-=4
for _ in range(n):
    print('*' * counter)
    counter-=2