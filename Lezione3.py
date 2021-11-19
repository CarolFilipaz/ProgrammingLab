# scrivere uno script che sommi tutti i valori delle vendite degli shampoo del file "shampoo_sales.csv". Poi committate il file in cui l'avete scritto.


#apro shampoo_sales
my_file = open ('shampoo_sales.txt', 'r')

#inizializzo lista vuota dove ci sono i valori
values = []

#
s=0


for line in my_file:
 
  elements = line.split(',')

  if elements[0] != 'Date':
    date = elements[0]
    value = elements[1]

    values.append(float(value))

    s=s+float(elements[1])

print(s)

my_file.close()


  


