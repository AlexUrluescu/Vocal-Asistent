
from pywinauto import Desktop
import win32gui

def loadwindowslist(hwnd, topwindows):
	topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))


def findandshowwindow(swinname, bshow, bbreak):
	topwindows = []
	print(f"Aic este {topwindows}")
	win32gui.EnumWindows(loadwindowslist, topwindows)
	print(f"Aici 1.2 este {topwindows}")
	for hwin in topwindows:	
		sappname=str(hwin[1])
		if swinname in sappname.lower():	
			nhwnd = 25101150
			print(">>> Found: " + str(nhwnd) + ": " + sappname)
			if(bshow):
				win32gui.ShowWindow(nhwnd,5)
				win32gui.SetForegroundWindow(nhwnd)
			if(bbreak):
				break


lista = []
app = "notepad"

windows = Desktop(backend="uia").windows()

for w in windows:
    lista.append(w.window_text().lower())
    print(w.window_text())

print(lista)

if app in lista:
    findandshowwindow("notepad", True, True)
    print("exist")

else:
    print("doesn't exist")


