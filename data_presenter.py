open_file = open("CupcakeInvoices.csv", 'r')

# for line in open_file:
#     print(line)

# for line in open_file:
#     cupcake = line.rstrip('\n').split(",")
#     print(cupcake[2])



# for line in open_file:
#     price = line.rstrip('\n').split(",")
#     price = float(price[-1]) * float(price [-2])
#     print(price)


# total = 0

# for line in open_file:
#     price = line.rstrip('\n').split(",")
#     total += float(price[-1])
    
# print(total)

# open_file.close()

from matplotlib import pyplot as plt

chocolate = 0
vanilla = 0
strawberry = 0

for line in open_file:
    price = line.rstrip('\n').split(',')
    if price[2] == 'Chocolate':
        chocolate += float(price[-1]) * float(price[-2])
    elif price[2] == 'Vanilla':
        vanilla += float(price[-1]) * float(price[-2])
    elif price[2] == 'Strawberry':
        strawberry += float(price[-1]) * float(price[-2])

print("strawbery:", strawberry)
print("Vanilla:", vanilla)
print("Chocolate:", chocolate)




cupcakeX = ['Chocolate', 'Vanilla','Strawberry']
cupcakeY = [int(chocolate), int(vanilla), int(strawberry)]

plt.bar(cupcakeX, cupcakeY, width=.25)


plt.style.use('fivethirtyeight')
plt.xlabel('Cupcake Flavors')
plt.ylabel('Revenue Earned per Flavor')
plt.title('Cupcake Revenue Chart')
plt.tight_layout()
plt.show()






