import os, platform, time, sys

print('\n\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Checking For Update...')
os.system('git pull')

print('Follow my facebook')
os.system("xdg-open https://www.facebook.com/MrT4N.Official")

# Check korchi eta ki Android (Termux) naki normal Linux
is_android = 'Android' in platform.version() or 'termux' in sys.prefix

if is_android:
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Termux Detected (64 Bit)')
    time.sleep(3)
    os.system("clear")
    import detector
else:
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Linux PC Detected')
    time.sleep(3)
    os.system("clear")
    import phish_detector
