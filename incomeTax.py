# income_tax.py

def calculate_tax(gross_income, num_dependents):
    """
    Calculate the income tax based on the gross income and number of dependents.

    Tax brackets:
    - 10% on the first $9,875
    - 12% on income between $9,876 and $40,125
    - 22% on income above $40,125

    Dependents:
    - $500 deduction per dependent

    :param gross_income: int, the gross income
    :param num_dependents: int, the number of dependents
    :return: int, the calculated income tax
    """
    if gross_income < 0:
        raise ValueError("Gross income cannot be negative")
    if not isinstance(num_dependents, int):
        raise ValueError("Number of dependents must be an integer")

    # Calculate the taxable income
    taxable_income = gross_income - (num_dependents * 500)

    # Calculate the tax
    if taxable_income <= 9875:
        tax = taxable_income * 0.10
    elif taxable_income <= 40125:
        tax = 987.50 + ((taxable_income - 9875) * 0.12)
    else:
        tax = 4617.50 + ((taxable_income - 40125) * 0.22)

    return int(tax)

'''
# Example usage:
gross_income = 60000
num_dependents = 2
tax = calculate_tax(gross_income, num_dependents)
print(f"The income tax is: ${tax:.2f}")
'''