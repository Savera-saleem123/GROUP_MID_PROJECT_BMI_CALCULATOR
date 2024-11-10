# BMI Calculator code

# to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # BMI formula: weight (kg) / (height (m))^2
    return bmi

# to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5: #this if,elif,else function is used to classify the data ,if is used when the statment is true
        return "Underweight"
    elif 18.5 <= bmi < 24.9: #elif is used for the multiple conditions
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity" #else is used to excecute the code when all the conditions are false

# Main function to run the program(its a function that takes the users data and execute in terminal)
def main():
    print("Welcome to the BMI Calculator!")

    # Taking user input for weight and height
    weight = float(input("Enter your weight in kilograms (kg): ")) #float is used, here because the upcoming data might be in decimal 
    height = float(input("Enter your height in meters (m): "))

    # Calculating BMI
    bmi = calculate_bmi(weight, height)

    # Determining BMI category
    category = bmi_category(bmi)

    # Displaying the result
    print(f"Your BMI is: {bmi:.2f}") #the 2f is used here to restrict or round off the data upto two decimal
    print(f"Category: {category}") #this f function enhance the readibility

# This will run the main function if the script is executed
if __name__ == "__main__": #this line ensures that if the data is directly run,so it executes in this main function
    main()
