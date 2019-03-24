
def validator(inp, max_val, message):
	if inp > max_val:
		print(message)
	return min(inp, max_val)

def take_input():
	"""Helper function to take input for a user"""
	income = float(input("Gross Annual Income: ").strip())
	home_loan = float(input("Home Loan Interest Amount: ").strip())
	home_loan = validator(home_loan, 200000, "Max home loan interest deduction (200000)")
	taxsaving_80c = float(input("Tax Saving 80C: ").strip())
	taxsaving_80c = validator(taxsaving_80c, 150000, "Max home loan interest deduction (150000)")

	return income, home_loan, taxsaving_80c

def calculate_tax(income, home_loan, taxsaving_80c):
	"""Returns a number. Tax needs to be paid given income and saving details

	Arguments:
		income : float, how much annual income
		home_loan : float, how much interest paid on home loan
		taxsaving_80c: float, Investment maid to save tax.
	"""
	# your code starts here.
	income_tax = 0
	if income <= 500000:
		return income_tax
	elif income > 500000 and income <= 1000000:
		tax = 12500 + (income - taxsaving_80c - home_loan - 500000)*0.2
		income_tax = tax*1.04
	elif income > 1000000:
		tax = 112500 + (income - taxsaving_80c - home_loan - 1000000)*0.3
		income_tax = tax*1.04			

	return income_tax

def tax_calculation():
	"""Calculates Tax for given income and investment"""

	# your code starts here.
	income, home_loan, taxsaving_80c = take_input()
	print(income, home_loan, taxsaving_80c)
	income_tax = calculate_tax(income, home_loan, taxsaving_80c)
	print("Income Tax:{}".format(income_tax))


if __name__ == '__main__':
	tax_calculation()