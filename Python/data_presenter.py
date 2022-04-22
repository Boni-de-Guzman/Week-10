# Create a new file called data_presenter.py.

# done

# Open the CupcakeInvoices.csv.

# done

# Loop through all the data and print each row.


open_file = open("CupcakeInvoices.csv")

for line in open_file:
    print(line)
 
# Loop through all the data and print the type of cupcakes purchased.

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[0])


# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
 
each_total = 0

for line in open_file:
    line = line.strip()
    values = line.split(",")
    each_total = float (values[3])*float(values[4])
    name = values[0]
    print(name, "has total amount of",each_total)


# Loop through all the data, and print out the total for all invoices combined.

all_total = 0

for line in open_file:
    line = line.strip()
    values = line.split(",")
    all_total = all_total+(int(values[3]) * float(values[4]))
    print(all_total)




# Close your open file.]

open_file.close()