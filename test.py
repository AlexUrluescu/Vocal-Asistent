
from pywinauto import Desktop

lista = []
app = "Notepad"

windows = Desktop(backend="uia").windows()

for w in windows:
    lista.append(w.window_text().lower())
    print(w.window_text())

print(lista)

if app in lista:
    print("exist")

else:
    print("doesn't exist")
