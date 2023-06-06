import unittest
from game_shop.main_window.routing_logic import create_new_user

class baseline_TESTS(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_user1(self):
        result = create_new_user(email='lolkekpyk', password='2002')
        self.assertEqual('unsuccess', result)

    def test_create_user2(self):
        result = create_new_user(email='bukina@gmail.com', password='2002')
        self.assertEqual('unsuccess', result)

    def test_create_user3(self):
        result = create_new_user(email='bukina@gmail.ru', password='123123')
        self.assertEqual('unsuccess', result)

    def test_create_user4(self):
        result = create_new_user(email='0', password='')
        self.assertEqual('unsuccess', result)

    def test_create_user5(self):
        result = create_new_user(email='', password='')
        self.assertEqual('unsuccess', result)