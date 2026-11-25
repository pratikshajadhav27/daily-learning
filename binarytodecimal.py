def binary_to_decimal(binary_str):
    decimal = 0
    for bit in binary_str:
        decimal = decimal * 2 + int(bit)
    return decimal