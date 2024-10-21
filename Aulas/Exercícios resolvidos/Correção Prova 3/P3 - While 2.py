time1, time2 = map(int, input().split())

v_time1 = 0
v_time2 = 0

while time1 != time2:
    
    if time1 > time2:
        v_time1 = v_time1 + 1
    else:
        v_time2 = v_time2 + 1
    
    
    time1, time2 = map(int, input().split())

if v_time1 >= v_time2:
    print("Time 1")
else:
    print("Time 2")
    
