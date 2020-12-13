import pytest
import json

from src.utils.EndPointUtils import BookingEndpoint

BODY_ROMAN_SHCHERBICH = {"firstname": "Roman", "lastname": "Shcherbich", "totalprice": 777, "depositpaid": True,
                         "bookingdates": {"checkin": "2021-01-14", "checkout": "2021-01-16"},
                         "additionalneeds": "Breakfast, Bicycle"}
BODY_YULIYA_SHCHERBICH = {"firstname": "Yuliya", "lastname": "Shcherbich", "totalprice": 524, "depositpaid": False,
                          "bookingdates": {"checkin": "2021-01-14", "checkout": "2022-01-16"},
                          "additionalneeds": None}


@pytest.mark.parametrize('booking_id, booking_body_dic',
                         [(1, BODY_ROMAN_SHCHERBICH),
                          (2, BODY_YULIYA_SHCHERBICH)],
                         ids=["{} {}".format(BODY_ROMAN_SHCHERBICH['firstname'], BODY_ROMAN_SHCHERBICH['lastname']),
                              "{} {}".format(BODY_YULIYA_SHCHERBICH['firstname'], BODY_YULIYA_SHCHERBICH['lastname'])])
def test_update_booking_by_id(api_client, token, default_headers, booking_id, booking_body_dic):
    token_cookie = "token={}".format(token)
    default_headers.update(Accept="application/json", Cookie=token_cookie)
    url = BookingEndpoint().get_path_with_id(booking_id)
    resp = api_client.put(url, data=json.dumps(booking_body_dic), headers=default_headers)
    assert resp.status_code == 200
    assert resp.json() == booking_body_dic
