List = []
n = int(input("Enter the limit:"))
print("Enter the numbers:")
i = 0
while i<n:
    num = int(input())
    List.append(num)
    i+=1
print(f" The original list is :{List}")


max = List[0]
sec_max = List[0]
third_max = List[0]

for i in List:
    if i >max:
        third_max=sec_max
        sec_max=max
        max=i
    elif i>sec_max:
        third_max=sec_max
        sec_max=i
    elif i>third_max:
        third_max=i
print(f"The Third largest number is:{third_max}")