from django.contrib import admin
from users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('following', )
    readoly_fields = ('username', )
    fildsets = (
        ('Dados pessoais', {
            'fields': ('username', 'email', 'date_joined'),
        }),
        ('Tuiter', {
            'fields': ('fowllowing', ),
            'description': 'Coisas relacionadas ao nosso sistema'
        }),
    )

admin.site.register(User)