kwh = int(input("전기사용량 : "))
month = int(input("월 : ")) 
weather = float(input("기후환경요금 : "))
adjust = float(input("연료비조정요금 : "))

if month == 7 or month == 8:
  if kwh <= 300:
    base_rate = 730
    used_rate = kwh * 73.3
  elif kwh <= 450:
    base_rate = 1260
    used_rate = (kwh-300) * 142.3 + 300 * 73.3
  else:
    base_rate = 6060
    used_rate = (kwh-450) * 210.6 + 150 * 142.3 + 300 * 73.3
else:
  if kwh <= 200:
    base_rate = 730
    used_rate = kwh * 73.3
  elif kwh <= 400:
    base_rate = 1260
    used_rate = (kwh-200) * 142.3 + 200 * 73.3
  else:
    base_rate = 6060
    used_rate = (kwh-400) * 210.6 + 200 * 142.3 + 200 * 73.3


weather_rate = kwh * weather
adjust_rate = kwh * adjust

rate = int(base_rate) + int(used_rate) + weather_rate + adjust_rate
tax = round(rate * 0.1)

fund = int(rate * 0.037 / 10) * 10

bill = rate + tax + fund
bill = int(bill / 10) * 10
print(bill)
