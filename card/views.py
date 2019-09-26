from rest_framework.decorators import api_view
from rest_framework.response import Response

from card import credit_card


@api_view(http_method_names=["POST"])
def validate(request):
    """Validate credit card number and return details, if valid. Require POST request to prevent exposing cc number in GET params."""
    cc_number = str(request.data.get("cc_number"))

    if not cc_number.isdigit() or not credit_card.is_valid(int(cc_number)):
        return Response({"valid": False})

    try:
        pieces = credit_card.get_identifiers(int(cc_number))
        pieces["valid"] = True
        return Response(pieces)
    except:
        return Response({"valid": False})


@api_view()
def get_random(request):
    """Return random credit card number for specified CC network."""
    network = request.GET.get("network", "").lower()

    if network == "visa":
        cc_number = credit_card.get_random_visa()

    elif network == "american express":
        cc_number = credit_card.get_random_american_express()

    elif network == "discover":
        cc_number = credit_card.get_random_discover()

    elif network == "mastercard":
        cc_number = credit_card.get_random_mastercard()

    else:
        # Invalid network should still return 200,
        # while indicating that the network provided was invalid.
        return Response({"valid": False})

    return Response({"valid": True, "cc_number": cc_number})
