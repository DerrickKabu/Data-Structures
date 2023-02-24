# Create a dictionary to store car brands as keys and their corresponding models and prices as values
#Github link : https://github.com/DerrickKabu/Data-Structures.git

car_prices = {
    "Toyota": {"Corolla": 15000, "Camry": 20000, "Rav4": 25000, "Supra":80000, "Vitz":5000},
    "Honda": {"Civic": 18000, "Accord": 22000, "CR-V": 28000, "HRV":30000, "Acura-NSX":100000},
    "Ford": {"Fiesta": 12000, "Focus": 17000, "F-150": 25000, "Mustang":200000, "GT":400000},
    "Bugatti":{"Chiron":2000000,"Mistral":3000000, "Veyron":1500000, "DB-11":700000, "Chiron Super Sport":3000000},
    "Lamborghini":{"Murcielago":800000, "Aventador":500000, "Huracan":400000, "Sian":2000000, "Gallardo":200000},
    "Mercedes Benz":{"AMG-GTR":600000, "G-63":400000, "EQS":300000, "GLE":400000, "4MATIC":30000}
}

# A function that allows the user to input a car brand and model and returns the corresponding price

def get_car_price():
    # Prompt user to input a car brand and model
    
    car_brand = input("Enter the brand of the car: ")
    car_model = input("Enter the model of the car: ")
    
    # Search for the car model in the car_prices dictionary
    
    if car_brand in car_prices and car_model in car_prices[car_brand]:
        return car_prices[car_brand][car_model]
    
    else:
        return None

# Call the get_car_price function to get the price of a specific car model

price = get_car_price()

# Check if the price is not None, and print the price of the car model

if price is not None:
    print("The price of the car is: $",price)
else:
    print("Car brand or model not found.")
