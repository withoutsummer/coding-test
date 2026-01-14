def solution(a, b):
    # 인덱스 1~12까지만 사용
    days_of_month_list = [0,31,29,31,30,31,30,31,31,30,31,30,31]

    # 인덱스 1~7 사용
    day_of_week_list = ["","SUN","MON","TUE","WED","THU","FRI","SAT"]
    first_idx = 6

    prev_month_days = 0
    totals = 0
    
    for i in range(1,a):
        prev_month_days += days_of_month_list[i]
    
    totals = prev_month_days + b
    cur_idx = totals % 7 + (first_idx - 1) if totals % 7 + (first_idx - 1) <= 7 else (totals % 7 + (first_idx - 1)) % 7
    
    return day_of_week_list[cur_idx]