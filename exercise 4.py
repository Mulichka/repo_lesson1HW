# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = input('Введите целое положительное число: ')
i = len(num)
list_num = []
while i != -1:
    list_num.append(int(num[i-1]))
    i -=1
list.sort(list_num)
result = list_num[-1]
print(f'Наибольшая цифра в Вашем числе: {result}')

# мне нравится через for:
# num = input('Введите целое положительное число: ')
# list_num = []
# for nums in num:
#    list_num.append(int(nums[0]))
# list.sort(list_num)
# result = list_num[-1]
# print(f'Наибольшая цифра в Вашем числе: {result}')