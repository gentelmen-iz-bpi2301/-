import requests
city = input()
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid=6f29939a343ff1b4723d94c660f344e3"
weather = requests.get(url).json()
t = weather['main']['temp']
feels = weather['main']['feels_like']
atmospheric_pressure = weather['main']['pressure']
wind = weather['wind']['speed']
h=weather['main']['humidity']
print('Сейчас в городе',city ,str(t) ,'градусов, а ощущается как',str(feels))
print('Атмосферное давление',str(round(atmospheric_pressure*0,750064)),'мм рт.ст.')
print('Скорость ветра',str(wind),'м/с')
print('Влажность воздуха на данный момент',str(h),'%')