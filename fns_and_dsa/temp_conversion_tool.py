FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius (fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit= (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main():
    temperature = float(input("Enter the temperature to convert:"))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if temperature_type == "C":
        convertion = convert_to_celsius(temperature)
        print(f"temperature:{convertion}°F")
    if temperature_type == "F":
        convertion = convert_to_fahrenheit(temperature)
        print(f"temperature:{temperature}°C")
    else:
        print("invalid syt,please enter correct :")
main()
