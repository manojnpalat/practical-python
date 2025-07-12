# mortgage.py
#
# Exercise 1.7
# Exercise 1.7: Dave's mortgage
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
# The interest rate is 5% and the monthly payment is $2684.11.
# Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:


def calc_fin(principal, rate, payment, extra_payment, start, end):
  total_paid = 0
  i = 1
  weight = 0

  print("i:payment:principal")
  while principal > 0:
    if i >= start and i <= end: weight = 1 
    else: weight = 0
#    print(f"i:{i}, weight:{weight}")
    extra_payment *= weight
    i = i +1 
    payment = payment+ extra_payment
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    print(f"{i} :{round(payment)} :{round(principal)}")
  
  return total_paid

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 0
start = 0
end = 0
total_paid = calc_fin(principal, rate, payment, extra_payment, 0, 0)
print(f" total_paid: {total_paid} with extra_payment:{extra_payment} from {start} to {end}")

#Exercise 1.8: Extra payments
#Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
start = 1
end = 12
total_paid = calc_fin(principal, rate, payment, extra_payment, start, end)
print(f" total_paid: {round(total_paid)} with extra_payment:{round(extra_payment)} from {start} to {end}")






