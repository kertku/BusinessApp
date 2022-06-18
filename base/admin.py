from django.contrib import admin

from base.models import Business, Ownership, Owner, BusinessUser, User

admin.site.register(Business)
admin.site.register(Ownership)
admin.site.register(Owner)
admin.site.register(User)
admin.site.register(BusinessUser)
