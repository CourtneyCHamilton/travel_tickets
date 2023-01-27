# ticket types
ticket_type = 0
display_ticket_type = True

# display ticket type menu
while display_ticket_type:
    print(str('Ticket types:'))
    print(format("1. Budget", '<11s')+"("+(format("500kr", '>6'))+")")
    print(format("2. Economy", '<11s')+"("+(format("750kr", '>6'))+")")
    print(format("3. VIP", '<11s')+"("+(format("2000kr", '>6'))+")")
    print()

    userTicket_choice = int(input('Input ticket type '))

    if userTicket_choice == 1:
        ticket_type = 500
        display_ticket_type = False
    elif userTicket_choice == 2:
        ticket_type = 750
        display_ticket_type = False
    elif userTicket_choice == 3:
        ticket_type = 2000
        display_ticket_type = False
    else:
        print('Invalid choice.')

print()

# display user selections declare variables
num_bag = 0
num_meal = 0
display_options = True

# user options
while display_options:
    print(str('Currently you have:'))
    print(num_bag, str('bag(s) registered'))
    print(num_meal, str('meal(s) registered'))
    print()

    print('Here are your options:')
    print(str('1. Add bag (max 1)'))
    print(str('2. Add meal (max 1)'))
    print(str('3. Remove bag'))
    print(str('4. Remove meal'))
    print(str('5. Finalize ticket'))

# optional purchase user input
    opt_purch = int(input('Your choice '))

    if opt_purch == 1:
        num_bag += 1
    elif opt_purch == 2:
        num_meal += 1
    elif opt_purch == 3:
        num_bag = 0
    elif opt_purch == 4:
        num_meal = 0
    elif opt_purch == 5:
        display_options = False
    else:
        print('Invalid choice.')
        print()
    print()
# Finalizing the ticket
bag_total = 0
meal_total = 0
# bag total condition
if num_bag == 1:
    bag_total = 200
else:
    bag_total = 0

# meal total condition
if num_meal == 1:
    meal_total = 150
else:
    meal_total = 0

# receipt calulation
receipt_total = bag_total + meal_total + ticket_type

# receipt itemized
header = str('Receipt:')
ticket_receipt = str(format("Ticket", '<7')+":"+format(ticket_type, '>5d')+"kr")
bag_receipt = str(format("Bag", '<7')+":"+format(bag_total, '>5d')+"kr")
meal_receipt = str(format("Meal", '<7')+":"+format(meal_total, '>5d')+"kr")
divider_line = str(format("-------", '>15s'))
receipt_sum_display = str(format("Total", '<7')+":"+format(receipt_total, '>5d')+"kr")

items = [header, ticket_receipt]

# add bag and/or meal to receipt
if bag_total > 0:
    items.append(bag_receipt)

if meal_total > 0:
    items.append(meal_receipt)

# add dashes and total sum to receipt display
items.append(divider_line)
items.append(receipt_sum_display)

# display receipt
for x in items:
    print(x)
