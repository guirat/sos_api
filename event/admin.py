from django.contrib import admin

# Register your models here.
from event.models import Participant, Event, Ticket


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cin',
        'email',
        'phone_number',
        'birth_date',
        'description',
        'sex',


    )
    search_fields = ('name', 'email')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)


@admin.register(Ticket)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'ticket_id',
        'qr_code',
        'price',
        'is_paid',

    )
    search_fields = ('ticket_id',)