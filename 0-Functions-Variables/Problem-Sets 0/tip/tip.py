def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    remove_dollar = d.replace("$", "")
    return float(remove_dollar)


def percent_to_float(p):
    remove_percent = p.replace("%", "")
    percent = float(remove_percent)
    return percent / 100


main()

# test cases
# $50.00, 15% should return $7.50
# $100.00, 18% should return $18.00
# $15.00, 25% should return $3.75


# check50 cs50/problems/2022/python/tip

# submit50 cs50/problems/2022/python/tip
