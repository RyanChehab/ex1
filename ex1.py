while True:
    try:
        n= int(input("Please enter a positive number: "))
        if n>0:
            break
    except ValueError:
        print("wrong input!")

counter=1
width = n*2
for _ in range(n):
    print(('*' * counter).center(width))
    counter+=2

counter-=4
for _ in range(n):
    print(('*' * counter).center(width))
    counter-=2