# Credit Card Validator

## Purpose

Provides API endpoints to validate an existing credit card number based on Luhn's algorithm, and generate valid credit card numbers at random for a given network.

## Install

*This assumes your computer has Python 3.7 and Virtualenv installed.*

```bash
$ git clone https://github.com/jhtimmins/credit-card-validator.git

$ cd credit-card-validator

$ virtualenv -p python3.7 virtualenv

$ source virtualenv/bin/activate.sh

$ pip install -r requirements.txt
```

## Run Tests

```bash
$ python manage.py test
```

## Run Server

```bash
$ python manage.py runserver
```

## Available Endpoints

### GET /cards/?network={network}

Returns a random card number for the specified network.

```bash
$ http 127.0.0.1:8000/cards/?network=visa
HTTP/1.1 200 OK
Allow: OPTIONS, GET
Content-Length: 43
Content-Type: application/json
Date: Thu, 26 Sep 2019 02:25:18 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "cc_number": 4259529325868188,
    "valid": true
}

```

### POST /cards/validate

Validates credit card number and returns details if valid.

```bash
$ http POST 127.0.0.1:8000/cards/validate cc_number=4259529325868188
HTTP/1.1 200 OK
Allow: OPTIONS, POST
Content-Length: 120
Content-Type: application/json
Date: Thu, 26 Sep 2019 02:26:56 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "account": 932586818, 
    "bin": 425952, 
    "checksum": 8, 
    "industry": "Banking and Financial", 
    "mii": 4, 
    "network": "Visa", 
    "valid": true
}
```
