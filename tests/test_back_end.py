import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Users, Tanks
from os import getenv


class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DATABASE'),
                SECRET_KEY=getenv('SKEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        test1 = Users(first_name="admin", last_name="admin",
                      email="admin@admin.com")

        # create test non-admin user
        test2 = Users(first_name="test", last_name="user",
                      email="test@user.com")

        # save users to database
        db.session.add(test1)
        db.session.add(test2)
        db.session.commit()

    def tearDown(self):

        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


class TestTanks(TestBase):

    def test_add_new_tank(self):

        with self.client:
            self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com'),
                follow_redirects=True)
            response = self.client.post(
                url_for('tanks'),
                data=dict(
                    name="Fishy Tank",
                    description="",
                    ammonia=0.1,
                    nitrate=0,
                    nitrite=2),
                follow_redirects=True)
            self.assertIn(b'Fishy Tank', response.data)

class TestLogout(TestBase):
    def test_logout(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com'),
                follow_redirects=True)
        self.client.post(url_for('logout'),
                follow_redirects=True)
        response=self.client.get('home')
        self.assertIn(b'home',response.data)

class TestDelete(TestBase):
    def test_delete_account(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com'),
                follow_redirects=True)
        self.client.post(url_for('account'),
                follow_redirects=True)
        self.client.post(url_for('account_delete'),
                follow_redirects=True)
        response = self.client.get(url_for('login'))
        self.assertIn(b'Login',response.data)

class TestRegistration(TestBase):
    def test_register_account(self):
        self.client.post(
            url_for('register'),
            data=dict(
                first_name='Tobias',
                last_name='Jackson',
                email='tj@tj.com'),
            follow_redirects=True)
        response=self.client.get('login')
        self.assertIn(b'Login',response.data)

class TestRegLogin(TestBase):
    def test_reglogin(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com'),
                follow_redirects=True)
        response = self.client.post(
            url_for('register'),
            follow_redirects=True)
        self.client.get(url_for('home'))
        self.assertIn(b'Account',response.data) 