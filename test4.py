lista = ['taskbar', 'main.py - vocal-asistent - visual studio code', 'powerpoint (produs nelicențiat)', 'word (produs nelicențiat)', 'new tab - personal - microsoft\u200b edge', 'notepad', '', 'program manager']

powerpoint = "powerpoint (produs nelicențiat)"
word = "word (produs nelicențiat)"

cuvant_cheie = "produs nelicențiat"

# if powerpoint in lista:
#     print("exista")
#     powerpoint = powerpoint.split()[0]
#     print(powerpoint)
#     print(lista)
i=0

while i < len(lista):
        # if(lista[i] == "powerpoint (produs nelicențiat)"):
        #     lista[i] = "powerpoint"
        #     print("am gasit powerpoint")

        # if(lista[i] == "word (produs nelicențiat)"):
        #     lista[i] = "word"
        #     print("am gasit word")
        if cuvant_cheie in lista[i]:
                lista[i] = lista[i].split()[0]
                print("exista")
        
        i=i+1

print(lista)

# -----------------------------------------

