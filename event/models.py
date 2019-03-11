from datetime import timezone, datetime

from django.db import models

from polymorphic.models import PolymorphicModel

EMPTY = {'blank': True, 'null': True}
REQUIRED = {'blank': False, 'null': False}
PRIMARY = {'primary_key': True, 'unique': False}


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.CharField(max_length=200, **EMPTY)
    start_date = models.DateTimeField(default=datetime.now, verbose_name='Start Date', **REQUIRED)
    end_date = models.DateTimeField(default=datetime.now, verbose_name='End Date', **REQUIRED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return self.name


class Ticket(models.Model):
    number = models.IntegerField(verbose_name='Number')
    ticket_id = models.CharField(max_length=255, verbose_name='Ticket ID', **PRIMARY)
    qr_code = models.ImageField(upload_to='tickets/qr_code', default='tickets/qr_code/no-qr.png', verbose_name='QR Code')
    image = models.ImageField(upload_to='tickets/png', verbose_name='Ticket Image')
    price = models.FloatField(verbose_name='Price')
    is_paid = models.BooleanField(default=False, verbose_name='Is paid')
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, verbose_name='event', **EMPTY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return self.ticket_id


class ParticipantAbstract(PolymorphicModel):
    SEX = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    first_name = models.CharField(max_length=255, verbose_name='Name')
    last_name = models.CharField(max_length=255, verbose_name='Name')
    email = models.CharField(max_length=200, **REQUIRED)
    description = models.CharField(max_length=200, **EMPTY)
    cin = models.CharField(max_length=200, **EMPTY)
    phone_number = models.CharField(max_length=200, **REQUIRED)
    birth_date = models.DateField(max_length=200, **EMPTY)
    sex = models.CharField(max_length=200, choices=SEX, **EMPTY)
    is_member = models.BooleanField(verbose_name="Is member", default=False, **REQUIRED)
    events = models.ManyToManyField(Event)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return '{} {}'.format(self.first_name, self.last_name)


class ParticipantReservation(ParticipantAbstract):
    approved = models.BooleanField(verbose_name="Approved", default=False, **REQUIRED)

    def __str__(self): super().__str__()


class Participant(ParticipantAbstract):
    ticket = models.OneToOneField(Ticket, verbose_name='Ticket', on_delete=models.SET_NULL, default=None, **EMPTY)

    def __str__(self): super().__str__()