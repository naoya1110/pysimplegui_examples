import keyboard
import time

while True:
    key = keyboard.read_key()
    
    if key=="a":
        print("aを押しました。")
    
    if key=="q":
        print("qを押しました。終了！")
        break
    
    time.sleep(0.2)