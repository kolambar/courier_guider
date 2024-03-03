from django.contrib import admin

from orders.models import Courier


@admin.register(Courier)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'chat_id', 'status', 'shift_start', 'order_finished')
    list_filter = ('status', )
    search_fields = ('name', )
