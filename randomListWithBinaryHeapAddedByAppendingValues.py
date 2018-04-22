#F. Derek Roman - GitHub Profile CodeNamor
#SWDV-610-3W Data Structures Unit 6

#import random module
import random
#import for using heap functionality
import heapq

#function for generating a random list of integers and storing those numbers in a list
def RandList(begin,end,inc):
    #create and emply list for storing the random integer values
    intList=[]
    #for loop for creating the values and storing those values into the list
    for i in range(inc):
        intList.append(random.randint(begin,end))
        #return the list
    return intList

def main():
    begin=1
    end=100
    ind=10
    li = []     #creating an empty list to append the values too
    #append values of the RandList function to the empty list
    li.append(RandList(begin,end,ind))
    #print the heap values
    print("The heap values are ",end=" ")
    print(list(li))
    
main()
