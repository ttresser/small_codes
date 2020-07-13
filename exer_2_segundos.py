sec0 = int(input("Por favor, entre com o número de segundos que deseja converter: "))

day = sec0 // 86400
sec2 = sec0 % 86400
hr = sec2 // 3600
sec3 = sec2 % 3600
minu = sec3 // 60
sec = sec3 % 60

print(day, "dias,", hr, "horas,", minu, "minutos e", sec, "segundos.")
