from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, name, surname, password=None):
        """
        Creates and saves a User with the given username, password.
        """
        if not username:
            raise ValueError('Users must have an username !')

        user = self.model(
            username=username,
            name=name,
            surname=surname,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, surname, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            name,
            surname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='Kullanıcı Adı',
        max_length=255,
        unique=True,
    )

    name = models.CharField(verbose_name='name', max_length=30)
    surname = models.CharField(verbose_name='surname', max_length=30)

    # User profile Photos
    profile_photo = models.ImageField(verbose_name='PP', upload_to='pp')

    # User is Teacher ?
    role = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
