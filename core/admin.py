from django.contrib import admin

# Register your models here.
from core.models import Member, Activity
from event.models import Ticket


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cin',
        'email',
        'phone_number',
        'birth_date',
        'description',
        'sex',


    )
    search_fields = ('name', 'cin', 'email')


@admin.register(Activity)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',


    )
    search_fields = ('name',)
