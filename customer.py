class sxCustomer:
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
       self.customer_id = customer_id
       self.account_type = account_type
       self.first_name = first_name
       self.last_name = last_name
       self.current_video_rentals = current_video_rentals
       self.limit_rentals = 1

class pxCustomer(sxCustomer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
        self.account_type = account_type
        self.limit_rentals = 3
        self.current_video_rentals = current_video_rentals
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals)


class sfCustomer(sxCustomer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
        self.account_type = account_type
        self.limit_rating = 'R'
        self.current_video_renatls = current_video_rentals
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals)


class pfCustomer(sfCustomer, pxCustomer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals=None):
        self.account_type = account_type
        self.current_video_rentals = current_video_rentals
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals)
