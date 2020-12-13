def test_restful_booker_auth(api_client, token):
    assert token is not None
    assert type(token) is str
    assert len(token) >= 15

