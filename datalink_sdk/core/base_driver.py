class BaseDriver:
    """
    Base driver class for DataLink SDK.
    All database drivers must inherit from this class.
    """

    def __init__(self, config: dict):
        self.config = config

    def connect(self):
        raise NotImplementedError("connect() method must be implemented by the driver subclass.")
