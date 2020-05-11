#Перевод времени из секунд
time = int(input('Сколько секунд хотите перевести во время: '))
hour = int(time / 3600)
minute = int(time / 60 - hour * 60)
sec = int(time - minute * 60 - hour * 3600)
print(f'Время {hour} : {minute} : {sec}')