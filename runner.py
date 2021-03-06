# runner performs all input gathering and validation before sending it to
# Store class / codeplatoon_store instance to perform the task
from store import codeplatoon_store, Store

mode = None

while(mode != '6'):
    mode = input("""
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
""")

    if mode == '1':
        codeplatoon_store.view_store_inventory()
    elif mode == '2':
        loop = True
        while(loop):
            customer_id = input('Enter id of customer: ')
            if(not customer_id.isnumeric()):
                print('\nERROR: Customer id must be a valid number')
            elif int(customer_id) not in Store.all_customer_ids():
                print(f'\nERROR: customer "{customer_id}" not found')
            else:
                customer_id = int(customer_id)
                print(f'\n Customer {customer_id} is renting: {codeplatoon_store.find_rentals_by_customer_id(customer_id)}')
                loop=False
    elif mode == '3':
        # gathers valid data and passes to #add_customer
        customer_data = {}
        loop = True
        while loop:
            user_input = input('Enter customer id: ') 
            if(not user_input.isnumeric()):
                print(f'\nERROR: Customer id must be a valid number'); 
            else:
                customer_data['customer_id'] = int(user_input)
                if(customer_data['customer_id'] in Store.all_customer_ids()):
                    print(f'\nERROR: Cannot add customer id: {user_input} because it already exists')
                else:
                    loop=False
            # prompt user for valid entry for account type
        loop = True
        while loop:
            customer_data['account_type'] = input('Enter account type (sx/px/sf/pf): ')
            if(customer_data['account_type'] not in ['sx', 'px', 'sf', 'pf']):
                print('\nERROR: That entry is invalid. Enter: (sx / px / sf / pf)')
            else:
                loop = True
                while(loop):
                    customer_data['first_name'] = input('Enter first name: ')
                    if(len(customer_data['first_name']) == 0):
                        print('\nERROR: Field may not be empty.')
                    else:
                        loop=False
                loop=True
                while(loop):
                    customer_data['last_name'] = input('Enter last name: ')
                    if(len(customer_data['last_name']) == 0): 
                        print('\nERROR: Field may not be empty.') 
                    else:
                        loop=False
                codeplatoon_store.add_customer(customer_data)
                print('\nSUCCESS: Customer created')

    elif mode == '4':
        customer = None
        # validate that user input is numeric and exists
        loop = True
        while(loop):
            customer_id = input('Enter id of customer making the rental: ')
            if(not customer_id.isnumeric()):
                print('\nERROR: Customer id must be a valid number')
            elif(int(customer_id) not in Store.all_customer_ids()):
                print(f'\nERROR: Customer id {customer_id} not found')
            else:
                for i, customer in enumerate(codeplatoon_store.customers):
                    if(customer.customer_id == int(customer_id)):
                        customer = codeplatoon_store.customers[i]
                        if(customer.current_video_rentals == '' or customer.current_video_rentals == None):
                            loop=False
                        elif(customer.current_video_rentals):
                            customer_rentals_total = len(customer.current_video_rentals.split('/'))
                            if(customer.limit_rentals == customer_rentals_total):
                                print(f'\nDENIED: {customer.account_type} customer has already reached max rental limit: {customer.limit_rentals} ({customer.current_video_rentals})')
                            else:
                                loop=False
        # validate input video title is in inventory and doesn't conflict with user's rating limit
        loop = True
        while(loop):
            video_title = input('Enter video title to rent (case sensitive): ')
            if video_title not in Store.all_video_titles():
                print(f'\nERROR: Your search for "{video_title}" did not match any video titles')
            elif customer.limit_rating:
                video_rating = [video['rating'] for video in codeplatoon_store.inventory if video['title'] == video_title][0]
                print('rating', video_rating, customer.limit_rating)
                if customer.limit_rating == video_rating:
                    print(f'\nDENIED: {customer.account_type} has a rating limit: {customer.limit_rating}')
                    break
            for item in codeplatoon_store.inventory:
                if item['title'] == video_title and item['copies_available'] == 0:
                    print(f'\nERROR: "{video_title}": title out of stock')
                elif item['title'] == video_title and item['copies_available'] > 0:
                    loop = False
                    codeplatoon_store.rent_video(customer_id, video_title) 
                    print(f'\nSUCCESS: "{video_title}" is now rented out to customer.')
    elif mode == '5':
        # validate that the input customer_id is numeric and exists
        loop = True
        while(loop):
            customer_id = input('Enter id of customer returning the rental: ')
            if(not customer_id.isnumeric()):
                print('\nERROR: Customer id must be a valid number')
            elif(int(customer_id) not in Store.all_customer_ids()):
                print(f'\nERROR: Customer id {customer_id} not found')
            else:
                loop = False
        loop = True
        # validate that the input video title is part of store inventory,
        # and that the customer has the input video title in their current rentals
        while(loop):
            video_title = input('Enter video title to return (case sensitive): ')
            if video_title not in Store.all_video_titles():
                print(f'\nERROR: Your search for "{video_title}" did not match any video titles')
            else:
                for i, customer in enumerate(codeplatoon_store.customers):
                    if(customer.customer_id == int(customer_id)):
                        customer = codeplatoon_store.customers[i]
                        if(video_title not in customer.current_video_rentals):
                            print(f'\nDENIED: Customer does not have "{video_title}" in ther current rentals: {customer.current_video_rentals}')
                        else:
                            codeplatoon_store.return_video(int(customer_id), video_title)
                            print(f'\nSUCCESS: {video_title} has been returned to shelf')
                            loop=False
    elif mode == '6':
        break
