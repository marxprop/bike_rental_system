import datetime
import random
bike_available = 50
tags = ["BK{0:03}".format(i) for i in range(1,bike_available+1)]
rental_codes = [i for i in range(1000,2001)] 
transaction_details = {}

class Rental_system(object):
    def __init__(self,bikes_available=bike_available):
        self.bike_available = bikes_available
        global transaction_details
        self.bike_tags = tags

    def hourly_rental(self, amount_of_bikes, no_of_hours):
        print('Note, You will be charged $5 per hour')
        self.amount_per_period = 5
        self.amount_of_bikes = amount_of_bikes
        self.no_of_hours = self.rent_duration
        self.rental_type = 'hour(s)'
        self.due_time = self.date_time + datetime.timedelta(hours = self.rent_duration)
        self.billing()
        self.generate_code()
        self.invoice()

    def daily_rental(self, amount_of_bikes, no_of_days):
        print('You will be charged $20 per day')
        self.amount_per_period = 20
        self.amount_of_bikes = amount_of_bikes
        self.days = self.rent_duration
        self.rental_type = 'day(s)'
        self.due_time = self.date_time + datetime.timedelta(hours = self.rent_duration*24)
        self.billing()
        self.generate_code()
        self.invoice()

    def weekly_rental(self, amount_of_bikes, no_of_weeks):
        print('You will be charged $60 per week')
        self.amount_per_period = 60
        self.amount_of_bikes = amount_of_bikes
        self.no_of_weeks = self.rent_duration
        self.rental_type = 'week(s)'
        self.due_time = self.date_time + datetime.timedelta(hours = self.rent_duration*24*7)
        self.billing()
        self.generate_code()
        self.invoice()

    def billing(self):
        self.borrow_time = str(self.date_time.year)+'-'+str(self.date_time.month)+'-'+str(self.date_time.day) + '      ' + 'Time:'+ self.date_time.strftime("%I")+':'+ self.date_time.strftime("%M")+self.date_time.strftime("%p")
        self.dued_time = str(self.due_time.year)+'-'+str(self.due_time.month)+'-'+str(self.due_time.day) + '           ' 'Due time:'+ self.due_time.strftime("%I")+':'+ self.due_time.strftime("%M")+self.due_time.strftime("%p")
        if self.amount_of_bikes < 1:
            print('Please how many bikes do you want to rent?')
            ax.customer()
        
        elif self.amount_of_bikes >= 3 and self.amount_of_bikes <= 5:
            print("\nCongratulations you're eligible for the family rental discount")
            total_amount = (self.amount_of_bikes * self.rent_duration * self.amount_per_period)
            discount_amount = total_amount * 0.3
            self.amount_to_pay = total_amount - discount_amount
        
        else:
            self.amount_to_pay = (self.amount_of_bikes * self.rent_duration * self.amount_per_period)

    def generate_code(self):
        global rental_codes, transaction_details, tags
        self.customer_code = random.choice(rental_codes)
        transaction_details.update({ self.customer_code : [self.customer_code, self.name, self.choice, self.amount_of_bikes, self.rent_duration, self.rental_type, self.borrow_time, self.dued_time, self.amount_to_pay, self.bike_tag]})
        rental_codes.remove(self.customer_code)

    def invoice(self):
        print("\nMVF BIKE RENTAL INVOICE")
        print("Name:", self.name,)
        print("Rental code:", self.customer_code)
        print("Rental period type:", self.choice)
        print('Amount of bike(s) rented:', self.amount_of_bikes)
        print("Rental period duration:", self.rent_duration, self.rental_type)
        print("Day of rental:", self.borrow_time)
        print("Due date:", self.dued_time)
        print("Amount to pay:", str(self.amount_to_pay)+'$')
        print("Rented bike tags:", *self.bike_tag, sep = ', ')
        print('--------------------------------------------------------')

    def returnbike(self):
        global bike_available
        print("\nInput the RENTAL CODE on your invoice to see your details")
        entered_code = int(input('Enter your rental code: '))
        if entered_code in transaction_details:
            trans_det = transaction_details.get(entered_code)
            print("\nMVF BIKE RENTAL INVOICE")
            print("Name:", trans_det[1],)
            print("Rental code:", trans_det[0])
            print("Rental period type:", trans_det[2])
            print('Amount of bike(s) rented:', trans_det[3])
            print("Rental period duration:", trans_det[4], trans_det[5])
            print("Day of rental:", trans_det[6])
            print("Due date:", trans_det[7])
            print("Amount to pay:", str(trans_det[8])+'$')
            print("Rented bike tags:", *trans_det[9], sep = ', ')
            owner = input("\n Owner has confirmed payments and bike tags? (YES/NO): ")
            if owner == 'yes' or owner =='YES' or owner == 'Yes':
                del transaction_details[entered_code]
                bike_available += trans_det[3]
                for i in self.bike_tags:
                    self.bike_tags.remove(i)
                print('PAID!!!!')
            else:
                print("Please confirm with the shop owner, Thanks.....")
        
        else:
            print("Invalid passcode!!!")




            

class customer(Rental_system):
    def choices(self):
        global bike_available, tags
        self.date_time = datetime.datetime.now()
        choice = input("Please input your type of rental period: ")
        self.choice = choice
        self.bike_tag = []
        if self.choice == 'hourly':
            self.amount_of_bikes = int(input("How many bike(s) do you want to rent: "))
            self.rent_duration = int(input("For how many hours do you want to rent: "))
            if self.amount_of_bikes < self.bike_available:
                self.bike_tag = self.bike_tags[:self.amount_of_bikes]
                tags = [bike for bike in tags if bike not in self.bike_tag]
                self.name = str(input("Please insert your fullname here: "))
                self.hourly_rental(self.amount_of_bikes, self.rent_duration)
                bike_available -= self.amount_of_bikes
            
            else:
                print('Not enough bikes available for rental!')

        elif self.choice == 'daily':
            self.amount_of_bikes = int(input("How many bike(s) do you want to rent: "))
            self.rent_duration = int(input("For how many days do you want to rent: "))
            if self.amount_of_bikes < self.bike_available:
                self.bike_tag = self.bike_tags[:self.amount_of_bikes]
                tags = [bike for bike in tags if bike not in self.bike_tag]
                self.name = str(input("Please insert your fullname here: "))
                self.daily_rental(self.amount_of_bikes, self.rent_duration)
                bike_available -= self.amount_of_bikes
            
            else:
                print('Not enough bikes available for rental!')

        elif self.choice == 'weekly':
            self.amount_of_bikes = int(input("How many bike(s) do you want to rent: "))
            self.rent_duration = int(input("For how many weeks do you want to rent: "))
            if self.amount_of_bikes < self.bike_available:
                self.bike_tag = self.bike_tags[:self.amount_of_bikes]
                tags = [bike for bike in tags if bike not in self.bike_tag]
                self.name = str(input("Please insert your fullname here: "))
                self.weekly_rental(self.amount_of_bikes, self.rent_duration)
                bike_available -= self.amount_of_bikes
            
            else:
                print('Not enough bikes available for rental!')

        else: 
            print('Error!, Please insert an appropriate rental period')    

while True:
    transaction = input("Hello there! What do you want to do? (RENT / RETURN): ")
    if transaction == 'rent' or transaction == 'ReNT' or transaction== 'RENT':
        print('\nCurrently we have', bike_available, 'bikes available for rental')
        print('--------------------------------------------------------------------------')
        print('''You can rent bikes on hourly basis for $5 per hour.
    You can rent bikes on daily basis for $20 per day.
    You can rent bikes on weekly basis for $60 per week.
    You can also have rental discounts for 3 to 5 bike rentals.\n
    Type in (hourly,daily or weekly) depending on your choice of rental period''')
        
        customer1 = customer()
        customer1.choices()

    elif transaction == 'return' or transaction == 'Return' or transaction== 'RETURN':
        customer1 = customer()
        customer1.returnbike()

    else:
        print("Please input an appropraite option")

    


