
def take_input():
	"""Helper function to take input for a user"""
	#Take input and validate 
	income = # your code, input for annual income
	# input for filing status e.g. Single, Married Joint e.t.c.	
	filing_status = int(input("Filing Status [1: Single, 2: Married Joint, 3: Married separate, 4: House Head]: "))
	other_deduction = # your code, input for other monthly deduction.	

	return income, filing_status, other_deduction


def calculate_federal_income_tax(taxable_income):
	"""Returns the federal income tax"""
	fed_tax = 0
	if taxable_income <= 9700:
		fed_tax = # your code
	elif taxable_income > 9700 and taxable_income <= 39475:
		fed_tax = # your code
	elif taxable_income > 39475 and taxable_income <= 84200:
		fed_tax = # your code
	elif taxable_income > 84200 and taxable_income <= 160725:
		fed_tax = # your code
	elif taxable_income > 160725 and taxable_income <= 204100:
		fed_tax = # your code
	elif taxable_income > 204100 and taxable_income <= 510300:
		fed_tax = # your code
	elif taxable_income > 510300:
		fed_tax = # your code

	return fed_tax


def calculate_social_security(annual_income):
	"""Return social security deduction"""
	oasdi = # calculate minimum of $8239.80 or oasdi
	medical_insurance = # medical portion 1.45%
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

	taxable_income = #your code

	if taxable_income <= 0:
		fed_tax = # your code
	else:
		fed_tax = # call calculate_federal_income_tax()

	social_sec = calculate_social_security(income)

	take_home = # calculate take-home salary

	return take_home
	

def tax_calculation():
	"""Calculates Tax for given income filing status"""

	# your code starts here.
	# call above function and print the income Tax in required_format
	income, filing_status, other_deduction = #your code take input here
	take_home_salary = # your code
	print("Take-Home Salary: {}".format(take_home_salary))

if __name__ == '__main__':
	tax_calculation()
	



