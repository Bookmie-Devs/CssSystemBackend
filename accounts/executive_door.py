# the excutive door is a login view specifically design to verify
# users from the frontend who try to access the executive dashboard if
# they are staff and still active
from rest_framework.request import Request
from rest_framework.decorators import api_view
from accounts.repository import UserRepository
from rest_framework import status
from rest_framework.response import Response
from utils.utils import is_mobile


@api_view(["POST"])
def excutive_door(request: Request):
    index_number = request.data.get("index_number")
    is_executive = UserRepository.check_if_staff(index_number)
    mobile = is_mobile(request)

    print(index_number, is_executive)
    if is_executive:
        executive_relative_path = "/executive-dashboard-cb/"
        # Build the absolute URL
        absolute_url = request.build_absolute_uri(executive_relative_path)
        conext = {
            "status": "success",
            "is_executive": True,
            "executive_login": absolute_url,
        }
        if mobile:
            conext["mobile"] = True
            conext["message"] = (
                "It is recommended to access executive dashboard from laptop or desktop view"
            )
        return Response(status=status.HTTP_200_OK, data=conext)
    else:
        conext = {
            "status": "failed",
            "is_executive": False,
            "executive_login": None,
        }
        return Response(status=status.HTTP_400_BAD_REQUEST, data=conext)
