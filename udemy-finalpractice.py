def list_check(mylist):
    for item in mylist:
        if isinstance(item,list):
            continue
        else:
            return False
    return True


#print(list_check([[],[1],[2,3], (1,2)])) # False
#list_check([1, True, [],[1],[2,3]]) # False
#list_check([[],[1],[2,3]]) # True

def includes(collection, value, search_index=0):
    if isinstance(collection, str) or isinstance(collection, list):
        return value in collection[search_index:]
    else:
        return value in collection.values()

T = includes([1, 2, 3], 1,2) # True
print(T)


def range_in_list(mylist, start = 0, end = -1):
    if end >= len(mylist):
        end = -1
    return sum(i for i in mylist[start:end])

print(range_in_list([1,2,3,4],0,2))



def reverse_vowels(mystr):
    v_list = []
    for c in mystr:
        if c in "aeiouAEIOU":
            v_list.append(c)
    v_list = v_list[::-1]
    print(v_list)
    idx = 0
    newlist = []
    for c in mystr:
        if c not in "aeiouAEIOU":
            newlist.append(c)
        else:
            newlist.append(v_list[idx])
            idx = idx + 1
    return "".join(newlist)

print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"


def once(func):
    msg = []
    func.is_called = False # 函数也是一个object 可以设置其property

    def innerfunc(*args):
        if not(func.is_called):
            func.is_called = True
            return func(*args)

    return innerfunc

def add(a,b):
    return a+b

oneAddition = once(add)
print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None


def next_prime():
    prime = 2;
    while True:
        yield prime
        prime = findnextprime(prime)

def findnextprime(prime):
    while True:
        prime = prime + prime%2 +1 # 跳过中间能被2整除的
        flag = True
        for i in range(2,prime):
            if prime % i == 0:
                flag = False
                break;
        if flag:
            return prime

primes = next_prime()
print([next(primes) for i in range(25)])
