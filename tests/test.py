import unittest
from Model.user import User
from Model.place import Places
from Persistence.datamanager import data_manager
from API.v1.app import db
from sqlalchemy.exc import IntegrityError

class DatabaseOperationsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configuration pour utiliser une base de données de test
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Nettoyage après les tests
        db.session.remove()
        db.drop_all()

    def test_create_user_db(self):
        # Test de création d'un utilisateur via la base de données
        user = User(email="test@example.com")
        db.session.add(user)
        db.session.commit()
        self.assertIsNotNone(user.id)

    def test_duplicate_user_db(self):
        # Test de la contrainte d'unicité de l'email
        user1 = User(email="unique@example.com")
        db.session.add(user1)
        db.session.commit()
        user2 = User(email="unique@example.com")
        db.session.add(user2)
        with self.assertRaises(IntegrityError):
            db.session.commit()

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User(email="test@example.com")
        self.assertEqual(user.email, "test@example.com")

    def test_email_uniqueness(self):
        User.create(email="test1@example.com")
        with self.assertRaises(ValueError):
            User.create(email="test1@example.com")

    def test_created_at_updated_at(self):
        user = User.create(email="test@example.com")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_user_uniqueness(self):
        User.create(email="test1@example.com")
        with self.assertRaises(ValueError):
            User.create(email="test1@example.com")

    def test_update_user(self):
        user = User.create(email="test@example.com", name="Old Name")
        user.name = "New Name"
        self.assertEqual(user.name, "New Name")

    def test_user_creation_validation(self):
        with self.assertRaises(ValueError):
            User.create(email="invalid email")


class TestPlaces(unittest.TestCase):
    def test_create_place(self):
        user = User.create(email="test@example.com")
        place = Places.create(user)
        self.assertEqual(place.host, user)

    def test_host_is_user(self):
        with self.assertRaises(ValueError):
            Places.create("not a user instance")

    def test_place_creation(self):
        user = User.create(email="test@example.com")
        place = Places.create(user, name="Place Name", description="Place Description")
        self.assertEqual(place.name, "Place Name")
        self.assertEqual(place.description, "Place Description")

    def test_host_assignment_rules(self):
        user1 = User.create(email="test1@example.com")
        user2 = User.create(email="test2@example.com")
        place = Places.create(user1)
        with self.assertRaises(ValueError):
            place.host = user2

    def test_place_attribute_validation(self):
        user = User.create(email="test@example.com")
        with self.assertRaises(ValueError):
            Places.create(user, latitude=200, longitude=200)

    def test_deleting_places(self):
        user = User.create(email="test@example.com")
        place = Places.create(user)
        user.places.remove(place)
        self.assertNotIn(place, user.places)

    def test_amenity_addition(self):
        user = User.create(email="test@example.com")
        place = Places.create(user)
        amenity = "Pool"
        place.amenities.append(amenity)
        self.assertIn(amenity, place.amenities)

    def test_retrieve_update_amenities(self):
        user = User.create(email="test@example.com")
        place = Places.create(user)
        amenity = "Pool"
        place.amenities.append(amenity)
        self.assertIn(amenity, place.amenities)
        place.amenities.remove(amenity)
        self.assertNotIn(amenity, place.amenities)
    
    def test_create_user_invalid_email(self):
        with self.assertRaises(ValueError):
            User.create(email="invalid email", first_name="Test", last_name="User")
    
    if __name__ == '__main__':
        unittest.main()