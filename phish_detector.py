import os, platform, time, sys

print('\n\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Checking For Update...')
os.system('git pull')

print('Follow my facebook')
os.system("xdg-open https://www.facebook.com/MrT4N.Official")

is_android = 'termux' in sys.prefix or 'Android' in platform.version()
is_linux_pc = platform.system() == "Linux" and not is_android

if is_android:
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Termux Detected (64 Bit)')
    time.sleep(3)
    os.system("clear")
    import detector

elif is_linux_pc:
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Linux PC Detected')
    time.sleep(3)
    os.system("clear")
    import phish_detector

else:
    # Onno kono OS (Windows/Mac) hole
    print("Sorry, your device is not supported.")
