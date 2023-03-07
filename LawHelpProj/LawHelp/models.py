from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class LegalEntity(models.Model):
    full_name = models.CharField(max_length=200, null=True, blank=False)
    short_name = models.CharField(max_length=100, null=True, blank=False)
    ogrn = models.BigIntegerField(null=True, blank=False)
    inn = models.BigIntegerField(null=True, blank=False)
    address = models.TextField(null=True, blank=False)
    
    class Meta:
        abstract = True


class Defendant(LegalEntity):
    defendant_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.defendant_id}/{self.short_name}"


class Plaintiff(LegalEntity):
    plaintiff_id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.plaintiff_id}/{self.short_name}"


class Court(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    address = models.TextField(null=True, blank=False)
    
    def __str__(self):
        return self.name


class Case(models.Model):
    case_id = models.AutoField(primary_key=True)
    court_case_id = models.CharField(max_length=50, null=True, blank=True)
    plaintiff = models.ForeignKey(Plaintiff, on_delete=models.CASCADE)
    defendant = models.ForeignKey(Defendant, on_delete=models.CASCADE)
    case_card = models.URLField(null=True)
    
    def __str__(self):
        return f"{self.case_id} - {self.court_case_id}: {self.plaintiff} - {self.defendant}"