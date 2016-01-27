from django.contrib import admin

# Register your models here.
from UserAccount.models import *

admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Profession)
admin.site.register(Emp_prfn)
admin.site.register(Employe)
admin.site.register(Task_employe)
admin.site.register(Transaction)
admin.site.register(Master)
