from django.test import TestCase

from card import credit_card


class TestValidation(TestCase):
    def test_validate_cards(self):
        test_card_numbers = [
            (49927398716, True),
            (49927398717, False),
            (1234567812345678, False),
            (1234567812345670, True),
        ]

        for num, valid in test_card_numbers:
            self.assertEqual(credit_card.is_valid(num), valid)


class TestIdentification(TestCase):
    def test_assertion_fails_for_invalid_number(self):
        with self.assertRaises(AssertionError):
            credit_card.get_identifiers(123)

    def test_get_network(self):
        networks = [
            ("44", credit_card.NETWORK_VISA),
            ("55", credit_card.NETWORK_MASTERCARD),
            ("33", credit_card.NETWORK_AMERICAN_EXPRESS),
            ("37", credit_card.NETWORK_AMERICAN_EXPRESS),
            ("6011", credit_card.NETWORK_DISCOVER),
            ("644", credit_card.NETWORK_DISCOVER),
            ("65", credit_card.NETWORK_DISCOVER),
            ("77", credit_card.NETWORK_OTHER),
        ]

        for prefix, network in networks:
            self.assertEqual(credit_card.get_network(prefix), network)

    def test_get_identifiers(self):
        number = 49927398716
        identifiers = credit_card.get_identifiers(number)
        self.assertEqual(identifiers["mii"], 4)
        self.assertEqual(identifiers["industry"], credit_card.INDUSTRY_ASSIGNMENT["4"])
        self.assertEqual(identifiers["bin"], 499273)
        self.assertEqual(identifiers["account"], 9871)
        self.assertEqual(identifiers["checksum"], 6)
        self.assertEqual(identifiers["network"], "Visa")

    def test(self):
        for _ in range(10):
            self.assertIsNotNone(credit_card.get_random_visa())

        for _ in range(10):
            self.assertIsNotNone(credit_card.get_random_american_express())

        for _ in range(10):
            self.assertIsNotNone(credit_card.get_random_mastercard())

        for _ in range(10):
            self.assertIsNotNone(credit_card.get_random_discover())
