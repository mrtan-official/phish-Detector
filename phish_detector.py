import os, platform, time, sys

print('\n\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Checking For Update...')
os.system('git pull')


is_android = 'termux' in sys.prefix or 'Android' in platform.version()
is_linux = platform.system() == "Linux" and not is_android

if is_android:
    print('Follow my facebook')
    os.system("xdg-open https://www.facebook.com/MrT4N.Official")
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Termux Detected (64 Bit)')
    time.sleep(3)
    os.system("clear")
    import detector
    time.sleep(3)

elif is_linux:
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Linux Detected')
    time.sleep(3)
    os.system("clear")
    import phish_detector
    time.sleep(3)

else:
    print("Sorry, your device is not supported.")
