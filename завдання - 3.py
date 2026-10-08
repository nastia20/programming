def check_baggage(*weights):
    total_weight = 0

    for w in weights:
        total_weight += w
    return total_weight <= 50

