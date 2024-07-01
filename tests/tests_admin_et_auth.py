import unittest
from API.v1.app import db, app
app.app_context().push()
from flask_jwt_extended import create_access_token

class RBACTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()
        
    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def test_login_access(self):
        # Test d'accès autorisé
        with app.test_client() as client:
            response = client.post('/auth/login', json={'username': 'user_test', 'password': 'password_test'})
            self.assertEqual(response.status_code, 400)

        # Test d'accès non autorisé
        with app.test_client() as client:
            response = client.post('/auth/login', json={'username': 'wrong_user', 'password': 'wrong_password'})
            self.assertEqual(response.status_code, 400)

    def test_admin_access(self):
        # Création d'un token avec les droits administrateur
        admin_token = create_access_token(identity='admin_user', additional_claims={"is_admin": True})
        # comment créer des tokens (rechercher sur internet) 
        # Création d'un token sans les droits administrateur
        user_token = create_access_token(identity='simple_user')

        # Test d'accès autorisé pour l'administrateur
        with app.test_client() as client:
            response = client.get('/admin/some_admin_endpoint', headers={'Authorization': f'Bearer {admin_token}'})
            self.assertEqual(response.status_code, 404)

        # Test d'accès non autorisé pour un utilisateur simple
        with app.test_client() as client:
            response = client.get('/admin/some_admin_endpoint', headers={'Authorization': f'Bearer {user_token}'})
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
