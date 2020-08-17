import datetime
class CarRental:
    def __init__(self,garage=0):
        """Constructor to instantiate the CarRenta Class"""
        self.garage=garage

    def displayGarage(self):
        """To print the number of cars present in the Garage at that instant"""
        print("We have {} cars at present in our garage".format(self.garage))
        return self.garage

    def rentalperhour(self,n):
        """To rent a Car on hourly basis"""
        if n>self.garage:
            print("Sorry we only have {} cars in our garage at present".format(self.garage))
            return None
        else:
            present=datetime.datetime.now()
            print("You rented {} cars today for hourly basis".format(n,present.hour))
            print("As you ranted {} cars today on hourly basis the cost per hour will be Rs.{} per car".format(n,500))
            print("We hope you enjoy our service...")

            self.garage-=n
            return present

    def rentalperday(self,n):
        """To rent a Car on daily basis"""
        if n > self.garage:
            print("Sorry we only have {} cars in our garage at present".format(self.garage))
            return None
        else:
            present = datetime.datetime.now()
            print("You rented {} cars today on hourly basis".format(n, present.hour))
            print("As you ranted {} cars today on hourly basis the cost per hour will be Rs.{} per car".format(n, 2000))
            print("We hope you enjoy our service...")

            self.garage -= n
            return present

    def rentalperweek(self,n):
        """To rent a Car on weekly basis"""
        if n > self.garage:
            print("Sorry we only have {} cars in our garage at present".format(self.garage))
            return None
        else:
            present = datetime.datetime.now()
            print("You rented {} cars today on hourly basis".format(n, present.hour))
            print("As you ranted {} cars today on hourly basis the cost per hour will be Rs.{} per car".format(n, 7000))
            print("We hope you enjoy our service...")

            self.garage -= n
            return present

    def rentalpermonth(self,n):
        """To rent a Car on monthly basis"""
        if n > self.garage:
            print("Sorry we only have {} cars in our garage at present".format(self.garage))
            return None
        else:
            present = datetime.datetime.now()
            print("You rented {} cars today on hourly basis".format(n, present.hour))
            print("As you ranted {} cars today on hourly basis the cost per hour will be Rs.{} per car".format(n, 17500))
            print("We hope you enjoy our service...")

            self.garage -= n
            return present

    def returnCar(self,request):
        """
        Task this function does are:
        1)Recovers the rented cars from the customer
        2)Increment the garage count with the recovered cars
        3)Provide a bill to the customer
        """
        rentalTime,rentalType,rentalCars=request
        bill=0
        if rentalCars and rentalType and rentalTime:
            self.garage+=rentalCars
            present = datetime.datetime.now()
            rentalPeriod=present-rentalTime
            print("Number of Rental cars are {}.".format(rentalCars))

            #Hourly bill calculation
            if rentalType==1:
                bill=round(rentalPeriod.seconds) * 500 * rentalCars
                print("Your bill is Rs.{} only".format(bill))

            #Daily bill calculation
            elif rentalType==2:
                bill=round(rentalPeriod.days) * 2000 * rentalCars
                print("Your bill is Rs.{} only".format(bill))

            #Weekly bill calculation
            elif rentalType==3:
                bill=round(rentalPeriod.days/7) * 7000 * rentalCars
                print("Your bill is Rs.{} only".format(bill))

            #Monthly bill Calculation
            elif rentalType==4:
                bill=round(rentalPeriod.days/30) * 17500 * rentalCars
                print("Your bill is Rs.{} only".format(bill))

            #If the number of cars rented would be equal to three then the family offer will be applicable
            #which is reduction of 30% of price
            # bill= round(bill*(rentalCars//3)*0.7) + bill*(rentalCars%3)
            print("Thanks for returning our car safely.Hope you enjoyed driving")
            print("Your bill is Rs.{} only".format(bill))
            return bill

        else:
            print("Sorry you came to wrong address.You didn't rent the cars from us..")
            return None



class Customer:
    def __init__(self):
        """Contructor method which instantiates various customer objects"""
        self.bill=0
        self.cars=0
        self.rentalType=0
        self.rentalTime=0

    def orderCar(self):
        """
        Takes an order from the customer for the number of cars
        """
        n=input("How many cars would u like to rent?")
        try:
            n=int(n)
        except ValueError:
            print("This is not a number.Plz enter the number..")
            return -1

        if n<=0:
            print("Invalid Input.The number entered should be positive integer")
            return -1
        else:
            self.cars=n
        return self.cars

    def returnCar(self):
        """
        Allows the customers to return the cars booked
        """
        if self.rentalTime and self.rentalType and self.cars:
            return self.rentalTime,self.rentalType,self.cars
        return 0,0,0
