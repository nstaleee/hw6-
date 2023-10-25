cities = " київ,\nоДеса \nЛьвів.\nжитоМИР,\nуЖгОрОд.....\nХарКІВ \n,слАвУтИч".replace(',','').replace('.','').title().split()
print(cities)
for city in cities:
    print(f'Я \U0001F49E {city}')
pass