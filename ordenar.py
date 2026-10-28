nums = input('ingrese 3 números (separelos por ","): ').split(',')

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])


if a > b:
    if a > c:
        if b > c:
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        print(b,a,c)
elif a > c:
    if b > c:
        print(c,a,b)
    else:
        print(b,c,a)
elif b> c:
    print(a,c,b)

else: print(a,b,c)
