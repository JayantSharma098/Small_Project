import datetime
import time
import winsound  

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}...")

while True:

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    

    if current_time == alarm_time:
        print("Wake up! ⏰")
        
        for i in range(10):
            winsound.Beep(1000, 1000)  
        break

    time.sleep(1)
