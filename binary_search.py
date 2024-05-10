

def binary_search(lst, key):    #lst is our array and key is the item we want to find
    start = 0
    end = len(lst)
    i = (start+end)//2  #integer division

    while start <= end:
        print("start is", start, "end is", end)
        print("i is", i, "lst[i] is", lst[i])
        if lst[i] == key:
            return(key, i)
        elif lst[i] < key:
            #we move right
            start = i + 1
        else:
            #we move left
            end = i - 1

        i = (start+end)//2
    
    return(key, -1)

if __name__ == "__main__":
    lst = [0,1,3,4,5,6,7,8,9,10]
    key = 2
    print(binary_search(lst, key))





























"""


def binary_search(lst, key):
    start = 0
    end = len(lst)

    i = (start+end)//2      #integer division

    while start <= end:
        print("start is", start, "end is", end)
        print("i is", i, "lst[i] is", lst[i])
        if lst[i] == key:
            #stop looking
            return(key, i)
        elif lst[i] < key:
            #move right in the list
            start = i + 1
        else:
            #move left in the list
            end = i - 1

        i = (start+end)//2
    
    return(key, -1)

if __name__ == "__main__":
    lst = [0,1,3,4,5,6,7,8,9,10]
    key = 2
    print(binary_search(lst, key))

    

[0,1,3,4,5,6,7,8,9,10]


#lst is the array, and key is the item we are looking for
#we want to return the key and the index (or -1 if the index DNE)
def binary_search(lst, key):    
    start = 0
    end = len(lst)

    i = (start+end)//2

    while start <= end:
        if lst[i] == key:
            return(key, i)
        elif lst[i] < key:
            #we move right
            start = i + 1
        else:
            #we move left
            end = i -1
        i = (start+end)//2
    
    return(key, -1)





























def binary_search_tree(lst, key):
    #print("key is", key, "of type", type(key))
    start = 0
    end = len(lst) - 1
    i = (end + 1)//2

    while start <= end:
        #print("start is", start, "end is", end)
        #print("i is now", i, "lst[i] is", lst[i])
        if lst[i] == key:
            return(key, i)
        elif lst[i] < key:
            #move right
            start = i + 1
        else:
            #move left
            end = i - 1
        i = (end+start)//2
    
    if (start > end):
        print("broke loop bc start not < end")
    else:
        print("broke loop bc i became out of bounds")
    return (key,-1)


if __name__ == "__main__":
    for i in range(-10, 20):
        print(binary_search_tree([0,1,2,3,4,5,6,7,8,9,10], i))
        print()
"""