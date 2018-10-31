#!/usr/bin/python3

def calculate_total_cost(m_cost, tip_pct, tax_pct):
    """ Calculate the total meal cost (including tip and tax) """
    tip = (m_cost * tip_pct) / 100
    tax = (m_cost * tax_pct) / 100
    total = round(m_cost + tip + tax, 0)

    return total

def main():
    """ Main method """
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    total_cost = calculate_total_cost(meal_cost, tip_percent, tax_percent)

    print(int(total_cost))

if __name__ == '__main__':
    main()

    
    
