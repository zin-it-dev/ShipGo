from django.contrib.auth.models import BaseUserManager

from .enums import Role

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not username or len(username) <= 0 : 
            raise ValueError("Users must have an username")
        
        if not email or len(email) <= 0 : 
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.role = Role.ADMIN
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user