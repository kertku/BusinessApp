from django.contrib import admin
from base.models import Company, Ownership, BusinessUser, User

admin.site.register(Company)
admin.site.register(Ownership)
admin.site.register(User)
admin.site.register(BusinessUser)
