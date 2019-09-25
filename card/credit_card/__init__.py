import random

from card.credit_card.credit_card import (
    INDUSTRY_ASSIGNMENT,
    NETWORK_AMERICAN_EXPRESS,
    NETWORK_DISCOVER,
    NETWORK_MASTERCARD,
    NETWORK_OTHER,
    NETWORK_PREFIXES,
    NETWORK_VISA,
    generate_number,
    get_identifiers,
    get_network,
    is_valid,
)


def get_random_visa() -> int:
    """Generate random Visa number based on predefined prefixes/length."""
    return generate_number(
        random.choice(credit_card.NETWORK_PREFIXES[credit_card.NETWORK_VISA]),
        credit_card.LENGTH_VISA,
    )


def get_random_american_express() -> int:
    """Generate random AmEx number based on predefined prefixes/length."""
    return generate_number(
        random.choice(
            credit_card.NETWORK_PREFIXES[credit_card.NETWORK_AMERICAN_EXPRESS]
        ),
        credit_card.LENGTH_AMERICAN_EXPRESS,
    )


def get_random_discover() -> int:
    """Generate random Discover number based on predefined prefixes/length."""
    return generate_number(
        random.choice(credit_card.NETWORK_PREFIXES[credit_card.NETWORK_DISCOVER]),
        credit_card.LENGTH_DISCOVER,
    )


def get_random_mastercard() -> int:
    """Generate random Mastercard number based on predefined prefixes/length."""
    return generate_number(
        random.choice(credit_card.NETWORK_PREFIXES[credit_card.NETWORK_MASTERCARD]),
        credit_card.LENGTH_MASTERCARD,
    )


__all__ = [
    "get_identifiers",
    "get_random_visa",
    "get_random_american_express",
    "get_random_discover",
    "get_random_mastercard",
    "is_valid",
    "INDUSTRY_ASSIGNMENT",
    "NETWORK_AMERICAN_EXPRESS",
    "NETWORK_DISCOVER",
    "NETWORK_MASTERCARD",
    "NETWORK_OTHER",
    "NETWORK_PREFIXES",
    "NETWORK_VISA",
]
