# I declare that my work contains no examples of misconduct,such as plagiarism, or collusion.
# Any code taken from other sources is referenced with in my code solution.
# Student ID : w1985670

# Date : 01/08/2023

def Mainprogram():

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

    if(total!=120):
        print("Total incorrect")

    else:
        if(pcr==120):
            print("Progress")
            credit_list.append("progress ")
            value_list.append(pcr)
            value_list.append(dcr)
            value_list.append(fcr)
        elif(pcr==100):
            print("Progress(module trailer)")
            credit_list.append("trailer  ")
            value_list.append(pcr)
            value_list.append(dcr)
            value_list.append(fcr)
        elif(80<=fcr<=120):
            print("exclude")
            credit_list.append("exclude  ")
            value_list.append(pcr)
            value_list.append(dcr)
            value_list.append(fcr)
        else:
            print("Do not progress – module retriever")
            credit_list.append("retriever")
            value_list.append(pcr)
            value_list.append(dcr)
            value_list.append(fcr)

def count(item):
    histogram={}
    for i in item:
        histogram[i]=histogram.get(i,0)+1
    return histogram

#created value lis for store each student pcr dcr fcr

credit_list=[]
value_list=[]
Mainprogram()           

print()    

start=input('Would you like to enter another set of data? \nEnter y for yes or q to quit and view results : ')

print()

while(start=='y'):

    Mainprogram()     

    print()    

    start=input('Would you like to enter another set of data? \nEnter y for yes or q to quit and view results : ')

    print()

    
#histogram printing
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


#task2 print the grades with marks
    
index1=0
index2=1
index3=2

for i in credit_list:

    print(i, end="-")
    print(value_list[index1],",",value_list[index2],",",value_list[index3])
    index1=index1+3
    index2=index2+3
    index3=index3+3


    

#task 3 text file handling

f0=open("text.txt","w")
element1="-"
element2=","

index1=0
index2=1
index3=2

for i in credit_list:
    
    all_values=str(value_list[index1])+","+str(value_list[index2])+","+str(value_list[index3])
    f0.write(i+element1)
    f0.write(all_values)
    f0.write("\n")
    index1=index1+3
    index2=index2+3
    index3=index3+3

f0.close()


     
    



        
    



