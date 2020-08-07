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
        test1 = Users(first_name="admin", last_name="admin", email="admin@admin.com")

        # create test non-admin user
        test2 = Users(first_name="test", last_name="user", email="test@user.com")

        # save users to database
        db.session.add(test1)
        db.session.add(test2)
        db.session.commit()

    def tearDown(self):

        ##Will be called after every test
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
            response = self.client.post(
                '/tanks',
                data=dict(
                    name="Fishy Tank",
                    description="Test Tank",
                    ammonia=0.01,
                    nitrate=0,
                    nitrite=2
                ),
                follow_redirects=True
            )
            self.assertIn(b'Fishy Tank', response.data)

