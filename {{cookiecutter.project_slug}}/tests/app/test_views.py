from faker import Faker
from flask import url_for
from flask_testing import TestCase

from app import create_app, CONFIG
from tests.app.fake import Provider


class ViewsTest(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(Provider)

        self.app = self.create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def create_app(self):
        return create_app(CONFIG)

    def test_hello_world(self):
        self.client.get(url_for('core.hello'))
