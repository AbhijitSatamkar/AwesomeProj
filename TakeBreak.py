import webbrowser
import time

print("This program is started on" + time.ctime())
for x in range(1, 2):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=EEX_XM6SxmY")
print("This program is ends on" + time.ctime())