# Write your solution here!
#from classes.school import School
from store import codeplatoon_store

#school = School('Ridgemont High')
#todo: add more validations
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

    all_customer_ids = [customer.customer_id for customer in codeplatoon_store.customers]
    all_videos = [item['title'] for item in codeplatoon_store.inventory]
    if mode == '1':
        #view store inventory
        codeplatoon_store.view_store_inventory()
    elif mode == '2':
        #View customer rented videos
        while True:
            customer_id = int(input('Enter customer id: '))
            if customer_id not in all_customer_ids:
                print(f'Customer "{customer_id}" does not exist')
            else:
                break
        rental = codeplatoon_store.find_rentals_by_customer_id(customer_id)
        print(rental)
    elif mode == '3': 
        #todo: prevent duplicate ids
        #no initial list of video rentals
        #add new customer
        customer_data = {}
        while True:
            user_input = input('Enter customer id:\n') 
            if(not user_input.isnumeric()):
               print(f'User id must be numeric'); 
            else:
                customer_data['customer_id'] = int(user_input)
                if(customer_data['customer_id'] in all_customer_ids):
                    print(f'Cannot add customer id: {user_input} because it already exists')
                break
        while True:
            customer_data['account_type']       = input('Enter account type (sx/px/sf/pf): \n')
            if(customer_data['account_type'] not in ['sx', 'px', 'sf', 'pf']):
                print('That entry is invalid. Enter: (sx / px / sf / pf)')
            else:
                break
        customer_data['first_name'] = input('Enter first name: \n')
        customer_data['last_name']  = input('Enter last_name: \n')
        codeplatoon_store.add_customer(customer_data)

    elif mode == '4':
        customer = None
        #rent video, pop store inventory, create or append current video rentals
        #validates input id for rental limit
        #todo: handle when empty list shows rental 1 (customer 4)
        loop = True
        while(loop):
            user_input = input('Enter id of the customer making the rental\n') 
            customer_id = None
            if(not user_input.isnumeric()):
                print('customer id must be numeric')
            else: 
                customer_id = int(user_input)
                print(customer_id)
            #validates customer id exists
            all_customer_ids = [customer.customer_id for customer in codeplatoon_store.customers]
            if(customer_id not in all_customer_ids):
                print(f'Customer id {customer_id} not found')
            else:
                for i, customer in enumerate(codeplatoon_store.customers):
                    if(customer.customer_id == customer_id):
                        customer = codeplatoon_store.customers[i]
                        print(f'customer limit rating {customer.limit_rating}')
                        if(customer.current_video_rentals):
                            customer_rentals_total = (len(customer.current_video_rentals.split('/')))
                            print(f'customer.limit_rentals = {customer.limit_rentals}, customer_rentals_total: {customer_rentals_total}')
                            if(customer.limit_rentals == customer_rentals_total):
                                print(f'{customer.account_type} customer has already reached max rental limit: {customer.limit_rentals} ({customer.current_video_rentals})')
                        #elif(customer.limit_rating == video_rating):
                        #    pass
                        else:
                            loop = False
        #validates input video title
        loop = True
        while(loop):
            video_title = input('Enter video title to rent (case sensitive)\n')
            if video_title not in all_videos:
                print(f'Your search for "{video_title}" did not match any video titles\n')
            elif customer.limit_rating:
                video_rating = [video['rating'] for video in codeplatoon_store.inventory if video['title'] == video_title][0]
                print('rating', video_rating, customer.limit_rating)
                if customer.limit_rating == video_rating:
                    print(f'{customer.account_type} has a rating limit: {customer.limit_rating}')
                    break
                for item in codeplatoon_store.inventory:
                    break
                    if item['title'] == video_title and item['copies_available'] == 0:
                        print(f'"{video_title}": title out of stock\n')
                    elif item['title'] == video_title and item['copies_available'] > 0:
                        print(f'"{video_title}": title is available to rent out\n')
                        loop = False
            codeplatoon_store.rent_video(customer_id, video_title) 
            break
    elif mode == '5':
        video_title = input('Enter video title to return (case sensitive)\n')
        customer_id = input('Enter id of customer returning the rantal\n')
        codeplatoon_store.return_video(customer_id, video_title)
        #return video
        pass
    elif mode == '6':
        break
