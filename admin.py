from mystat_app import Users
from django.contrib import admin

class UsersAdmin(admin.ModelAdmin):
	fieldsets = [
		('Username',	{'fields': ['username']}),
		('Email', 	{'fields': ['email']}),
		('Registered',	{'fields': ['registered']}),
	]

admin.site.register(Users, UsersAdmin)