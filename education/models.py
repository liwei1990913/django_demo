from django.db import models
from django.contrib.auth.models import  User

from pygments.lexers import get_all_lexers         # 一个实现代码高亮的模块
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())     # 列出所有配色风格


# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,

    )
    name = models.CharField(max_length=64, verbose_name="姓名")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    #is_admin = models.BooleanField(default=False)
    role = models.ManyToManyField("Role", blank=True, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email


    class Meta:
        permissions = (
            ('education_table_change', 'education_table_change'),
            ('education_list_delete', 'education_list_delete'),
            ('education_list_save', 'education_list_save'),
            ('education_table_save', 'education_table_save'),

        )




# class UserProfile(models.Model):
#     """用户信息表"""
#     user = models.OneToOneField(User)
#     name = models.CharField(max_length=64, verbose_name="姓名")
#     role = models.ManyToManyField("Role",blank=True,null=True)
#
#
#     def __str__(self): #__unicode__
#         return self.name

class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name


class CustomerInfo(models.Model):
    name=models.CharField(max_length=32 ,verbose_name='姓名')
    age=models.SmallIntegerField( verbose_name='年龄')


class Article(models.Model):
    title=models.CharField(max_length=64,verbose_name='标题')
    content=models.TextField(verbose_name='内容')
    user=models.ForeignKey('UserProfile',on_delete=None)
    ctime=models.DateField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment=models.CharField(max_length=128,verbose_name='评论')
    ctime = models.DateField()

    aritcle=models.ForeignKey('Article',on_delete=None)

    reply = models.ForeignKey(verbose_name='回复评论', to='self', related_name='back', null=True,blank=True,on_delete=None)

    user = models.ForeignKey(verbose_name='评论者', to='UserProfile',on_delete=None)


class Area(models.Model):
       name=models.CharField(max_length=64,verbose_name='地区')
       nextname=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)

       def __str__(self):
           return self.name