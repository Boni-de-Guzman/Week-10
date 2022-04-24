
log_file = open("um-server-01.txt") 
#its variable called log_file to get the content of  the file (.txt, csv,etc)

def sales_reports(log_file):
    # def meaning defining function followed by parameters
    
    for line in log_file:
        # for loop is use to iterate through list performing the same action on each item.

        line = line.rstrip()
        
        # rstrip is use to remove trailing characters and it's define by the variable called line

        day = line[0:3]
     
        #  using bracket notation allows to pull out specific amount_melon. the number inside the bracket ([0:3]) refers to the value index 

        if day == "Mon":
            print(line)
        
        # "if" is a conditional statement if the value is determined weather true or false. If the statement is true it would run whatever condition is given otherwise it it would generate the condition given by else statement.

sales_reports(log_file)
    
    #  this prints out whatever the specific function given



########(Extra Credit)#############

# In process.py, write another function that prints out all the melon orders that delivered over 10 melons.

for lines in log_file:
    for line in lines:
       line = lines.split()
       value = line[2]
       amount_melon = int(value)

    if(amount_melon > 10):
     print(lines)

    
    

