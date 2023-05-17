from datetime import datetime, timedelta 

# 현재 시각을 구하고 특정 형식으로 출력하기 
t = datetime.now()
fmt = t.strftime('%Y년%m월%d일 %H시%M분%S초')
print(fmt)

# 날짜 시간 표시 
t2 = datetime(2023, 1, 1)
print(t2.strftime('%Y년 %m월 %d일'))

# d-day를 지정 
dday = datetime(2025, 4, 13)
now = datetime.now()        # 오늘 날짜를 지정 
delta = dday - now 
print('앞으로 ' + str(delta.days + 1) + '일 남았습니다.')

# 남은 시간 계산하기 
sleep_t = datetime(2023, 1, 1, 22, 0 , 0)
wakeup_t = datetime(2023, 1, 2, 8, 30 , 0)

delta2 = wakeup_t - sleep_t
sec = delta2.seconds     # 수면 시간을 초로 환산 
hours = sec / (60 * 60)

print("총 수면시간은 " + str(hours) + "입니다.")

# n일후 날짜 조사하기 
base_t = datetime(2025, 2, 27)
t3 = base_t + timedelta(days=3)
print(t3.strftime('%Y년 %m월 %d일'))