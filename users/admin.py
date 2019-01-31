from .models import User, Department
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    pass

# adminパスにきた時に、ページに表示する
@admin.register(User)
# adminの表示項目の変更等
class AdminUserAdmin(UserAdmin):

    # 入力項目
    # 一行毎に変更可能
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email','departments')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # リスト表示項目
    list_display = ('username', 'email', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name', 'email')
    # フィルターを作成
    filter_horizontal = ('groups', 'user_permissions','departments')