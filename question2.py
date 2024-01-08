print("Input 5 names")
lst = []
a = 0

for i in range(1):
    lst.append(input())
    lst[i].strip()

lst.sort()


for i in range(1):
    for j in lst[i]:
        a += 1
        if(j != ' '):
            pass
        else:
            k = lst[i]
            substring_to_upper = k[0:a]
            uppercase_substring = substring_to_upper.upper()
            k = uppercase_substring + k[a:]

            substring_to_lower = k[a:]
            lowercase_substring = substring_to_lower.lower()
            k = k[0:a] + lowercase_substring
            lst[i] = k
            
            lst[i] = lst[i].replace(" ", "")
            
    a = 0


for i in range(1):
    p = len(lst[i]) - 2
    k = lst[i]
    print(k[0:p])


    
    
      