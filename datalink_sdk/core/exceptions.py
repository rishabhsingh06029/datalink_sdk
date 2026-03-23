class DataLinkException(Exception):
    """Base exception for DataLink SDK."""
    pass


class UnsupportedDriverError(DataLinkException):
    """Raised when an unsupported database driver type is provided."""
    pass


class DataLinkConnectionError(DataLinkException):
    """Raised when a database connection attempt fails."""
    pass


class DataLinkConfigError(DataLinkException):
    """Raised when the provided configuration is invalid or incomplete."""
    pass
