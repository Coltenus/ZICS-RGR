from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from server.models import UserModel

# Register your models here.


# Assigning permissions to a user
# User.objects.create_user(username="student1", password="123456")
# user = User.objects.get(username="student1")
# print(Permission.objects.all())
# user.user_permissions.add(permission)

# Assigning permissions to a group
# group = Group.objects.get(name="developers")
# group.permissions.add(permission)


admin.site.register(UserModel)