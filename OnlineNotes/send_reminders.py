from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from OnlineNotes.models import Note

class Command(BaseCommand):
    help = 'Send email reminders for notes'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        notes = Note.objects.filter(reminder_datetime__lt=now)

        for note in notes:
            subject = 'Reminder: ' + note.title
            message = 'This is a reminder for your note: ' + note.content
            from_email = 'patience@gmail.com'
            recipient_list = 'recipient-email@gmail.com'
            attachment = ['notes.pdf', 'notes.csv']

            send_mail(subject, message, from_email, recipient_list, attachment)