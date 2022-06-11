class sxCustomer:
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
       self.customer_id = customer_id
       self.account_type = account_type
       self.first_name = first_name
       self.last_name = last_name
       self.current_video_rentals = current_video_rentals
       self.limit_rentals = 1
       self.limit_rating = None

class pxCustomer(sxCustomer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals)
        self.account_type = account_type
        self.current_video_rentals = current_video_rentals
        self.limit_rentals = 3

class sfCustomer(sxCustomer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals)
        self.account_type = account_type
        self.current_video_renatls = current_video_rentals
        self.limit_rating = 'R'

class pfCustomer(pxCustomer, sfCustomer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals)
        self.account_type = account_type
        self.current_video_rentals = current_video_rentals

jon = pfCustomer(10, 'pf', 'jon', 'fancy')
print(jon.limit_rentals)
print(jon.limit_rating)
