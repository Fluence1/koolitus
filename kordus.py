#while
#for

#index=100
#teineIndex=10
#print(index)

#while index<=10:
   #print(teineIndex)
   #index+=1
    #teineIndex+=100
    #if index==5:
        #print(index)
        #continue
        #break #jätab koodi pooleli
#else:
    #print("Condition is False")

#fruits=["apple","banana","cherry"]
#for x in fruits: #for x in "auto": kirjutab tähthaaval a u t o (käib kõik elemendid väiksemast suuremani läbi)
    #pass #jätab kogu loopi vahele

#for x in range(2,60,3): #nr 6 on arvud 0-5
    #print(x)
#else:
    #print("Finished!")

#for x in range(11):
    #for x in range(11):
        #print(x)

#Anname ette mingi listi objekte
#kasutaja sisestab mingi elemendi sinna listi
#for x in range(LISTIPIKKUS)
#   LIST[INDEX]
#print(LIST[ELEMENT])
#mitmes see listis on  /// LISTINIMETUS.INDEX(ELEMENT)
# vaja läheb 2 loopi, üks listi näitamiseks, teine selle otsimiseks 
loomad=["panda","kilpkonn","siga","koer","kass"]
for x in loomad:
    print(x)

vastus=input("Vali mingi loom - ")
for x in loomad:
    print(loomad.index(vastus))  
    

#saaks panna ka 
#for x in loomad:
    #if x==vastus:
        #vastus=testlist.index(valik)
        #print(vastus)


    
