loan = 600_000
current_debt = loan
total_paid = 0

for i in range(1, 8):
    instalment = round((loan/7), 2)
    interest = round(current_debt * 0.06, 2)
    total_payment = instalment + interest

    print("Betaling nummer", i)
    print("Siv betaler", instalment, "i avdrag")
    print("Siv betaler", interest, "i renter")
    print("\n")

    total_paid += total_payment
    current_debt -= instalment


print("Gjenværende gjeld", round(current_debt, 2))
print("Totalt betalt:", round(total_paid, 2))