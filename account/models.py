from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, name, password=None):
        if not email:
            raise ValueError('유저는 이메일을 가지고 있어야 합니다')
        if not nickname:
            raise ValueError('유저는 닉네임을 가져야 합니다')
        if not name:
            raise ValueError('유저는 이름을 가져야 합니다')
        user = self.model(
			email = self.normalize_email(email),
			nickname = nickname,
			name = name
		)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, name, password=None):
        user = self.create_user(
	        email,
	        password = password,
	        nickname = nickname,
		    name = name
        )
        user.is_admin = True
        user.save(user=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=-False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.nickname