from django.db import models
from django.db import connections, models
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone
from .manager import RequestManager
from django.contrib.auth.models import User

# Create your models here.


class Engineer(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    change_password = models.TextField()  # This field type is a guess.
    email = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    enabled = models.TextField()  # This field type is a guess.
    first_name = models.CharField(max_length=255, blank=True, null=True)
    is_logged_on = models.TextField()  # This field type is a guess.
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    no_of_wrong_login_count = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    user_name = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    # role = models.ForeignKey('Role', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    zendesk_id = models.CharField(
        unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineer'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Site(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zone = models.CharField(max_length=255, blank=True, null=True)
    # client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    no_of_ac_installed = models.CharField(
        max_length=255, blank=True, null=True)
    nof_panels = models.CharField(max_length=255, blank=True, null=True)
    sudo_name = models.CharField(max_length=255, blank=True, null=True)
    fuel_tank_size = models.CharField(max_length=255, blank=True, null=True)
    generator_size = models.CharField(max_length=255, blank=True, null=True)
    gen_run_hour_date = models.DateTimeField(blank=True, null=True)
    last_ac_maintenance_date = models.DateTimeField(blank=True, null=True)
    last_generator_service_hour = models.BigIntegerField(blank=True, null=True)
    last_panel_maintenance_date = models.DateTimeField(blank=True, null=True)
    last_preventive_maintenance = models.TextField(blank=True, null=True)
    last_preventive_maintenance_date = models.DateTimeField(
        blank=True, null=True)
    last_recorded_run_hour = models.BigIntegerField(blank=True, null=True)
    next_ac_maintenance_date = models.DateTimeField(blank=True, null=True)
    next_panel_maintenance_date = models.DateTimeField(blank=True, null=True)
    # last_ac_maintenance = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)
    # last_panel_maintenance = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)
    site_manager = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    victron_id = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    # last_preventive_maintenance_0 = models.ForeignKey('Task', models.DO_NOTHING, db_column='last_preventive_maintenance_id', blank=True, null=True)  # Field renamed because of name conflict.
    current_fuel_level = models.BigIntegerField(blank=True, null=True)
    fuel_level_date = models.DateTimeField(blank=True, null=True)
    communicating = models.CharField(max_length=255, blank=True, null=True)
    phcn = models.CharField(max_length=255, blank=True, null=True)
    average_daily_fuel_usage = models.CharField(
        max_length=255, blank=True, null=True)
    average_gen_daily_run_hour = models.BigIntegerField(blank=True, null=True)
    hours_to_service = models.BigIntegerField(blank=True, null=True)
    next_service_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site'

    def save(self, *args, **kwargs):
        self.date_created = self.date_created
        self.sudo_name = self.sudo_name
        self.phcn = self.phcn
        self.fuel_level_date = self.fuel_level_date
        self.fuel_tank_size = self.fuel_tank_size

        super(Site, self).save(*args, **kwargs)

    def __str__(self):
        order_by = self.name
        return self.name


class DeiselReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    actual_remaining_litres = models.CharField(
        max_length=255, blank=True, null=True)
    expected_remaining_litres = models.CharField(
        max_length=255, blank=True, null=True)
    gen_run_hour = models.CharField(max_length=255, blank=True, null=True)
    indicative_consumption = models.CharField(
        max_length=255, blank=True, null=True)
    site = models.ForeignKey(Site, models.DO_NOTHING, blank=True, null=True)
    engineer = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    actual_consumption = models.CharField(
        max_length=255, blank=True, null=True)
    reference_top_up_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deisel_report'


class SiteReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    ac_status_report = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    connected = models.CharField(max_length=255, blank=True, null=True)
    current_fuel_level = models.CharField(
        max_length=255, blank=True, null=True)
    engineer = models.TextField(blank=True, null=True)
    generator_age = models.CharField(max_length=255, blank=True, null=True)
    generator_brand = models.CharField(max_length=255, blank=True, null=True)
    generator_size = models.CharField(max_length=255, blank=True, null=True)
    generator_status_report = models.TextField(blank=True, null=True)
    inverter_status = models.CharField(max_length=255, blank=True, null=True)
    last_delivery_date = models.CharField(
        max_length=255, blank=True, null=True)
    last_delivery_quantity = models.CharField(
        max_length=255, blank=True, null=True)
    last_gen_service_hours = models.CharField(
        max_length=255, blank=True, null=True)
    last_panel_cleaning = models.CharField(
        max_length=255, blank=True, null=True)
    last_service_date = models.CharField(max_length=255, blank=True, null=True)
    lighting_status_report = models.CharField(
        max_length=255, blank=True, null=True)
    load_on_critical_inverter_total = models.CharField(
        max_length=255, blank=True, null=True)
    load_onl1 = models.CharField(max_length=255, blank=True, null=True)
    load_onl2 = models.CharField(max_length=255, blank=True, null=True)
    load_onl3 = models.CharField(max_length=255, blank=True, null=True)
    next_delivery_due_date = models.CharField(
        max_length=255, blank=True, null=True)
    next_panel_cleaning = models.CharField(
        max_length=255, blank=True, null=True)
    next_service_date = models.CharField(max_length=255, blank=True, null=True)
    next_service_due = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    number_of_panels = models.CharField(max_length=255, blank=True, null=True)
    pv_harvest_status = models.CharField(max_length=255, blank=True, null=True)
    run_hour = models.CharField(max_length=255, blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    solar_strings = models.CharField(max_length=255, blank=True, null=True)
    status_report = models.CharField(max_length=255, blank=True, null=True)
    torque_level_check_date = models.CharField(
        max_length=255, blank=True, null=True)
    # Field renamed because of name conflict.
    engineer_0 = models.ForeignKey(
        Engineer, models.DO_NOTHING, db_column='engineer_id', blank=True, null=True)
    # Field renamed because of name conflict.
    site_0 = models.ForeignKey(
        Site, models.DO_NOTHING, db_column='site_id', blank=True, null=True)
    time_sheet_end = models.CharField(max_length=255, blank=True, null=True)
    time_sheet_start = models.CharField(max_length=255, blank=True, null=True)
    battery_appearance_ok = models.CharField(
        max_length=255, blank=True, null=True)
    battery_temperature_ok = models.CharField(
        max_length=255, blank=True, null=True)
    battery_terminal_ok = models.CharField(
        max_length=255, blank=True, null=True)
    site_communicating = models.CharField(
        max_length=255, blank=True, null=True)
    date_ac_issue_report = models.CharField(
        max_length=255, blank=True, null=True)
    no_of_fault_ac = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    extra_image1 = models.CharField(max_length=255, blank=True, null=True)
    extra_image2 = models.CharField(max_length=255, blank=True, null=True)
    extra_image3 = models.CharField(max_length=255, blank=True, null=True)
    extra_image4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_report'


class FuelTopUp(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    fuel_level_after_top_up = models.CharField(
        max_length=255, blank=True, null=True)
    fuel_level_before_top_up = models.CharField(
        max_length=255, blank=True, null=True)
    generator_run_hours = models.CharField(
        max_length=255, blank=True, null=True)
    litres = models.CharField(max_length=255, blank=True, null=True)
    percentage_loading = models.CharField(
        max_length=255, blank=True, null=True)
    top_up_date = models.DateTimeField(blank=True, null=True)
    vendors = models.CharField(max_length=255, blank=True, null=True)
    engineer = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(Site, models.DO_NOTHING, blank=True, null=True)
    gen_run_hour_pic_id = models.CharField(
        max_length=255, blank=True, null=True)
    gen_run_hour_pic_url = models.CharField(
        max_length=255, blank=True, null=True)
    job_completion_form1 = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuel_top_up'

    # from django.contrib.auth.models import User


class DieselRequests(models.Model):

    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'

    STATUS_CHOICES = (
        (STATUS_APPROVED, 'approved'),
        (STATUS_REJECTED, 'rejected'),
        (STATUS_PENDING, 'pending'),
        (STATUS_CONFIRMED, 'confirmed'),
    )

    requestdate = models.DateField(auto_now_add=True)
    request_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    mgr_approved_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    cto_approved_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)

    site = models.ForeignKey(Site, models.CASCADE,
                             verbose_name='Confirm Site')
    engineer = models.ForeignKey(
        Engineer, models.CASCADE, verbose_name='Confirm Engineer')
    phcn_comment = models.CharField(max_length=2000, null=True, blank=True)
    quantity_required = models.IntegerField(null=True, blank=True)
    justification = models.CharField(max_length=3000, null=True, blank=True)
    noc_approve = models.BooleanField(blank=True, null=True)
    cto_approve = models.BooleanField(blank=True, null=True)
    noc_comment = models.CharField(max_length=3000, blank=True, null=True)
    cto_comment = models.CharField(max_length=3000, blank=True, null=True)
    noc_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    cto_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = RequestManager()

    class Meta:
        ordering = ['-requestdate']
        verbose_name_plural = 'Diesel Requests'

    @property
    def request_approved(self):
        return self.noc_approve == True

    @property
    def approve_request(self):
        if not self.noc_approve:
            self.noc_approve = True
            self.noc_status = 'confirmed'
            self.save()

    @property
    def pending_request(self):
        if self.noc_approve:
            self.noc_approve = False
            self.noc_status = 'pending'
            self.save()

#########################################################################################################

    @property
    def cto_request_approved(self):
        return self.cto_approve == True  # and self.cto_approve == True

    @property
    def cto_approve_request(self):
        if not self.cto_approve:  # and self.cto_approve:
            self.cto_approve = True
            self.cto_status = 'approved'
            self.save()

    @property
    def cto_pending_request(self):
        if self.cto_approve:
            self.cto_approve = False
            self.cto_status = 'pending'
            self.save()


#########################################################################################################

    @property
    def request_cancel(self):
        if self.noc_approve or not self.noc_approve:
            self.noc_approve = False
            self.noc_status = 'cancelled'
            self.save()

    @property
    def reject_request(self):
        if self.noc_approve or not self.noc_approve:
            self.noc_approve = False
            self.status = 'rejected'
            self.save()

    @property
    def is_rejected(self):
        return self.noc_status == 'rejected'

    def __str__(self):
        return str(str(self.requestdate) + '-' + str(self.site) + '-' + str(self.noc_status))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'


class DieselRequestsLessThan35days(models.Model):

    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'

    STATUS_CHOICES = (
        (STATUS_APPROVED, 'approved'),
        (STATUS_REJECTED, 'rejected'),
        (STATUS_PENDING, 'pending'),
        (STATUS_CONFIRMED, 'confirmed'),
    )

    requestdate = models.DateField(auto_now_add=True)
    request_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    mgr_approved_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    cto_approved_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)

    site = models.ForeignKey(Site, models.CASCADE,
                             verbose_name='Confirm Site')
    engineer = models.ForeignKey(
        Engineer, models.CASCADE, verbose_name='Confirm Engineer')
    phcn_comment = models.CharField(max_length=2000, null=True, blank=True)
    quantity_required = models.IntegerField(null=True, blank=True)
    justification = models.CharField(max_length=3000, null=True, blank=True)
    noc_approve = models.BooleanField(blank=True, null=True)
    cto_approve = models.BooleanField(blank=True, null=True)
    noc_comment = models.CharField(max_length=3000, blank=True, null=True)
    cto_comment = models.CharField(max_length=3000, blank=True, null=True)
    noc_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    cto_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    # ------------------------------------------------------------------------------
    mng_justfication = models.CharField(max_length=2000, blank=True, null=True)
    justified = models.BooleanField(default=False)
    approve = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    has_approved = models.BooleanField(default=False)
    has_rejected = models.BooleanField(default=False)
    rejection_comment = models.CharField(
        max_length=2000, blank=True, null=True)
    no_days = models.CharField(
        max_length=20, blank=True, null=True)
    cto_approve = models.BooleanField(default=False)
    cto_reject = models.BooleanField(default=False)
    email_sent_after_justification = models.BooleanField(default=False)
    email_sent_for_rejection = models.BooleanField(default=False)
    email_sent_for_approval = models.BooleanField(default=False)
    # --------------------------------------------------------------------
    objects = RequestManager()

    class Meta:
        ordering = ['-requestdate']
        # verbose_name_plural = 'Diesel Requests'

    def __str__(self):
        return str(str(self.requestdate) + '-' + str(self.site) + '-' + str(self.noc_status))
