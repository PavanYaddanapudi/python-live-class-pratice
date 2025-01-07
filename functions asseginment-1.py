def trip(distance, mileage, fcost):
    if distance == 0 or mileage == 0:
        return False
    else:
        liters = distance / mileage
        tprice = liters * fcost
        return tprice 

def main():
    # Gather input
    distance = int(input("Total distance of trip (in km): "))
    mileage = int(input("Mileage of your vehicle (km/l): "))
    fcost = float(input("Cost of the fuel per liter: "))
    result = trip(distance, mileage, fcost)
    if result is False:
        print("Invalid input: Distance and mileage must be greater than zero.")
    else:
        print("total cost of the trip is:",result)
if __name__ == "__main__":
    main()
