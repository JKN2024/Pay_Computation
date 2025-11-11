# Computing pay usung Functions
def computepay(hours, rate):
    if hours > 40:
        # Calculate overtime hours
        overtime = hours - 40
        # Regular pay for 40 hours + overtime pay (1.5 times the rate)
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        # No overtime
        pay = hours * rate
    return pay

# Get input from user
hrs = float(input("Enter Hours: "))
rte = float(input("Enter Rate: "))

# Call the function
p = computepay(hrs, rte)
print(p)
