from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        #REGISTER =======================================================================================
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data["email"]
        first_name = register_data["firstName"]
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

        #EDIT =======================================================================================
        new_name = "Changed Name"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response3, 200)

        #GET =======================================================================================
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit")


    def test_edit_without_auth(self):
        # REGISTER =======================================================================================
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        user_id = self.get_json_value(response1, "id")


        # EDIT =======================================================================================
        new_name = "Changed Name"
        auth_sid = "wrong_data"
        token = "wrong_data"
        response2 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response2, 400)

        # LOGIN =======================================================================================
        email = register_data["email"]
        password = register_data["password"]
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET =======================================================================================
        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response3,
            "firstName",
            "learnqa",
            "Имя изменилось, хотя должно было остаться неизменным")

    def test_edit_with_another_valid_creds(self):
        # REGISTER =======================================================================================
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        user_id = self.get_json_value(response1, "id")

        # LOGIN_ANOTHER_USER ===============================================================================
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response2 = MyRequests.post("/user/login", login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT =======================================================================================
        new_name = "Changed Name"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response3, 400)

        # VALID_LOGIN ===================================================================================
        email = register_data["email"]
        password = register_data["password"]
        login_data2 = {
            "email": email,
            "password": password
        }
        response5 = MyRequests.post("/user/login", login_data2)
        auth_sid2 = self.get_cookie(response5, "auth_sid")
        token2 = self.get_header(response5, "x-csrf-token")

        # GET =======================================================================================
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            "learnqa",
            "Имя изменилось, хотя должно было остаться неизменным")


    def test_edit_to_invalid_email(self):
        #REGISTER =======================================================================================
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data["email"]
        first_name = register_data["firstName"]
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

        #EDIT =======================================================================================
        new_name = "Changed Name"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": "emailexample.com"}
        )
        Assertions.assert_code_status(response3, 400)

        #GET =======================================================================================
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "email",
            email,
            "Wrong email of the user after edit")


    def test_edit_to_short_firstname(self):
        #REGISTER =======================================================================================
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data["email"]
        first_name = register_data["firstName"]
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

        #EDIT =======================================================================================
        new_name = "C"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response3, 400)

        #GET =======================================================================================
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            "learnqa",
            "Wrong name of the user after edit")