def fatorial(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * fatorial(a-1)

def main():
    num = int(input("Fatorial de: "))
    fat = fatorial(num)
    print(f'{num}! = ', end=' ')
    for i in range(num,0,-1):
        print(f"{i}", end=' ')
        if i == 1:
            break
        print('.', end=' ')
    print(f'= {fat}', end=' ')


main()