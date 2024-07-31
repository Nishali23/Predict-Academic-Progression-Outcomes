# I declare that my work contains no examples of misconduct,such as plagiarism, or collusion.
# Any code taken from other sources is referenced with in my code solution.
# Student ID : w1985670

# Date : 01/08/2023

#function created for the mainpart

def Mainprogram():

    #try except for value error inside the while true
    
    while True:
        try:
            pcr=int(input("enter your pass mark : "))
            
            #while loop used for get the valid marks
            
            while (pcr!=0) and (pcr!=20) and (pcr!=40) and (pcr!=60) and (pcr!=80) and (pcr!=100) and (pcr!=120):
                print("out of range")
                pcr=int(input("enter your pass mark : "))
            break    

        except ValueError:
            print("Integer required")

    while True:
        try:
            dcr=int(input("enter your defer mark : "))
            while (dcr!=0 and dcr!=20 and dcr!=40 and dcr!=60 and dcr!=80 and dcr!=100 and dcr!=120):
                print("out of range")
                dcr=int(input("enter your defer mark : "))
            break    

        except ValueError:
            print("Integer required")

    while True:
        try:
            fcr=int(input("enter your fail mark : "))
            while (fcr!=0 and fcr!=20 and fcr!=40 and fcr!=60 and fcr!=80 and fcr!=100 and fcr!=120):
                print("out of range")
                fcr=int(input("enter your fail mark : "))
            break    

        except ValueError:
            print("Integer required")
            

    #total for total marks
    #conditions for grades
            
    total=pcr+dcr+fcr        

    if(total!=120):
        print("Total incorrect")

    else:
        if(pcr==120):
            print("Progress")
            credit_list.append("progress ")
        elif(pcr==100):
            print("Progress(module trailer)")
            credit_list.append("trailer  ")
        elif(80<=fcr<=120):
            print("exclude")
            credit_list.append("exclude  ")
        else:
            print("Do not progress – module retriever")
            credit_list.append("retriever")

#function for histogram
            
def count(item):
    histogram={}
    for i in item:
        histogram[i]=histogram.get(i,0)+1
    return histogram            

#list for store grades

credit_list=[]
Mainprogram()           

print()    

start=input('Would you like to enter another set of data? \nEnter y for yes or q to quit and view results : ')

print()

#while loop for loop the program until user enter q for quit

while(start=='y'):

    Mainprogram()     

    print()    

    start=input('Would you like to enter another set of data? \nEnter y for yes or q to quit and view results : ')

    print()

#print the histogram    

if (start=='q'):
    
    

    print ('---------------------------------------------------------')

    print ('Histogram')

    print()

                  
    histrodict =count(credit_list)

    keys=histrodict.keys()
    values=histrodict.values()


    for x,y in zip(keys,values):
        output=''
        times = y
        while times > 0:
                output+='*'
                times=times-1
        print(x,y,':',output)


    print()

    print (len(credit_list) , 'outcomes in total')



    print ('---------------------------------------------------------') 

     
    



        
    



