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

    if mode == '1':
        #view store inventory
        codeplatoon_store.view_store_inventory()
#        school.list_customers()
        pass
    elif mode == '2':
        #View customer rented videos
        customer_id = input('Enter customer id: ')
        rental = codeplatoon_store.find_rentals_by_customer_id(customer_id)
        print(rental)
    elif mode == '3': 
        #todo: prevent duplicate ids
        #no initial list of video rentals
        #add new customer
        customer_data = {}
        while True:
            input_customer_id = input('Enter customer id:\n')
            all_customer_ids = [customer.customer_id for customer in codeplatoon_store.customers]
            if(input_customer_id in all_customer_ids):
                print('Cannot add customer id: {customer_id} because it already exists')
            else:
                break
        customer_data['customer_id']      = input('Enter customer id:\n')
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
        #rent video, pop store inventory, create or append current video rentals
        all_videos = [item['title'] for item in codeplatoon_store.inventory]
        loop = True
        while (loop == True):
            video_title = input('Enter video title to rent (case sensitive)\n')
            if video_title not in all_videos:
                print(f'Your search for {video_title} did not match any video titles\n')
            elif video_title in all_videos:
                for item in codeplatoon_store.inventory:
                    if item['title'] == video_title and item['copies_available'] == 0:
                        print(f'{video_title} out of stock\n')
                    elif item['title'] == video_title and item['copies_available'] > 0:
                        print(f'{video_title} is available to rent out\n')
                        loop = False
        while(True):
            customer_id = int(input('Enter id of customer making the rental\n'))
            all_customer_ids = [customer.customer_id for customer in codeplatoon_store.customers]
            if(customer_id not in all_customer_ids):
                print(f'Customer id {customer_id} not found')
            else:
                break
        codeplatoon_store.rent_video(customer_id, video_title) 
    elif mode == '5':
        video_title = input('Enter video title to return (case sensitive)\n')
        customer_id = input('Enter id of customer returning the rantal\n')
        codeplatoon_store.return_video(customer_id, video_title)
        #return video
        pass
    elif mode == '6':
        break
