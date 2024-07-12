# temp_conversion_tool.py

# Global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit= (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


# Main function to interact with the user
def main():
    temperature  =int(input("Enter the temperature to convert:"))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if temperature_type == "C":
        convertiion = convert_to_celsius(temperature)
        print(f"temperature:{convertiion}°F")
    if temperature_type =="F" :
        convertiion = convert_to_fahrenheit(temperature)
        print(f"temperature:{temperature}°C")
    else:
        print("invalid number")

main()
