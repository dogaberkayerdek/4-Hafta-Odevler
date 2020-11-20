def grupla(liste):
    liste1=[[],[]]
    for i in range (len(liste)):
        if liste[i] % 2 == 0:
            liste1[1].append(liste[i])
        else:
            liste1[0].append(liste[i])
    print(liste1)
grupla(liste=[1,2,3,4,5,6,7,8,9])
