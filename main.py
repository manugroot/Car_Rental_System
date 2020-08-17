# import Customer,CarRental
from carrentalsys import Customer,CarRental


def main():
    shop = CarRental(20)
    customer = Customer()


    while True:
        n= input("""        
                ----------Car Rentals-----------------
                1) Cars Available in Garage.
                2) To initiate rental per hour service.
                3) To initiate rental per day service.
                4) To initiate rental per week service.
                5) To initiate rental per month service.
                6) To initiate returning the Car(s).
                7) Exit.
                """)
        try:
            choice=int(n)
        except ValueError:
            print("Oops!!!,U choose invalid option.")
            continue

        if(choice==1):
            shop.displayGarage()
        elif(choice==2):
            customer.rentalTime=shop.rentalperhour(customer.orderCar())
            customer.rentalType=1
        elif(choice==3):
            customer.rentalTime=shop.rentalperday(customer.orderCar())
            customer.rentalType=2
        elif(choice==4):
            customer.rentalTime=shop.rentalperweek(customer.orderCar())
            customer.rentalType=3
        elif(choice==5):
            customer.rentalTime=shop.rentalpermonth(customer.orderCar())
            customer.rentalType=4
        elif(choice==6):
            customer.bill = shop.returnCar(customer.returnCar())
            customer.rentalType,customer.rentalTime,customer.cars=0,0,0
        elif(choice==7):
            break
        else:
            print("OOPs!!!,U have to chose a number between 1-7")
            continue
        print("Thanks for using Car-Rental-Services")

if __name__=="__main__":
    main()
