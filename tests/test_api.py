import unittest
from unittest.mock import patch
from app.api import Api


class TestAPI(unittest.TestCase):

    @patch('api.Api.list_user')
    def test_user_set(self, mock_list_user):

        fake_json = [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
            }
        ]

        mock_list_user.return_value.status_code = 200
        mock_list_user.return_value.json.return_value = fake_json

        resp = Api.list_user()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), fake_json)


if __name__ == "__main__":
    unittest.main(verbosity=2)
