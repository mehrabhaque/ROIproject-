# Function to measure Return on Investment (ROI)
def Measure_roi(purchase_price, rental_income, property_taxes, maintenance_expenses):
   
    net_income = rental_income - property_taxes - maintenance_expenses
    
    roi = (net_income / purchase_price) * 100
    
    return roi 




# Function to display the menu and handle user input
def display_menu(): 

    # Display the menu
    print("Welcome to RealRoi!")
    print("Calculate your RealRoi")
    print("---------------")
    print("1. Measure ROI")
    print("2. Exit")

 # Main program loop
 
if __name__ == "__main__": 

    while True:
        display_menu()
        choice = input("Press 1 to start, Press 2 to quit: ")

        if choice == "1":
            try:
                purchase_price = float(input("Enter the purchase price: "))
                rental_income = float(input("Enter the expected rental income: "))
                property_taxes = float(input("Enter the property taxes: "))
                maintenance_expenses = float(input("Enter the maintenance expenses: "))

                # Calculate ROI
                roi = calculate_roi(purchase_price, rental_income, property_taxes, maintenance_expenses)

                # Print the ROI
                print("The Return on Investment (ROI) is  {:.2f}%".format(roi)) 

            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "2":
            print("Exiting RealRoi.")
            break
        else:
            print("Invalid choice.")

            
