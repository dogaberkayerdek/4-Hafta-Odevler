def sırala(liste):
    for i in range (len(liste)):
        for j in range (i+1,len(liste)):
            if liste[i] > liste[j]:
                temp=liste[j]
                liste[j]=liste[i]
                liste[i]=temp



    print("Listemizin sıralı hali" , liste )
        
        
