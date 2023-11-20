# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlarmTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    cleared = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    id_alarm = models.CharField(max_length=255, blank=True, null=True)
    id_site = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    started = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarm_tags'


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    zendesk_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Code(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    extra_info = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code'
        unique_together = (('code', 'type'),)


class DailyTimeSheet(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    asset_id = models.CharField(max_length=255, blank=True, null=True)
    brief_description_of_work = models.CharField(
        max_length=255, blank=True, null=True)
    cost_code = models.CharField(max_length=255, blank=True, null=True)
    hours = models.CharField(max_length=255, blank=True, null=True)
    log_time = models.DateTimeField(blank=True, null=True)
    site_code = models.CharField(max_length=255, blank=True, null=True)
    transport_cost = models.CharField(max_length=255, blank=True, null=True)
    engineer_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_time_sheet'


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
    site = models.ForeignKey('Site', models.DO_NOTHING, blank=True, null=True)
    engineer = models.ForeignKey(
        'Engineer', models.DO_NOTHING, blank=True, null=True)
    actual_consumption = models.CharField(
        max_length=255, blank=True, null=True)
    reference_top_up_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deisel_report'


class DgUploadToZendesk(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dg_upload_to_zendesk'


class Engineer(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
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
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey('Role', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    zendesk_id = models.CharField(
        unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineer'


class Fields(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    field_label = models.CharField(max_length=255, blank=True, null=True)
    field_name = models.CharField(max_length=255, blank=True, null=True)
    field_type = models.CharField(max_length=255, blank=True, null=True)
    required = models.CharField(max_length=255, blank=True, null=True)
    type_data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fields'


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
    site = models.ForeignKey('Site', models.DO_NOTHING, blank=True, null=True)
    gen_run_hour_pic_id = models.CharField(
        max_length=255, blank=True, null=True)
    gen_run_hour_pic_url = models.CharField(
        max_length=255, blank=True, null=True)
    job_completion_form1 = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuel_top_up'


class GeneratorConsumption(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    # Field renamed because it started with '_'.
    field_100loading = models.FloatField(
        db_column='_100loading', blank=True, null=True)
    # Field renamed because it started with '_'.
    field_25loading = models.FloatField(
        db_column='_25loading', blank=True, null=True)
    # Field renamed because it started with '_'.
    field_50loading = models.FloatField(
        db_column='_50loading', blank=True, null=True)
    # Field renamed because it started with '_'.
    field_75loading = models.FloatField(
        db_column='_75loading', blank=True, null=True)
    gen_size = models.CharField(
        unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generator_consumption'


class Gentracker(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    client = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    last_gen_service_date = models.CharField(
        max_length=255, blank=True, null=True)
    last_recorded_run_hour = models.BigIntegerField(blank=True, null=True)
    last_service_run_hour = models.BigIntegerField(blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    next_service_hour = models.BigIntegerField(blank=True, null=True)
    run_hour_date = models.CharField(max_length=255, blank=True, null=True)
    service_hour_difference = models.BigIntegerField(blank=True, null=True)
    site = models.ForeignKey('Site', models.DO_NOTHING, blank=True, null=True)
    site_manager = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    next_service_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gentracker'


class Mail(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    last_sent = models.DateTimeField(blank=True, null=True)
    mail_content = models.TextField(blank=True, null=True)
    mail_header = models.CharField(max_length=255, blank=True, null=True)
    mail_to = models.CharField(max_length=255)
    sent = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mail'


class MailAttachements(models.Model):
    mail = models.OneToOneField(Mail, models.DO_NOTHING, primary_key=True)
    attachements = models.CharField(max_length=255, blank=True, null=True)
    attachements_key = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mail_attachements'
        unique_together = (('mail', 'attachements_key'),)


class MailCopy(models.Model):
    mail = models.ForeignKey(Mail, models.DO_NOTHING)
    copy = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_copy'


class Permission(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    permission_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission'


class PmserviceReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    ac_service_date = models.CharField(max_length=255, blank=True, null=True)
    generator_service_date = models.CharField(
        max_length=255, blank=True, null=True)
    generator_service_run_hour = models.CharField(
        max_length=255, blank=True, null=True)
    panel_service_date = models.CharField(
        max_length=255, blank=True, null=True)
    engineer = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey('Site', models.DO_NOTHING, blank=True, null=True)
    extra_image = models.CharField(max_length=255, blank=True, null=True)
    job_completion_form1 = models.CharField(
        max_length=255, blank=True, null=True)
    job_completion_form2 = models.CharField(
        max_length=255, blank=True, null=True)
    ppm_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmservice_report'


class ReportConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_config'


class ReportConfigFields(models.Model):
    report_config = models.ForeignKey(ReportConfig, models.DO_NOTHING)
    fields = models.OneToOneField(Fields, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_config_fields'


class ReportDataAttributes(models.Model):
    report_config = models.ForeignKey(ReportConfig, models.DO_NOTHING)
    data_attributes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_data_attributes'


class Reports(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    engineer = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    report_config = models.ForeignKey(
        ReportConfig, models.DO_NOTHING, blank=True, null=True)
    site_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reports'


class ReportsSubmittedData(models.Model):
    reports = models.OneToOneField(
        Reports, models.DO_NOTHING, primary_key=True)
    submitted_data = models.CharField(max_length=255, blank=True, null=True)
    submitted_data_key = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'reports_submitted_data'
        unique_together = (('reports', 'submitted_data_key'),)


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    role_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class RoleApprovables(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING)
    approvables = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_approvables'


class RolePermission(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_permission'


class Setting(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setting'


class Site(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zone = models.CharField(max_length=255, blank=True, null=True)
    client = models.ForeignKey(
        Client, models.DO_NOTHING, blank=True, null=True)
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
    last_ac_maintenance = models.ForeignKey(
        'Task', models.DO_NOTHING, blank=True, null=True)
    last_panel_maintenance = models.ForeignKey(
        'Task', models.DO_NOTHING, blank=True, null=True)
    site_manager = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    victron_id = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    # Field renamed because of name conflict.
    last_preventive_maintenance_0 = models.ForeignKey(
        'Task', models.DO_NOTHING, db_column='last_preventive_maintenance_id', blank=True, null=True)
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


class SpringSession(models.Model):
    # Field name made lowercase.
    primary_id = models.CharField(
        db_column='PRIMARY_ID', primary_key=True, max_length=36)
    # Field name made lowercase.
    session_id = models.CharField(
        db_column='SESSION_ID', unique=True, max_length=36)
    # Field name made lowercase.
    creation_time = models.BigIntegerField(db_column='CREATION_TIME')
    # Field name made lowercase.
    last_access_time = models.BigIntegerField(db_column='LAST_ACCESS_TIME')
    # Field name made lowercase.
    max_inactive_interval = models.IntegerField(
        db_column='MAX_INACTIVE_INTERVAL')
    # Field name made lowercase.
    expiry_time = models.BigIntegerField(db_column='EXPIRY_TIME')
    # Field name made lowercase.
    principal_name = models.CharField(
        db_column='PRINCIPAL_NAME', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spring_session'


class SpringSessionAttributes(models.Model):
    # Field name made lowercase.
    session_primary = models.OneToOneField(
        SpringSession, models.DO_NOTHING, db_column='SESSION_PRIMARY_ID', primary_key=True)
    # Field name made lowercase.
    attribute_name = models.CharField(
        db_column='ATTRIBUTE_NAME', max_length=200)
    # Field name made lowercase.
    attribute_bytes = models.TextField(db_column='ATTRIBUTE_BYTES')

    class Meta:
        managed = False
        db_table = 'spring_session_attributes'
        unique_together = (('session_primary', 'attribute_name'),)


class SystemUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
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
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_user'


class Task(models.Model):
    type = models.CharField(max_length=31)
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    jcf1 = models.CharField(max_length=255, blank=True, null=True)
    jcf2 = models.CharField(max_length=255, blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    # This field type is a guess.
    change_oil_filter = models.TextField(blank=True, null=True)
    fuel_level_after_maintenance = models.CharField(
        max_length=255, blank=True, null=True)
    generator_run_hour_after_maintenance = models.BigIntegerField(
        blank=True, null=True)
    run_hour_scheduled_at = models.BigIntegerField(blank=True, null=True)
    completed_by = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(Site, models.DO_NOTHING, blank=True, null=True)
    site_manager = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class ZendeskIssue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignee_id = models.BigIntegerField(blank=True, null=True)
    brand_id = models.BigIntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_at = models.DateTimeField(blank=True, null=True)
    engineer_feedback = models.TextField(blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    forum_topic_id = models.BigIntegerField(blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    has_incidents = models.TextField()  # This field type is a guess.
    # This field type is a guess.
    is_public = models.TextField(blank=True, null=True)
    issue_log_id = models.CharField(max_length=255, blank=True, null=True)
    noc_responsible = models.CharField(max_length=255, blank=True, null=True)
    on_hold_with = models.CharField(max_length=255, blank=True, null=True)
    organization_id = models.BigIntegerField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    problem_id = models.BigIntegerField(blank=True, null=True)
    recipient = models.CharField(max_length=255, blank=True, null=True)
    requested_by_email = models.CharField(
        max_length=255, blank=True, null=True)
    requested_by_name = models.CharField(max_length=255, blank=True, null=True)
    requester_id = models.BigIntegerField(blank=True, null=True)
    responsible = models.CharField(max_length=255, blank=True, null=True)
    root_cause = models.CharField(max_length=255, blank=True, null=True)
    satisfaction_rating = models.CharField(
        max_length=255, blank=True, null=True)
    site_code = models.CharField(max_length=255, blank=True, null=True)
    site_manager = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    solved_date = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    submitter_id = models.BigIntegerField(blank=True, null=True)
    ticket_form_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zendesk_issue'
