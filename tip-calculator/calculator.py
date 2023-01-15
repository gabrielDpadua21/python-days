

def tip(bill, split, percentage):
    float_percent = percentage / 100
    total = bill + (bill * float_percent)
    return round((total / split), 2);