'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
   def savings(gross_pay, tax_rate, expenses):
    take_home_pay=(int((gross_pay*100) - (gross_pay*tax_rate)) - expenses*100)
    return take_home_pay
gross_pay=int(input("Input Gross Pay Here in whole Pesos:"))
tax_rate=float(input("Input Tax Rate Here:"))
expenses=int(input("Input Expenses Here in whole Pesos"))
print("The employee has ", savings(gross_pay, tax_rate, expenses), " centavos remaining from his/her gross pay after taxes and expenses")

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
   def material_waste(total_material, material_units, num_jobs, job_consumption):
    materials_used= (num_jobs*job_consumption)
    materials_available=(total_material - materials_used)
    return materials_available
    
total_material=int(input("Input total materials available here:"))
material_units =str(input("Input material unit available here:"))
num_jobs = int(input("Input number of jobs to run here:"))
job_consumption = int(input("Input the amnount of materials consumed per job here:"))

def interest(principal, rate, periods):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
   def interest(principal, rate, periods):
    sim_interest=(principal*100*rate*periods)
    new_principle=(sim_interest+principal)
    return new_principle
principal=int(input("Input the amount invested in Pesos here:"))
rate= float(input("Input the  the interest rate per period, expressed as a decimal representation of a percentage here:"))
periods= int(input("Input the number of periods invested in Pesos here:"))

print("The final value of the investment is ", int(interest(principal, rate, periods)),"centavos",sep='')



def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    def body_mass_index(weight, height):
    
    weight_kg = weight / 2.205
    height_m = (float(height[0]) * 0.3048) + float(float(height[1:]) * 0.0254)
    bmi = weight_kg / (height_m ** 2)
    return bmi

    
weight= float(input("Input your weight in pounds here:"))
height_x=input("Input your height:")
digits_only = ""

for i in height_x:
    if i.isdigit():
        digits_only += i

height=(digits_only)

print("Your BMI is ", body_mass_index(weight, height))
