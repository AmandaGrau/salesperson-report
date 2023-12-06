"""Generate sales report showing total melons each salesperson sold."""


# Variables assigned to salepeople and melons_sold as blank lists
salespeople = []
melons_sold = []

# Opens and loops over lines in text file, strips extra whitespace, and creates a list of strings
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    
    # Gets salesperson at index[0] and melons they've sold at index[2]
    salesperson = entries[0]
    melons = int(entries[2])
    
    # Checks if salesperson iis in the salespeople list
    if salesperson in salespeople:
        # Finds position where salesperson is stored in the salespeople list
        position = salespeople.index(salesperson)
        # Uses salesperson index position to index into melons_sold list
        melons_sold.append(melons_sold[position])
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)
        
# Loops through the indices in the salesperson list and 
# and prints the name os the salesperson and the melons they've sold.
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    