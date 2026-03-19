import os, platform, time, sys

print('\n\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Checking For Update...')
os.system('git pull')

print('Follow my facebook')
os.system("xdg-open https://www.facebook.com/MrT4N.Official")

# Architecture ebong OS check kora
bit = platform.architecture()[0]
os_type = platform.system()

if bit == '64bit':
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m You are 64 Bit user')
    time.sleep(3)
    os.system("clear")
    import detector
    
elif os_type == 'Linux':
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Linux Device Detected')
    time.sleep(3)
    os.system("clear")
    import phish_detector

else:
    print("Sorry, unsupported system.")
