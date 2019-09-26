from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CardTests(APITestCase):
    def test_get_random_card_visa(self):
        """Create random Visa card and test that it validates as a Visa."""
        response = self.client.get("/cards/?network=visa", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["valid"])
        self.assertIsNotNone(response.data["cc_number"])

        validate_response = self.client.post(
            "/cards/validate", {"cc_number": response.data["cc_number"]}, format="json"
        )

        self.assertEqual(validate_response.status_code, status.HTTP_200_OK)
        self.assertTrue(validate_response.data["valid"])
        self.assertEqual(validate_response.data["network"], "Visa")

    def test_get_random_card_invalid(self):
        """Attempt to create card for invalid network and confirm 200 but invalid response."""
        response = self.client.get("/cards/?network=blah", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["valid"])
        self.assertIsNone(response.data.get("cc_number"))
