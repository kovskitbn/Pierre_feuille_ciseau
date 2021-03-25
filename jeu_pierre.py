import random
import matplotlib.pyplot as plt
n = int(input('nombre de coup : '))
l_p1 = list()
l_p2 = list()
l_nul = list()
for k in range(1,n+1):
    coup = {'Feuille':'Pierre', 'Sciseau':'Feuille', 'Pierre':'Sciseau'}
    p1 = 0 
    p2 = 0 
    i=0
    nul = 0  
    while i!= k:  
        x2 = str(random.choice(list(coup.keys())))
        x1 = str(random.choice(list(coup.keys())))
        if coup[x1]==x2:
            p1+=1
        elif coup[x2]==x1:
            p2+=1
        else:
            nul += 1
        i+=1
    l_nul.append(nul)
    l_p1.append(p1)
    l_p2.append(p2)    
l = list(i for i in range(1,n+1))
plt.suptitle("Gain et Nul en fonction du nombre de coups {}".format(n))
plt.subplot(2,1,1)
plt.plot(l,l_p1,'r')
plt.plot(l,l_p2, 'g')
plt.subplot(2, 1, 2) 
plt.bar(l,l_nul )

plt.show()








     
    