import unittest
from Persistence.datamanager import data_manager
from Model.user import User

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.user = User(id=1, name="Test User", email="test@example.com")

    def testsaveandget(self):
        data_manager.save(self.user)
        retrieveduser = data_manager.get(self.user.id, type(self.user).__name__)
        self.assertEqual(retrieveduser, self.user)

    def testupdate(self):
        data_manager.save(self.user)
        self.user.name = "Updated User"
        data_manager.update(self.user)
        updated_user = data_manager.get(self.user.id, type(self.user).__name__)
        self.assertEqual(updated_user.name, "Updated User")

    def test_delete(self):
        data_manager.save(self.user)
        data_manager.delete(self.user.id, type(self.user).__name__)
        deleted_user = data_manager.get(self.user.id, type(self.user).__name__)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
