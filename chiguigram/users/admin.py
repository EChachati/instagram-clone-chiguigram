from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile

"""Trabajando el Dashboard de Administrador"""


# Register your models here.
@admin.register(Profile)  # Equivale a admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = (
        'pk', 'user', 'phone_number', 'website', 'profile_picture'
    )  # Campos a mostrar en la pagina de admin

    # Ver detalle al darle click a un campo
    list_display_links = ('user', 'website')

    # Permite que los campos colocados sean editables dentro de Admin
    list_editable = ('phone_number', 'profile_picture')

    # Elegir los campos validos para el buscador, Si no esta en list_display no sirve
    search_field = ('user__email',
                    'user__first_name',
                    'user__last_name',
                    'phone_number'
                    )

    # Poder filtrar datos
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    # Fields al momento de modificar un user
    fieldsets = (
        (None, {  # Titulo puede ser None
            'fields': (
                ('user', 'profile_picture'),  # Una Fila
            )
        }),
        ('Extra Info', {  # Titulo
            'fields': (
                ('website', 'phone_number'),  # Una Fila
                ('biography')  # Otra Fila
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified')
            )
        })
    )

    # archivos no modificables
    readonly_fields = ('created', 'modified', 'user')


""" 
Une los modelos de User y Profile para no tener que crear un user 
para añadirlo al perfil  
"""


class ProfileInline(admin.StackedInline):
    # Profile in line admin for users
    # Agregar el Admin al Profile
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
    # add profile admin to datebase user admin
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
