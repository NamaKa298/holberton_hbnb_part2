import unittest
from Persistence import data_manager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        from Model import User
        self.user = User(id=1, name="Test User", email="test@example.com")
        pass

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
        saved_user = data_manager.get(self.user.id, type(self.user).__name__)
        data_manager.delete(saved_user, type(saved_user).__name__)
        deleted_user = data_manager.get(saved_user.id, type(saved_user).__name__)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
