
from pywinauto import Desktop

lista = []

windows = Desktop(backend="uia").windows()

for w in windows:
    lista.append(w.window_text())
    print(w.window_text())

print(lista)