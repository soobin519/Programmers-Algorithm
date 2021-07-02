import datetime
def solution(a, b):
    days=['MON','TUE','WED','THU','FRI','SAT','SUN']
    return days[datetime.date(2016,a,b).weekday()]

#datetime클래스 이용하여 date(날짜 정보를 가지는)클래스 객체 사용
#weekday(): 요일 반환 함수 (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
