import unittest

# Example number 1
class TestStringMethods(unittest.TestCase):

    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    def test_isalnum(self):
        self.assertTrue('kunt14rs0'.isalnum())
        self.assertFalse('kunt!4rs0'.isalnum())

    def test_index(self):
        name = 'kuntiarso'
        self.assertEqual(name.index('r'), 6)
        with self.assertRaises(ValueError):
            name.index('hello')


# Example number 2
def connect_to_db():
    print('Connected to database')

def disconnect_from_db(db):
    print('Tidak terhubung ke database: {}'.format(db))

class User:

    username = ''
    active = False

    def __init__(self, db, username) -> None:
        self.username = username

    def set_active(self):
        self.active = True

class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = connect_to_db()
        self.kuntiarso = User(self.db, 'kuntiarso')

    def tear_down(self):
        disconnect_from_db(self.db)

    def test_user_default_not_active(self):
        self.assertFalse(self.kuntiarso.active) # not active by default

    def test_user_is_active(self):
        self.kuntiarso.set_active()
        self.assertTrue(self.kuntiarso.active)

if __name__ == '__main__':
    unittest.main()
