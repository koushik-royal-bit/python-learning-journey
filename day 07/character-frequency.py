v= input('enter string:').lower()
for char in v:
    count =0
    for c in v:
        if char in c:
            count+=1
    print(f'{char} : {count}')        