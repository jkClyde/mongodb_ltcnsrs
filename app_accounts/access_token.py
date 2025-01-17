from rest_framework_simplejwt.tokens import AccessToken

class CustomAccessToken(AccessToken):
    def custom_claims(self, user):
        return {
            'is_admin': user.is_admin,
            # Add any other custom claims you want to include
        }