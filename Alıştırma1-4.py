def grupla(liste):
    liste1=[[],[]]
    for i in range (len(liste)):
        if liste[i] % 2 == 0:
            liste1[1].append(liste[i])
        else:
            liste1[0].append(liste[i])
    print(liste1)

