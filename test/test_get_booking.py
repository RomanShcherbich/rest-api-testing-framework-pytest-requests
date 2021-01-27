import pprint
import pytest

from src.utils.EndPointUtils import BookingEndpoint


def test_get_booking(api_client):
    url = BookingEndpoint().get_path()
    resp = api_client.get(url)
    status_code = resp.status_code
    assert status_code == 200
    resp_body_dic = resp.json()
    pprint.pprint("Booking count = {}".format(len(resp_body_dic)))
    pprint.pprint(resp.text)
    for booking_dic in resp_body_dic:
        booking_id = booking_dic['bookingid']
        assert booking_id > 0


@pytest.mark.parametrize('booking_id', [1, 2, 3, 4])
def test_get_booking_by_id(api_client, booking_id):
    url = BookingEndpoint().get_path_with_id(booking_id)
    resp = api_client.get(url)
    resp_body_dic = resp.json()
    pprint.pprint(resp.text)
    assert resp.status_code == 200
    assert resp_body_dic['firstname'] is not None
    assert type(resp_body_dic['firstname']) is str
