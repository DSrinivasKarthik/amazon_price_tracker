
import matplotlib.pyplot as plt
import numpy as np
import csv
L=[]
L1=[]
date_list=[]
price_list=[]
def remove_blank(a,b):
    global test_list
    global list2
    test_list = a
    list2=b
    
    while("" in test_list) : 
            test_list.remove("") 
            
    while("" in list2) : 
            list2.remove("") 
            
    
    if 'Date and Time' in test_list:
        del test_list['Date and Time']
            
    
    
def split(d):
        
    ini_dict = d

    global keys
    global values
    keys = [] 
    values = [] 
    items = ini_dict.items() 
    for item in items: 
            keys.append(item[0]), values.append(item[1]) 
    
    remove_blank(keys,values)
    
def duplicates(d):
    test_dict = d

    temp = [] 
    res = dict() 
    for key, val in test_dict.items(): 
            if val not in temp: 
                    temp.append(val) 
                    res[key] = val
                    

    split(res)
    

def graph(file_name):
   
        
    with open(file_name, mode ='r')as file: 
          
        csvFile = csv.reader(file)
        
        for lines in csvFile:
            L.append(lines)
        global name
        global price
        global date
        name=L[1][0]
        price=[]
        date=[]
        for i in range(1,len(L)):
            price.append(L[i][1])
            
            date.append(L[i][4])
        
        for i in price:
            if i=='price':
                price.remove(i)
        for i in date:
            if i=="date":
                date.remove(i)
        
        d=dict(zip(date,price))
        
        print(d)
        
        
        duplicates(d)
    date_list=test_list
    for k in list2:
        price_list.append(float(k))
    x = np.array(date_list)
    y = np.array(price_list)

    plt.plot(x,y,'ro-',lw=5)
    plt.grid(True)
    plt.title (name)
    plt.xlabel("Date")
    my_xticks = date_list
    plt.xticks(x, my_xticks)
    plt.ylabel("Price")

    plt.show()







