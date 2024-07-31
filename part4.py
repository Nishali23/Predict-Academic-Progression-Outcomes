# I declare that my work contains no examples of misconduct,such as plagiarism, or collusion.
# Any code taken from other sources is referenced with in my code solution.
# Student ID : w1985670

# Date : 01/08/2023

def Mainprogram():

    #user input for get the student id
    student_id=input("Enter your Student Id : ")

    while True:
        try:
            pcr=int(input("enter your pass mark : "))
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
            

    total=pcr+dcr+fcr

    #insert student id , student marks and grade to my_dict

    if(total!=120):
        print("Total incorrect")

    else:
        if(pcr==120):
            print("Progress")
            my_dict.update({student_id :["progress",pcr,dcr,fcr] })
            
        elif(pcr==100):
            print("Progress(module trailer)")
            my_dict.update({student_id :["trailer",pcr,dcr,fcr] })
            
        elif(80<=fcr<=120):
            print("exclude")
            my_dict.update({student_id :["exclude",pcr,dcr,fcr] })
            
        else:
            print("Do not progress – module retriever")
            my_dict.update({student_id :["retriever",pcr,dcr,fcr] })
            

def count(item):
    histogram={}
    for i in item:
        histogram[i]=histogram.get(i,0)+1
    return histogram            

#dictionary for the store the data
my_dict={}
Mainprogram()           

print()    

start=input('Would you like to enter another set of data? \nEnter y for yes or q to quit and view results : ')

print()

while(start=='y'):

    Mainprogram()     

    print()    

    start=input('Would you like to enter another set of data? \nEnter y for yes or q to quit and view results : ')

    print()

if (start=='q'):

    #print the data in my_dict

    my_dict_keys=my_dict.keys()
    my_dict_values=my_dict.values()

    for keys,values in zip(my_dict_keys , my_dict_values):
        print(keys,end = " : " )
        for items in values:
            print(items,end=" ")
        print()    
    

    
    
    

    
    



        
    



