import time

x = 0

t_start = time.time()   # UNIXエポックからの経過時間（秒）を取得
                        # 1970年1月1日午前0時0分0秒（UTC）

for i in range(100000):
    x += i
    
t_end = time.time()

t_delta = t_end-t_start

print("t_start", t_start)
print("t_end", t_end)
print("t_delta", t_delta)