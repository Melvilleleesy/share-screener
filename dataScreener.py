from collections import defaultdict
import math

# constants
ERROR_MARGIN = 1e-6

def find_implicit_g(g, roic, wacc, pe):
        return (1 - g / roic) / (wacc - g) - pe

def screen_for_implicit_g(responses): 
    income, cashflow, balance, keymetrics = responses
    roic = keymetrics[0].get("roic", 0) if keymetrics else None 

    ev = keymetrics[0].get("enterpriseValue", 0)
    cash = balance[0].get("cashAndCashEquivalents", 0)
    preferredstock = balance[0].get("preferredStock", 0)
    minorityinterest = balance[0].get("minorityInterest", 0) 
    debt = balance[0].get("shortTermDebt", 0) + balance[0].get("longTermDebt", 0)
    equityvalue = ev - cash + debt - preferredstock - minorityinterest

    pe = equityvalue / income[0].get("netIncome", 0)
    wacc = 0.1  # will do future computation of wacc

    # Search domain: 0 <= g < min(wacc, roic)
    g_low = 0.0
    g_high = min(wacc, roic) - 1e-9  # stay clear of division by zero / negative numerator

    f_low = find_implicit_g(g_low, roic, wacc, pe)
    f_high = find_implicit_g(g_high, roic, wacc, pe)

    # If signs aren't opposite, there's no root in [g_low, g_high]
    print(f_low)
    print(f_high)
    if f_low == 0:
        return g_low
    if f_high == 0:
        return g_high
    if f_low * f_high > 0:
        return None  # no solution under the model/constraints

    # Bisection
    while True:
        g_mid = 0.5 * (g_low + g_high)
        f_mid = find_implicit_g(g_mid, roic, wacc, pe)

        if abs(f_mid) < ERROR_MARGIN or (g_high - g_low) < ERROR_MARGIN:
            return g_mid

        if f_low * f_mid < 0:
            g_high, f_high = g_mid, f_mid
        else:
            g_low, f_low = g_mid, f_mid

    # didn't converge within max_iter
    return str(0.5 * (g_low + g_high))

def screen_data(responses):
    return screen_for_implicit_g(responses)
    


