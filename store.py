import csv
from tabulate import tabulate
from customer import sxCustomer, pxCustomer, sfCustomer, pfCustomer

class Store:
    # every instance will have its own set of customers and inventory
    def __init__(self):
        self.customers = []
        self.inventory = []

    @classmethod
    def all_video_titles(cls):
        all_video_titles = [item['title'] for item in codeplatoon_store.inventory]
        return all_video_titles

    @classmethod
    def all_customer_ids(cls):
        all_customer_ids = [customer.customer_id for customer in codeplatoon_store.customers]
        return all_customer_ids

    # prints a table of current inventory using the tabulate module
    def view_store_inventory(self):
        all_videos = [[video['video_id'], video['title'], video['rating'], video['release_year'], video['copies_available']] for video in self.inventory]
        print(tabulate(all_videos, headers=['id', 'title', 'rating', 'release year', 'copies available']))

    # accepts user input id string to check against customers list, returns list of rentals
    def find_rentals_by_customer_id(self, input_id):
        input_id = int(input_id)
        for customer in self.customers:
            if(customer.customer_id == input_id):
                return customer.current_video_rentals

    # accepts customer data object, makes a Customer instance and appends it to customers list
    def add_customer(self, customer_data):
        #todo: handle incorrect data, duplicate id, etc
        customer_data['customer_id'] = int(customer_data['customer_id'])
        new_customer = customerMaker(**customer_data)
        self.customers.append(new_customer)
    
    # accepts user provided input strings
    # decrements copies available in inventory
    # concatenates input_title to the customer video rentals 
    def rent_video(self, input_customer_id, input_title):
        input_customer_id = int(input_customer_id)
         
        for item in self.inventory:
            if(item['title'] == input_title):
                item['copies_available'] -= 1
            
        for customer in self.customers:
            if customer.customer_id == input_customer_id:
                if(customer.current_video_rentals):
                    customer.current_video_rentals += f'/{input_title}'
                else:
                    customer.current_video_rentals = input_title

    # accepts user provided input strings
    # removes the input_title from customer's video rentals
    # increments copies available in inventory
    def return_video(self, input_customer_id, input_title):
        input_customer_id = int(input_customer_id)
        for customer in self.customers:
            if customer.customer_id == input_customer_id:
                if(customer.current_video_rentals):
                    rentals_list = customer.current_video_rentals.split('/')
                    if(input_title in rentals_list):
                        rentals_list.remove(input_title)
                        customer.current_video_rentals = '/'.join(rentals_list)
                else:
                    print(f'{input_title} did not match this user\'s current rentals {customer.current_video_rentals}')
        for item in self.inventory:
            if(item['title'] == input_title):
                item['copies_available'] += 1
                
codeplatoon_store = Store()

# this function is used to populate customers based on their account type
# via #add_customer and also for populating CSV customers
def customerMaker(**customer_data):
    if(customer_data['account_type'] == 'sx'):
        return sxCustomer(**customer_data)
    if(customer_data['account_type']== 'px'):
        return pxCustomer(**customer_data)
    if(customer_data['account_type'] == 'sf'):
        return sfCustomer(**customer_data)
    if(customer_data['account_type'] == 'pf'):
        return pfCustomer(**customer_data) 

# only codeplatoon_store instance holds this set of customer and inventory data 
with open('data/customers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        customer_id = int(row['id'])
        account_type = row['account_type']
        first_name = row['first_name']
        last_name = row['last_name']
        current_video_rentals = row['current_video_rentals']
        new_customer = customerMaker(customer_id=customer_id, account_type=account_type, first_name=first_name, last_name=last_name, current_video_rentals=current_video_rentals)
        codeplatoon_store.customers.append(new_customer)

with open('data/inventory.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        video_id = int(row['id'])
        release_year = int(row['release_year'])
        copies_available = int(row['copies_available'])
        codeplatoon_store.inventory.append({'video_id': video_id, 'title':row['title'], 'rating': row['rating'], 'release_year': release_year, 'copies_available': copies_available})

