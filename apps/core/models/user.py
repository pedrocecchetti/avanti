from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, nickname, password=None):

        user = self.model(email=email, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, date_of_birth, nickname, password=None):

        user = self.create_user(email, first_name, last_name, date_of_birth, nickname, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=64, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=128, verbose_name='Sobrenome')
    date_of_birth = models.DateField(verbose_name='Data de nascimento')

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, verbose_name='Senha')


    nickname = models.CharField(max_length=16, verbose_name='Apelido')

    
    is_active = models.BooleanField(default=False, verbose_name='Usuario Ativo?')
    is_staff = models.BooleanField(default=False, verbose_name='Funcionário?')
    is_superuser =  models.BooleanField(default=False, verbose_name='Admnistrador?')

    last_login = models.DateTimeField(null=True, verbose_name="Ultimo login")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima atualização")
    
    groups = models.ManyToManyField(
        blank=True,
        help_text="Grupo ao qual o usuário pertence. O usuário recebe todas as permissões dos grupos ao qual ele pertence.",
        related_name="user_groups",
        related_query_name="user",
        to="auth.Group",
        verbose_name="Grupos de usuário",
    )

    user_permissions = models.ManyToManyField(
        blank=True,
        help_text="Permissões específicas do usuário.",
        related_name="user_permissions",
        related_query_name="user",
        to="auth.Permission",
        verbose_name="Permissões do usuário",
    )


    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','date_of_birth', 'nickname']

    def get_full_name(self):
        return  f'{self.first_name} {self.last_name}'
        
    def get_short_name(self):
        return self.nickname
    

    def __str__(self):
        return self.get_full_name()

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'