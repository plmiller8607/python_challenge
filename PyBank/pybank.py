#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Import Dependencies (modules)
import csv, os

# Create file to load and file to output the results 
# Use os.path.join() to return path components as a single string
    #load 
        #directory = ".","Resources"
        # filename = "budget_data.csv"
    #output
        #directory = "."
        # filename = "budget_analysis.txt"
file_to_load=os.path.join(".","Resources","budget_data.csv")
file_to_output=os.path.join(".","budget_analysis.txt")

#set variables 
total_months=0
total_net=0

net_change_list=[]
month_of_changes=[]

increase=["",0]
decrease=["",99999999999999]


# Use "with" for best practice to open then csv reader to read
# Convert csv into a list of dictionaries
with open(file_to_load)as financial_data:
    reader=csv.reader(financial_data)
   

    # Skip the first row of the CSV file, and store it in the variable header. 
        # This allows access the header information separately from the data rows.
    header=next(reader)
       
    #Assign variables
    first_row=next(reader)
    
    total_net+=int(first_row[1]) 
    
    previous_net=int(first_row[1]) 
    
   
    total_months+=1
    
     
    for row in reader:
        #Track the totals    
            # total months
        total_months+= 1
               
            # total net          
        total_net += int(row[1])

       # Track net change in amount of "Profit/Losses"
        net_change=int(row[1])-previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        
        

        # Greatest increase in profits (date&amount)
        if(net_change>increase[1]):
            increase[0]=row[0]
            increase[1]=net_change


       # Greatest decrease in profits (date&amount)
        if(net_change<decrease[1]):
            decrease[0]=row[0]
            decrease[1]=net_change




# average the net change
net_monthly_average=sum(net_change_list)/len(net_change_list)


              
output = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: $ {total_net}\n"
    f"Average Change: $ {net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n"
    
)

print(output)

with open(file_to_output,"w") as txt_file:
    txt_file.write(output)
                  


# In[ ]:




