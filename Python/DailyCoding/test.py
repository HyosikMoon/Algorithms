def intro(*num, **data):
    print("\nData type of non-keyward argument:",type(num))
    print("\nData type of keyward argument:",type(data))

    if num != None:
        for n in num:
            print('nums: ', n)

    for key, value in data.items():
        print("{} is {}".format(key,value))

    print('{} is {}'.format(list(data.items())[2][0], list(data.items())[3]))

intro(1,2,3, Firstname="Sita", Lastname="Sharma", Age=22, Hello=None, Phone=1234567890)
