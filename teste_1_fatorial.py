num = int(input("Digite o valor de n: "))
if num != 0:
    fat = num
else:
    fat = 1
while num > 1:
    num = num - 1
    fat = fat * num
print(fat)
