class AppCoreError(Exception):
    """
    Basic exception for errors raised by modules in app.core,
    Reference: https://julien.danjou.info/python-exceptions-guide/
    """
    def __init__(self, msg=None):
        if msg is None:
            msg = "AppError Exception was raised."

        super().__init__(msg)
