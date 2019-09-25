import random

NETWORK_VISA = "Visa"
NETWORK_DISCOVER = "Discover"
NETWORK_MASTERCARD = "Mastercard"
NETWORK_AMERICAN_EXPRESS = "American Express"
NETWORK_OTHER = "Other"

INDUSTRY_ASSIGNMENT = {
    "1": "Airline",
    "2": "Airline",
    "3": "Travel and Entertainment",
    "4": "Banking and Financial",
    "5": "Banking and Financial",
    "6": "Merchandising and Finance",
    "7": "Petroleum",
    "8": "Telecommunications",
    "9": "National Assignment",
}

NETWORK_PREFIXES = {
    NETWORK_VISA: ("4"),
    NETWORK_MASTERCARD: ("5"),
    NETWORK_AMERICAN_EXPRESS: ("3", "37"),
    NETWORK_DISCOVER: ("6011", "644", "65"),
}

LENGTH_VISA = 16
LENGTH_DISCOVER = 16
LENGTH_MASTERCARD = 16
LENGTH_AMERICAN_EXPRESS = 15


def is_valid(number: int) -> bool:

    if number <= 0:
        return False

    as_string = str(number)
    reverse = as_string[::-1]

    odd_digits = reverse[::2]
    odd_sum = sum(int(i) for i in odd_digits)

    even_digits = reverse[1::2]
    doubled_even_digits = [int(i) * 2 for i in even_digits]
    summed_digits_for_even_doubles = [i // 10 + i % 10 for i in doubled_even_digits]
    sum_of_even_digit_sums = sum(summed_digits_for_even_doubles)

    return (sum_of_even_digit_sums + odd_sum) % 10 == 0


def get_identifiers(number: int) -> dict:
    assert is_valid(number)
    as_string = str(number)

    pieces = {}
    pieces["mii"] = int(as_string[0])
    pieces["industry"] = INDUSTRY_ASSIGNMENT[as_string[0]]
    pieces["bin"] = int(as_string[:6])
    pieces["account"] = int(as_string[6:-1])
    pieces["checksum"] = int(as_string[-1])
    pieces["network"] = get_network(as_string)

    return pieces


def generate_number(prefix: str, length: int) -> int:
    interior_pieces = [
        str(random.randint(0, 9)) for _ in range(length - len(prefix) - 1)
    ]
    interior_value = "".join(interior_pieces)
    options = [prefix + interior_value + str(i) for i in range(10)]
    for option in options:
        if is_valid(int(option)):
            return int(option)

    return None


def get_network(number: str) -> str:
    for network, prefixes in NETWORK_PREFIXES.items():
        if number.startswith(prefixes):
            return network

    return NETWORK_OTHER
