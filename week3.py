# Function to calculate Return on Investment (ROI)
def calculate_roi(Purchase_Price, Rental_Price, property_taxes, maintenance_cost):
  if Purchase_Price == 0:
   return None

net_income = Rental_Price - property_taxes - maintenance_cost
roi = (net_income / Purchase_Price) * 100



 # Function for displaying the menu for the user inputs
def display_menu():
    print("Real Estate ROI Calculator")
    print("----------------------------")
    print("1. Calculate ROI")
    print("2. Exit")
 
 # Function for taking user inputs
 def take_user_input():
    user_input = input("Enter your choice: ")
    return user_input
 
 # Function for displaying the menu for the user inputs
 def display_menu():
    print("Real Estate ROI Calculator")
    print("----------------------------")
    print("1. Calculate ROI")
    print("2. Exit")
 
 # Function for taking user inputs
 def take_user_input():
    user_input = input("Enter your choice: ")
    return user_input
 
 # Function for displaying the menu for the user inputs
 # Main program
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            try:
                purchase_price = float(input("Enter the purchase price: "))
                rental_income = float(input("Enter the expected rental income: "))
                property_taxes = float(input("Enter the property taxes: "))
                maintenance_expenses = float(input("Enter the maintenance expenses: "))

                # Calculate ROI
                roi = calculate_roi(purchase_price, rental_income, property_taxes, maintenance_expenses)

                # Print the ROI
                print("The Return on Investment (ROI) is {:.2f}%".format(roi))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue






