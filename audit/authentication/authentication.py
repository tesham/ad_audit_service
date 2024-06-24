import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from audit.models.custom_user import CustomUser
from audit_service import settings


class SafeJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None
        try:
            access_token = authorization_header.split(' ')[1]
            private_key = getattr(settings, 'JWT_SECRET_KEY')
            payload = jwt.decode(
                access_token, private_key, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        except Exception as exe:
            raise exceptions.AuthenticationFailed('Invalid token')

        user_dict = dict(
            name=payload.get('name'),
            session_id=payload.get('session_id')
        )

        user = CustomUser(user_dict)
        user.is_authenticated = True

        return (user, None)