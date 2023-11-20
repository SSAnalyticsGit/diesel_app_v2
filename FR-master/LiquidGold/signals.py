from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse
from django.db import transaction
# since we are creating Profile for every new user
from .models import Profile, DieselRequests, Site, Engineer, DieselRequestsLessThan35days
from django.core.mail import send_mail, EmailMessage, BadHeaderError
# created a signal where User act as the sender since we want to automatically create a Profile for every User created


@receiver(post_save, sender=User)  # when a user is saved, send a signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        # everytime a user is created, we create a profile
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)  # when a user is saved, send a signal
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

############################# Ope added stars here ###########################


@receiver(pre_save, sender=DieselRequestsLessThan35days)
def pre_save_toggle_justified(sender, instance, **kwargs):
    if instance.mng_justfication is not None:
        instance.justified = True
        # instance.save()

    else:
        instance.justified = False


@receiver(post_save, sender=DieselRequestsLessThan35days)
def send_email_on_save(sender, instance, **kwargs):
    # Generate the URL dynamically using reverse
    if not instance.email_sent_after_justification and instance.justified:

        url_path = reverse('justified-requests')
        complete_url = 'http://127.0.0.1:8000/' + url_path

        # Email subject and body
        subject = 'Click the link to view task details'
        body = f'Click the following link to view the task details: {complete_url}'

        # Send the email
        send_mail(subject, body, settings.EMAIL_HOST_USER, [
            'afowora@starsightenergy.com'], fail_silently=False)

        instance.email_sent_after_justification = True
        instance.save()


@receiver(pre_save, sender=DieselRequestsLessThan35days)
def pre_save_toggle_has_approved(sender, instance, **kwargs):
    if not instance.email_sent_for_approval and instance.approve:

        instance.has_approved = True
        url_path = reverse('approve-requests')
        complete_url = 'http://127.0.0.1:8000/' + url_path

        # Email subject and body
        subject = 'Click the link to view task details'
        body = f'Click the following link to view the task details: {complete_url}'

        # Send the email
        send_mail(subject, body, settings.EMAIL_HOST_USER, [
            'cukachukwu@starsightenergy.com'], fail_silently=False)
        instance.email_sent_for_approval = True
        instance.save()

    else:
        instance.has_approved = False


@receiver(pre_save, sender=DieselRequestsLessThan35days)
def pre_save_notify_manager(sender, instance, **kwargs):
    if not instance.email_sent_for_rejection and instance.reject:
        # Email subject and body
        subject = 'Request rejected by Boye.'
        body = f'The request was rejected due to unaccepted justification. Please reach out to afowora@starsightenergy.com'

        # subject = 'New Request for Diesel'
        # manager = request.POST.get('manager')
        # for e in User.objects.filter(id=manager):
        #     manager_email = e.email

        # Send the email
        send_mail(subject, body, settings.EMAIL_HOST_USER,
                  #   [manager_email],
                  fail_silently=False)
        instance.email_sent_for_rejection = True
        instance.save()


@receiver(post_save, sender=DieselRequestsLessThan35days)
def create_diesel_request(sender, instance, created, **kwargs):

    if instance.cto_approve:
        # Wrap the whole operation in a transaction
        with transaction.atomic():
            # ensures that the operations are executed within a single database transaction.
            site, _ = Site.objects.get_or_create(
                name=instance.site.name, sudo_name=instance.site.sudo_name)
            engineer, _ = Engineer.objects.get_or_create(
                first_name=instance.engineer.first_name)

            # Create DieselRequests instance
            diesel_request = DieselRequests.objects.create(
                site=site,
                engineer=engineer,
                manager=instance.manager,
                noc_approve=True,
                cto_approve=True,
                noc_status=DieselRequests.STATUS_APPROVED,
                cto_status=DieselRequests.STATUS_APPROVED,
                phcn_comment=instance.phcn_comment,
                quantity_required=instance.quantity_required,
                justification=instance.justification
            )
            print(diesel_request)

            diesel_request.save()


#################################### ends here #############################################
