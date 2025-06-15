class StancerAPIError(Exception):
    pass


class AuthenticationError(StancerAPIError):
    pass


class ResourceNotFoundError(StancerAPIError):
    pass


class NetworkError(StancerAPIError):
    pass
