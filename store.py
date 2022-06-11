import csv
from customer import sxCustomer, pxCustomer, sfCustomer, pfCustomer
class Store:
    def __init__(self):
        self.customers = []
        self.inventory = []
    
    def view_store_inventory(self):
        #todo: do this but with using an ascii table creator module 
        print(f'''
id                       title               rating             release_year            copies_available
''')
        for video in self.inventory:
            print(f'''
{video['video_id']}      {video['title']}    {video['rating']}  {video['release_year']} {video['copies_available']} 
''')
    def find_rentals_by_customer_id(self, input_id):
        #todo: what if customer is not in list? print message 
        input_id = int(input_id)
        all_customer_ids = [customer.customer_id for customer in self.customers]
        while True:
            if input_id not in all_customer_ids:
                print('No customer matches input: {input_id}')
            else:
                return customer.current_video_rentals

    def add_customer(self, customer_data):
        #todo: handle incorrect data, duplicate id, etc
        customer_data['customer_id'] = int(customer_data['customer_id'])
        print(customer_data)
        new_customer = customerMaker(**customer_data)
        self.customers.append(new_customer)

    def rent_video(self, input_customer_id, input_title):
        input_customer_id = int(input_customer_id)
#[{'video_id': 1, 'title': 'Toy Story', 'rating': 'G', 'release_year': 1995, 'copies_available': 0}, {'video_id': 2, 'title': 'WALL-E', 'rating': 'G', 'release_year': 2008, 'copies_available': 2}, {'video_id': 3, 'title': 'Up', 'rating': 'G', 'release_year': 2009, 'copies_available': 5}, {'video_id': 4, 'title': 'Inside Out', 'rating': 'PG', 'release_year': 2015, 'copies_available': 1}, {'video_id': 5, 'title': 'The Prestige', 'rating': 'PG-13', 'release_year': 2006, 'copies_available': 2}, {'video_id': 6, 'title': 'The Dark Knight', 'rating': 'PG-13', 'release_year': 2008, 'copies_available': 3}, {'video_id': 7, 'title': 'Inception', 'rating': 'PG-13', 'release_year': 2010, 'copies_available': 4}, {'video_id': 8, 'title': 'Intersteller', 'rating': 'PG-13', 'release_year': 2014, 'copies_available': 2}, {'video_id': 9, 'title': 'Deadpool', 'rating': 'R', 'release_year': 2016, 'copies_available': 3}, {'video_id': 10, 'title': 'The Godfather', 'rating': 'R', 'release_year': 1972, 'copies_available': 0}]
        #decrement record in inventory
        #todo: must make sure cannot go below 0!
        for item in self.inventory:
            if(item['title'] == input_title):
                item['copies_available'] -= 1
            
        
        #add to customer current video rentals
        #todo: make sure the formatting for current video rentals is correct
        #if not exist, make new [] and append only the name
        #if exists, append with / + input_title
        for customer in self.customers:
            if customer.customer_id == input_customer_id:
                if(customer.current_video_rentals):
                    customer.current_video_rentals += f'/{input_title}'
                else:
                    customer.current_video_rentals = input_title
            #print(customer.current_video_rentals)
    def return_video(self, input_customer_id, input_title):
        input_customer_id = int(input_customer_id)
        #increment record in inventory
        for item in self.inventory:
            if(item['title'] == input_title):
                item['copies_available'] += 1

        for customer in self.customers:
            if customer.customer_id == input_customer_id:
                rentals_list = customer.current_video_rentals.split('/')
                if(input_title in rentals_list):
                    rentals_list.remove(input_title)
                    print(f'match: {input_title} in {rentals_list}')
                    customer.current_video_rentals = '/'.join(rentals_list)
                    print(f'current_video_rentals:   {customer.current_video_rentals}')
                else:
                    print('no match')
                
codeplatoon_store = Store()

def customerMaker(**customer_data):
    print(customer_data)
    if(customer_data['account_type'] == 'sx'):
        return sxCustomer(**customer_data)
    if(customer_data['account_type']== 'px'):
        return pxCustomer(**customer_data)
    if(customer_data['account_type'] == 'sf'):
        return sfCustomer(**customer_data)
    if(customer_data['account_type'] == 'pf'):
        return pfCustomer(**customer_data) 

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
    for customer in codeplatoon_store.customers:
        print(customer.customer_id, customer.first_name, customer.account_type)

with open('data/inventory.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        video_id = int(row['id'])
        release_year = int(row['release_year'])
        copies_available = int(row['copies_available'])
        codeplatoon_store.inventory.append({'video_id': video_id, 'title':row['title'], 'rating': row['rating'], 'release_year': release_year, 'copies_available': copies_available})

codeplatoon_store.find_rentals_by_customer_id(2)
