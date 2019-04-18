def find_missing(arry1, arry2):
    missing_elements = []
    for e in arry1:
        if e not in arry2:
            missing_elements.append(e)
    return missing_elements

def find_missing_with_sets(arry1, arry2):
    missing_elements = set(arry1) - set(arry2)
    return list(missing_elements)

def find_missing_xor(arry1, arry2):
    xor_sum = 0
    for num in arry1:
        xor_sum ^= num
    for num in arry2:
        xor_sum ^= num
    
    return xor_sum
