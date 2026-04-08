# Ask for quantities of computers and printers
quantities_computers = input('How many computers do you want to buy? ')
quantities_printers = input('How many printers do you want to buy? ')

# Convert user inputs in integers
computers = int(quantities_computers)
printers = int(quantities_printers)

# List of items price
# Convert user inputs in integers
printers_cost = 2586
computers_cost = 17458
computers_disc = 145
printers_disc = 58

# Process ticket
if computers >= 10 and printers >= 10:
    total = (computers_cost * computers) + (printers_cost * printers) - (computers_disc * computers + printers_disc * printers)
    print(f"Your total price to pay is U$D {total}")
elif computers >= 10 and printers < 10:
    total = (computers_cost * computers) + (printers_cost * printers) - (computers_disc * computers)
    print(f"Your total price to pay is U$D {total}")
