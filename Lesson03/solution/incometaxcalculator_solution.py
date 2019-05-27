
def take_input():
	"""Helper function to take input for a user"""
	#Take input and validate 
	income = float(input("Annual Income: ").strip())# input for annual income
	# input for filing status e.g. Single, Married Joint e.t.c.	
	filing_status = int(input("Filing Status [1: Single, 2: Married Joint, 3: Married separate, 4: House Head]: "))
	other_deduction = float(input("Other Monthly Deduction: "))# input for other monthly deduction.	

	return income, filing_status, other_deduction


def calculate_federal_income_tax(taxable_income):
	"""Returns the federal income tax"""
	fed_tax = 0
	if taxable_income <= 9700:
		fed_tax = taxable_income*0.1
	elif taxable_income > 9700 and taxable_income <= 39475:
		fed_tax = 9700*0.1 + (taxable_income-9700)*.12
	elif taxable_income > 39475 and taxable_income <= 84200:
		fed_tax = 9700*0.1 + (39475-9700)*0.12 + (taxable_income-39475)*0.22
	elif taxable_income > 84200 and taxable_income <= 160725:
		fed_tax = 9700*0.1 + (39475-9700)*0.12 + (84200-39475)*0.22 + (taxable_income-84200)*0.24
	elif taxable_income > 160725 and taxable_income <= 204100:
		fed_tax = 9700*0.1 + (39475-9700)*0.12 + (84200-39475)*0.22 + (160725-84200)*0.24 + (taxable_income-160725)*0.32
	elif taxable_income > 204100 and taxable_income <= 510300:
		fed_tax = 9700*0.1 + (39475-9700)*0.12 + (84200-39475)*0.22 + (160725-84200)*0.24 + (204100-160725)*.32 + (taxable_income-204100)*0.35
	elif taxable_income > 510300:
		fed_tax = 9700*0.1 + (39475-9700)*0.12 + (84200-39475)*0.22 + (160725-84200)*0.24 + (204100-160725)*0.32 + (510300-204100)*0.35 + (taxable_income-510300)*0.37

	return fed_tax


def calculate_social_security(annual_income):
	"""Return social security deduction"""
	oasdi = min(annual_income*0.062, 8239.80)
	medical_insurance = annual_income*0.0145
	social_sec = oasdi + medical_insurance
	return social_sec


def calculate_tax(income, filing_status, other_deduction):
	"""Returns Take-Home salary for given income and filing_status.

	Arguments:
		income : float, how much annual income.
		filing_status : string, filing status e.g. Single, Married Joint e.t.c.
		other_deduction: float, Other monthly deduction.
	"""
	# your code starts here.
	standard_deduction_dict = {1: 12200, 2: 24400, 3: 12200, 4: 18350}
	standard_deduction = standard_deduction_dict[filing_status]
	other_deduction *= 12 # total yearly other deduction

	taxable_income = income - standard_deduction - other_deduction
	
	if taxable_income <= 0:
		fed_tax = 0
	else:
		fed_tax = calculate_federal_income_tax(taxable_income)

	social_sec = calculate_social_security(income)

	take_home = income - other_deduction - fed_tax - social_sec

	return take_home
	

def tax_calculation():
	"""Calculates Tax for given income filing status"""

	# your code starts here.
	# call above function and print the income Tax in required_format
	income, filing_status, other_deduction = take_input()
	take_home_salary = calculate_tax(income, filing_status, other_deduction)	
	print("Take-Home Salary: {}".format(take_home_salary))

if __name__ == '__main__':
	tax_calculation()
	



