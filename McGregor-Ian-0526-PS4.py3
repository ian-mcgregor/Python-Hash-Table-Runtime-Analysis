import random
    #for generating random integers
    #randint(self,a,b) returns random int in range a-b including ep's
import matplotlib.pyplot as plt
    #for plotting histogram... below is syntax to print histogram
    #x = [value1, value2, value3,....]
    #plt.style.use('ggplot')
    #plt.hist(x, bins = number of bins)
    #plt.show()
    
    
def hash1(word):
    #hash1
    sum = 0

    for i in range(len(word)):
        for j in range(len(a2z)):
            if (word[i] == a2z[j]):
                sum = sum + j + 1
    sum = (sum%5851)
    return sum
def hash2(word):
    #hash2
    sum = 0
    for i in range(len(word)):
        for j in range(len(a2z)):
            if (word[i] == a2z[j]):
                sum = sum + ((j + 1) * randNumList[j])
    sum = (sum%5851)
    return sum

#list Initializations and Declarations

nameList = []
newNameList = []

hashOneList = []
hashTwoList = []

randNumList = [6605, 5537, 7219, 6371, 2569, 5340, 7666, 8100, 7049, 3275, 1893, 28, 3280, 7087, 4876, 8722, 3340, 2778, 3417, 3270, 4707, 7854, 6743, 3015, 5840, 8399]
a2z = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

#Open File line by line
nameInput = open('dist.all.last.txt', 'r')

#Read only first word from each line and append it to nameList
for line in nameInput:
    nameList.append(line.split(None, 1)[0])
    
#For 50% of the names in original list:
#Access a random index in said list and append it to newNameList
for i in range(44394):
    newNameList.append(nameList[random.randint(0,88798)])
    
#iterate through newNameList and call hash1 on names, then append the return value to hashOneList
for i in range(len(newNameList)):
    word = newNameList[i]
    hashOneList.append(hash1(word))
#iterate through newNameList and call hash2 on names, then append the return value to hashTwoList
for i in range(len(newNameList)):
    word = newNameList[i]
    hashTwoList.append(hash2(word))
    
    
#Graph hash1 histogram
graph1 = plt.figure()
axis1 = graph1.add_subplot()
n, bins, patches = axis1.hist(hashOneList, 300)
axis1.set_title("Hash 1")
axis1.set_xlabel("Hash Index")
axis1.set_ylabel("Number of Strings")

#Graph hash2 histogram
graph2 = plt.figure()
axis2 = graph2.add_subplot()
n, bins, patches = axis2.hist(hashTwoList, 5851)
axis2.set_title("Hash 2")
axis2.set_xlabel("Hash Index")
axis2.set_ylabel("Number of Strings")

#initialize counterList1 and counterList2 values to 0

counterList1 = []
graphCounter = []
counterList2 = []
graphCounter2 = []

#Assign all values in counterList1 to 0
for i in range(300):
    counterList1.append(0)
#iterate through hashOneList and increment counterList1 every time index is encountered
for i in range(len(hashOneList)):
    counterList1[hashOneList[i]] = counterList1[hashOneList[i]] + 1
    graphCounter.append(max(counterList1))
    
    
# #Graph hash1 growth rate
graph3 = plt.figure()
axis3 = graph3.add_subplot()
axis3.plot(range(0, len(graphCounter)), graphCounter)
axis3.set_title("Hash 1 Max Growth Rate")
axis3.set_xlabel("Words Hashed")
axis3.set_ylabel("Longest Chain")    

# #Assign all values in counterList2 to 0
for i in range(5851):
    counterList2.append(0)
#iterate through hashTwoList and increment counterList1 every time index is encountered
for i in range(len(hashTwoList)):
    counterList2[hashTwoList[i]] = counterList2[hashTwoList[i]] + 1
    graphCounter2.append(max(counterList2))
    
# #Graph hash2 growth rate
graph4 = plt.figure()
axis4 = graph4.add_subplot()
axis4.plot(range(0, len(graphCounter2)), graphCounter2)
axis4.set_title("Hash 2 Max Growth Rate")
axis4.set_xlabel("Words Hashed")
axis4.set_ylabel("Longest Chain")

#Need to show #of collisions as a function of #of buckets
collisionA = []    
for a in range(1,300):
    col = 0
    finalForm1 = []
    for b in range(1, len(hashOneList)):
        word = hashOneList[b]
        if(word > 0):
            word = word % a
            if(word in finalForm1):
                 col += 1
            else:
                finalForm1.append(word)
    collisionA.append(col)

collisionB = []
for c in range(1,500):
    col = 0
    finalForm2 = []
    for d in range(1 ,len(hashTwoList)):
        word = hashTwoList[d]
        if(word > 0):
            word = word % c
            if(word in finalForm2):
                 col += 1
            else:
                finalForm2.append(word)
    collisionB.append(col)

# #Graph collisions as a function of l
graph5 = plt.figure()
axis5 = graph5.add_subplot()
axis5.plot(range(0, len(collisionA)), collisionA)
axis5.set_title("Collisions as a function of L")
axis5.set_xlabel("Size of L")
axis5.set_ylabel("Number of Collisions")  

# #Graph collisions as a function of L
graph6 = plt.figure()
axis6 = graph6.add_subplot()
axis6.plot(range(0, len(collisionB)), collisionB)
axis6.set_title("Collisions as a function of L")
axis6.set_xlabel("Size of L")
axis6.set_ylabel("Number of Collisions")    