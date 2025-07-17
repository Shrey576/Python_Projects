def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    currencies = {"USD": 1, "EUR": 0.91, "GBP": 0.81, "INR": 82.03}
    
    print("Available currencies: USD, EUR, GBP, INR")
    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()
    
    if from_currency in currencies and to_currency in currencies:
        amount = float(input(f"Enter amount in {from_currency}: "))
        exchange_rate = currencies[to_currency] / currencies[from_currency]
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency.")

main()
