from django.db import models


class Equipment(models.Model):
    SOFTWARE_REV_A = 'A'
    SOFTWARE_REV_B = 'B'
    SOFTWARE_REV_C = 'C'
    SOFTWARE_REV_D = 'D'

    MEMBERSHIP_CHOICES = [
        (SOFTWARE_REV_A, 'A'),
        (SOFTWARE_REV_B, 'B'),
        (SOFTWARE_REV_C, 'C'),
        (SOFTWARE_REV_D, 'D'),
    ]

    STATUS_APPROVED = 'Approved'
    STATUS_PENDING = 'Pending'
    STATUS_RETRIED = 'Retried'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (STATUS_APPROVED, 'Approved'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_RETRIED, 'Retried'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    AREA_APPROVAL_COMPANY = 'Company'
    AREA_APPROVAL_LOCATION = 'Location'
    AREA_APPROVAL_SYSTEM = 'System'

    AREA_APPROVAL_CHOICES = [
        (AREA_APPROVAL_COMPANY, 'Company'),
        (AREA_APPROVAL_LOCATION, 'Location'),
        (AREA_APPROVAL_SYSTEM, 'System'),
    ]

    id = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=500)
    model = models.CharField(max_length=255)
    version = models.IntegerField(blank=True, null=True)
    equipment_description = models.TextField()
    special_instructions = models.TextField(blank=True, null=True)
    software_rev = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES,
                                    blank=True, null=True)
    firmware_rev = models.CharField(max_length=255, blank=True, null=True)
    utility_software = models.CharField(max_length=255, blank=True, null=True)
    useful_life = models.IntegerField(blank=True, null=True)
    obsolescence_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              blank=True, null=True)
    date_approved = models.DateField(blank=True, null=True)
    area_approval = models.CharField(
        max_length=10, choices=AREA_APPROVAL_CHOICES, blank=True, null=True)
    approved_by = models.CharField(max_length=255, blank=True, null=True)
    documents_name = models.CharField(max_length=500, blank=True, null=True)
    documents_link = models.URLField(blank=True, null=True)


class EquipmentForm(models.Model):
    id = models.OneToOneField(Equipment, primary_key=True,
                              on_delete=models.CASCADE)
    application_restriction = models.TextField(blank=True, null=True)
    hazardous_area_classification_met = models.BooleanField(blank=True, null=True)
    other_approvals = models.TextField(blank=True, null=True)
    manufactural_quality_good = models.BooleanField(blank=True, null=True)
    installation_match_manufacturer_recommendations = models.BooleanField(
        blank=True, null=True)
    installation_match_manufacturer_recommendations_if_no = models.TextField(
        blank=True, null=True)
    maintainance_plan_agree_with_manufacturer_recommendations = models.BooleanField(
        blank=True, null=True)
    maintainance_plan_agree_with_manufacturer_recommendations_if_no = models.BooleanField(
        blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    approval_based_on = models.TextField(blank=True, null=True)
    prior_use_application = models.CharField(max_length=255, blank=True, null=True)
    as_of_date = models.DateField(blank=True, null=True)
    obsolescence_status = models.CharField(max_length=255, blank=True, null=True)
    obsolescence_date = models.DateField(blank=True, null=True)
    useful_life = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=255, blank=True, null=True)
    reviewed_date = models.DateField(blank=True, null=True)
    close_record = models.BooleanField(blank=True, null=True)
