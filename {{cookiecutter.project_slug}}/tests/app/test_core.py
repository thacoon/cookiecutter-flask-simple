from faker import Faker
from flask_testing import TestCase

from app import create_app, CONFIG
from tests.app.fake import Provider


class CoreTest(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(Provider)

    def tearDown(self):
        pass

    def create_app(self):
        return create_app(CONFIG)

    def test_faker_example(self):
        self.assertEqual(self.fake.foo(), 'bar')
