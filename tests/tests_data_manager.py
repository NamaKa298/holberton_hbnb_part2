import unittest
from Model.DataManager import DataManager
from Model.User import User

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.datamanager = DataManager()
        self.user = User(id=1, name="Test User", email="test@example.com")

    def testsaveandget(self):
        self.datamanager.save(self.user)
        retrieveduser = self.datamanager.get(self.user.id, type(self.user).__name__)
        self.assertEqual(retrieveduser, self.user)

    def testupdate(self):
        self.datamanager.save(self.user)
        self.user.name = "Updated User"
        self.data_manager.update(self.user)
        updated_user = self.data_manager.get(self.user.id, type(self.user).__name__)
        self.assertEqual(updated_user.name, "Updated User")

    def test_delete(self):
        self.data_manager.save(self.user)
        self.data_manager.delete(self.user.id, type(self.user).__name__)
        deleted_user = self.data_manager.get(self.user.id, type(self.user).__name__)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
