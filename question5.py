names = []
numb = []

for i in range(5):
   name = input("Enter a name: ")
   number = int(input("Enter a number: "))
   names.append(name)
   numb.append(number)

data = []
for i in range(5):
   data.append([names[i], numb[i]])

dict = {}
for item in data:
   dict[item[0]] = item[1]

sorted_items = sorted(dict.items(), key=lambda x: x[1])
sorted_dict = dict(sorted_items)

print(sorted_dict)
