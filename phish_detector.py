import os, platform, time, sys
print('\n\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Checking For Update...')
os.system('git pull')
print('Follow my facebook')
os.system("https://www.facebook.com/MrT4N.Official")
bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m You are 64 Bit user')
    time.sleep(3)
    os.system("clear") 
    import detector
elif bit == '32bit':
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156mSorry You are 32 Bit user')
    time.sleep(3)
    os.system("clear")
    
else:
    print("Sorry")
