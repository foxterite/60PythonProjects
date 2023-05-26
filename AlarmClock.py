import time
from playsound import playsound

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            playsound('alarm.mp3')  # Replace 'alarm_sound.mp3' with your preferred audio file
            break

# Prompt the user to input the alarm time
alarm_time = input("Enter the time of alarm to be set (in HH:MM:SS format): ")

# Call the set_alarm function with the provided alarm time
set_alarm(alarm_time)
