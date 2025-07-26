from rest_framework_simplejwt.views import TokenObtainPairView as JwtTokenObtainPairView, TokenRefreshView as JwtTokenRefreshView
from rest_framework_simplejwt import exceptions as jwt_exp
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime


class TokenObtainPairView(JwtTokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except jwt_exp.TokenError as e:
            raise jwt_exp.InvalidToken(e.args[0])
        
        res = Response(serializer.validated_data, status=status.HTTP_200_OK)
        
        try:
            res.delete_cookie("access_token")
        except Exception as e:
            print(e)
        
        res.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=serializer.validated_data["access"],
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
            path=settings.SIMPLE_JWT.get("AUTH_COOKIE_PATH", "/"),
            expires=datetime.utcnow() + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        res.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
            value=serializer.validated_data["refresh"],
            domain=settings.SIMPLE_JWT.get("AUTH_COOKIE_DOMAIN"),
            path=settings.SIMPLE_JWT.get("AUTH_COOKIE_PATH", "/"),
            expires=datetime.utcnow() + settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        return res
	

def refresh_get(request):
    try:
        RT = request.COOKIES["refresh_token"]
        return JsonResponse({"refresh": RT}, safe=False)
    except Exception as e:
        print(e)
        return None


class TokenRefreshView(JwtTokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except jwt_exp.TokenError as e:
            raise jwt_exp.InvalidToken(e.args[0])

        res = Response(serializer.validated_data, status=status.HTTP_200_OK)
        res.delete_cookie("access_token")
        res.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=serializer.validated_data["access"],
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
            path=settings.SIMPLE_JWT.get("AUTH_COOKIE_PATH", "/"),
            expires=datetime.utcnow() + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        return res