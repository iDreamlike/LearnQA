from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserDelete(BaseCase):
    def test_delete_user_2(self):
        # LOGIN =======================================================================================
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = MyRequests.post("/user/login", login_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        #DELETE  =======================================================================================
        response2 = MyRequests.delete(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response2, 400)


    def test_delete_just_created_user(self):
        #REGISTER =======================================================================================
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        #LOGIN =======================================================================================
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", login_data)
        auth_sid = self.get_cookie(response2,"auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #DELETE =======================================================================================
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response3, 200)

        #GET =======================================================================================
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response4, 404)


    def test_delete_user_with_another_creds(self):
        #REGISTER first user ===========================================================================
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # REGISTER second user ===========================================================================
        register_data_2 = self.prepare_registration_data()
        response1_1 = MyRequests.post("/user/", data=register_data_2)
        Assertions.assert_code_status(response1_1, 200)
        Assertions.assert_json_has_key(response1_1, "id")
        user_id_2 = self.get_json_value(response1_1, "id")


        #LOGIN =======================================================================================
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", login_data)
        auth_sid = self.get_cookie(response2,"auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #DELETE =======================================================================================
        response3 = MyRequests.delete(
            f"/user/{user_id_2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response3, 400)

        #GET =======================================================================================
        response4 = MyRequests.get(
            f"/user/{user_id_2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response4, 200)