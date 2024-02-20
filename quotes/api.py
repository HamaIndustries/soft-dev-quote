import json

from django.http import HttpRequest, HttpResponse, response

def login_api(request: HttpRequest):
    """
    Accepts JSON object containing username and (hashed) password

    responds with success and session info if valid.
    """
    pass

def registration_api(request: HttpRequest):
    """
    Accepts JSON object containing registration info

    responds with success if data is valid.
    """

def quote_history_api(request: HttpRequest):
    """
    Accepts JSON object describing requested user and filters, and responds with JSON object containing list of quote history entries.
    """
    fake_quote_data = [
        {"id": 1, "name": "huuuuge big contract", "cost": 12.00, "date": "2024-02-03"},
        {"id": 56, "name": "burger", "cost": 2.00, "date": "2024-02-05"},
        {"id": 23453, "name": "really expensive burger construction", "cost": 10000000.00, "date": "2024-02-22"},
        {"id": 43, "name": "dirt but if it was awesome", "cost": 0.69, "date": "2024-02-16"},
    ]

    resp_body = {
        "data": fake_quote_data,
        "page_count": 20,
        "current_page": 1,
        "sort": "asc"
    }

    return HttpResponse(json.dumps(resp_body), content_type="application/json", status=200) # pretend database responds with modified accepted data

def quote_form_api(request: HttpRequest):
    """
    Accepts JSON object describing quote request, and responds with success if valid.
    Should provide an "id" field that is 0 if creating a new form, and >0 if editing an existing one with that id.
    there should also be a delete method. (CRUD)
    """

    try:
        data = json.loads(request.body)
        print("Received json content:")
        print(data)

        if "id" in data and data["id"] == 0:
            data["id"] = 69 # pretend the database created a new form
        return HttpResponse(json.dumps(data), content_type="application/json", status=200) # pretend database responds with modified accepted data
    except json.JSONDecodeError:
        print(f"failed to parse JSON data: {request.body}")
        raise