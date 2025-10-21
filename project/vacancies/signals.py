from django.dispatch import Signal, receiver
from django.db.models.signals import post_save

from .models import Vacancy

custom_signal = Signal()

@receiver(custom_signal)
def print_custom_signal(sender, text, **kwargs):
    # some custom logic
    pass


@receiver(post_save)
def print_pre_save_event_data(sender, instance, **kwargs):
    if sender == Vacancy:
        # send email to all workers that new vacancy is available
        pass
