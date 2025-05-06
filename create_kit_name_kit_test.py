import sender_stand_request
import data

def get_auth_token():
    response = sender_stand_request.post_new_user(data.user_body)
    assert response.status_code == 201
    return response.json()["authToken"]

def get_kit_body(name_kit):
    current_body =data.kit_body.copy()
    current_body["name"] = name_kit
    return current_body


def positive_assert (kit_body):
    token = get_auth_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    kit_response_json = response.json()
    assert kit_response_json["name"] == kit_body["name"]

def negative_assert(kit_body):
    token = get_auth_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

def test_min_characters_kit_name():
    body = get_kit_body("a")
    positive_assert(body)

def test_max_characters_kit_name():
    body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(body)

def test_kit_name_empty_string():
    body = get_kit_body("")
    negative_assert(body)

def test_kit_name_too_long():
    body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(body)

def test_kit_name_special_characters():
    body = get_kit_body("!№%@,")
    positive_assert(body)

def test_kit_name_spaces():
    body = get_kit_body(" A Aaa ")
    positive_assert(body)

def test_kit_name_numbers():
    body = get_kit_body("123")
    positive_assert(body)

def test_kit_name_missing_field():
    body = data.kit_body.copy()
    del body["name"]
    negative_assert(body)

def test_kit_name_as_number_type():
    body = get_kit_body(123)
    negative_assert(body)







