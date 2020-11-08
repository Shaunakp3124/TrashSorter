with open("Unsorted.txt", "r") as unsorted, open("Compost.txt", "r") as compost, open("Recycle.txt", "r") as recycle, open("Trash.txt", "r") as trash:
    UnsortedArray = []
    CompostArray = []
    RecycleArray = []
    TrashArray = []
    for i in unsorted:
        UnsortedArray.append(i.strip())
    for i in compost:
        CompostArray.append(i.strip())

    for i in recycle:
        RecycleArray.append(i.strip())

    for i in trash:
        TrashArray.append(i.strip())

#print(UnsortedArray)
#print(CompostArray)
#print(RecycleArray)
#print(TrashArray)
# Now we will check every element in unsorted array and see if it is in another array
TanswerArray = []
CanswerArray = []
RanswerArray = []


for unsortedValue in UnsortedArray:
    if unsortedValue in CompostArray:
        CanswerArray.append(unsortedValue)
    elif unsortedValue in TrashArray:
        TanswerArray.append(unsortedValue)
    elif unsortedValue in RecycleArray:
        RanswerArray.append(unsortedValue)
    #else:
        #print(unsortedValue + ", Values not Found")


with open("Sorted.txt", "w") as Sorted:
    Sorted.write("Compost: ")
    for counter in range(0,len(CanswerArray)):
        Sorted.write(CanswerArray[counter] + " , ")
    Sorted.write("Trash: ")
    for counter in range(0,len(TanswerArray)):
        Sorted.write(TanswerArray[counter] + " , ")
    Sorted.write("Recycle: ")
    for counter in range(0,len(RanswerArray)):
        Sorted.write(RanswerArray[counter] + " , ")

# Now we need to write answers back to a file
