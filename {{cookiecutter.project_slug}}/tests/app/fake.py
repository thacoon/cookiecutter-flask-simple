from faker import Faker
from faker.providers import BaseProvider


fake = Faker()


class Provider(BaseProvider):
    """
    Add this new provider to faker instance with `ake.add_provider(Provider)`.
    Then it can be used as `fake.foo()`.
    Reference: https://faker.readthedocs.io
    """
    def foo(self):
        return 'bar'
