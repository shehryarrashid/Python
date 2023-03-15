balance = 1000
amount = int("300")
def take_card():
    print("Take the card out of ATM")

try:
    if balance >= int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")
except TypeError:
    print("Type Error Occurred")
except ValueError:
    print("Value Error Occurred")
except:
    print("Some error Occurred")
finally:
    take_card()