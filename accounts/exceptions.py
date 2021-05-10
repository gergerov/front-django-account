from rest_framework.response import Response


class IncorrectRequestData(Exception):
    data = {"error": True, "message": "incorrect request data"}
    message = "incorrect request data"
    response = Response(status=400, data=data)


# confirmations
class DoesNotExistsConfirmation(Exception):
    data = {"error": True, "message": "not exists confirmation"}
    message = "not exists confirmation"
    response = Response(status=400, data=data)


class UsedConfirmation(Exception):
    data = {"error": True, "message": "is used confirmation"}
    message = "is used confirmation"
    response = Response(status=400, data=data)


class IncorrectConfirmationType(Exception):
    data = {"error": True, "message": "incorrect confirmation type"}
    response = Response(status=400, data=data)
    message = "incorrect confirmation type"


class InactiveUser(Exception):
    data = {"error": True, "message": "inactive user"}
    response = Response(status=400, data=data)
    message = "inactive user"


class DoesNotExistsUsername(Exception):
    data = {"error": True, "message": "not exists username"}
    response = Response(status=400, data=data)
    message = "not exists username"


# user/password
class IncorrectUsernameOrPassword(Exception):
    data = {"error": True, "message": "Incorrect username or password"}
    response = Response(status=403, data=data)
    message = "Incorrect username or password"


class ExistsEmail(Exception):
    data={"error": True, "message": "exists email"}
    response = Response(status=400, data=data)
    message = "exists email"


class ExistsUsername(Exception):
    data={"error": True, "message": "exists username"}
    response = Response(status=400, data=data)
    message = "exists username"


class IncorrectEmail(Exception):
    data={"error": True, "message": "incorrect email"}
    response = Response(status=400, data=data)
    message = "incorrect email"


class IncorrectUsername(Exception):
    data={"error": True, "message": "incorrect username"}
    response = Response(status=400, data=data)
    message = "incorrect username"


class IncorrectAccountProfileType(Exception):
    data = {"error": True, "message": "incorrect account_profile_type"}
    response = Response(status=400, data=data)
    message = "incorrect account_profile_type"

