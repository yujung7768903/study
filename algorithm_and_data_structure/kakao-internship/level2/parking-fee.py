# 주차 요금 계산 / https://programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
import math

def cal_parking_time(in_time, out_time):
    in_hour, in_min = map(int, in_time.split(":"))
    out_hour, out_min = map(int, out_time.split(":"))
    return (out_hour - in_hour) * 60 + (out_min - in_min)

def cal_parking_fee(fees, parking_time):
    if parking_time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((parking_time - fees[0]) / fees[2]) * fees[3]

def solution(fees, records):
    answer = []
    dict_car_record = defaultdict(list) # key: 차량 번호, value: [입차 시각, 출차 시각]

    for record in records:
        time, car_number, in_out_record = list(record.split())
        dict_car_record[car_number].append(time)
        print(dict_car_record)
            
    for key, value in dict_car_record.items():
        parking_time = 0
        # 입차 이후 출차 기록이 없을 경우(= value 길이가 홀수 인 경우) 23:59 추가
        if len(value) % 2 == 1:
            dict_car_record[key].append('23:59')
            print(dict_car_record)

        for i in range(0, len(value), 2):
            print(f"i: {i}")
            parking_time += cal_parking_time(value[i], value[i + 1])
            parking_fee = cal_parking_fee(fees, parking_time)
            print(f"주차 시간: {parking_time}, 주차 요금: {parking_fee}")
            dict_car_record[key] = parking_fee

    answer = [value[1] for value in sorted(dict_car_record.items())] 
    print(answer)

    return answer

# ex_fees = [180, 5000, 10, 600]
# ex_records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
ex_fees = [1, 461, 1, 10]
ex_records = ["00:00 1234 IN"]

solution(ex_fees, ex_records)