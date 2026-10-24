def wait_until(price, budget, annual_savings, inflation, interest):
    years = 0
    
    while (budget < price):
        budget = (budget * (1 + interest)) + annual_savings
        price *= 1 + inflation
        years += 1
        
    return years

print(wait_until(25000, 12000, 2500, 0.02, 0.01))