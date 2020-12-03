numero_partecipanti = int(input("Numero dei partecipanti: "))
partecipanti = []
valori = []
for i in range(numero_partecipanti):
    a = input("Nome partecipante: ")
    b = float(input("Valore del lancio in m: "))
    partecipanti.append(a)
    valori.append(b)
    valore_maggiore = max(valori)
    #dizionario = {"a":"valore_maggiore"}
print("Il valore del lancio maggiore è: " + str(valore_maggiore)
