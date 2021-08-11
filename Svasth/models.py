from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django.db import models


class User(models.Model):
    User_Id = models.AutoField(primary_key=True)
    User_Name = models.CharField(max_length=100)
    User_Email = models.EmailField(max_length=254)
    User_Password = models.CharField(max_length=255)
    User_BirthDate = models.DateField(blank=True, null=True)
    User_BloodGroup = models.CharField(max_length=4, blank=True, null=True)
    User_Icon = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.User_Name


class Hospital(models.Model):
    Hospital_Id = models.AutoField(primary_key=True)
    Hospital_Name = models.CharField(max_length=254)
    Hospital_Location = models.TextField(max_length=1000)
    Hospital_Contact = models.CharField(max_length=15)
    Hospital_Logo = models.FileField()

    def __str__(self):
        return self.Hospital_Name


class Specialisation(models.Model):
    Specialisation_Id = models.AutoField(primary_key=True)
    Specialisation_Name = models.CharField(max_length=1000)
    Specialisation_Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.Specialisation_Name + "-" + self.Specialisation_Hospital.Hospital_Name


class Doctor(models.Model):
    Doctors_Id = models.AutoField(primary_key=True)
    Doctors_Name = models.CharField(max_length=254)
    Specialisation_Choices = (
        (" Allergist", " Allergist"),
        (" Anesthesiologist", " Anesthesiologist"),
        (" Cardiologist", "Cardiologist "),
        (" Orthopaedic", " Orthopaedic"),
        (" Endocrinologist", " Endocrinologist"),
        (" Dermatologist", " Dermatologist")
    )
    Doctors_Specialisation = models.ForeignKey(Specialisation, on_delete=models.CASCADE)
    Doctors_Icon = models.FileField()
    Doctors_Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.Doctors_Name + " (" + self.Doctors_Specialisation.Specialisation_Name + " )" + "-" + self.Doctors_Hospital.Hospital_Name


class Event(models.Model):
    Event_Id = models.AutoField(primary_key=True)
    Event_Name = models.CharField(max_length=1000)
    Event_Desc = models.TextField(max_length=1000)
    Event_link = models.CharField(max_length=1000)
    Event_img = models.FileField()
    Event_Date = models.DateField(default=now)

    def __str__(self):
        return self.Event_Name


class Report(models.Model):
    Report_Id = models.AutoField(primary_key=True)
    Reports_Choices = (
        (" CT Scan ", " CT Scan "),
        (" Blood Report ", " Blood Report "),
        (" ECG ", " ECG "),
        (" Urine Report ", " Urine Report "),
        (" X-Ray Report ", " X-Ray Report "),
        (" UltraSound Report ", " UltraSound Report ")
    )
    Report_Name = models.CharField(max_length=200, choices=Reports_Choices)
    Report_Desc = models.CharField(max_length=500, default='', blank=True)
    Report_Doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Report_Date = models.DateField(default=now)
    Report_file = models.FileField()
    Report_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Report_User.User_Name + "-" + self.Report_Name


class LoginTime(models.Model):
    LoginTime_Id = models.AutoField(primary_key=True)
    LoginTime_User = models.ForeignKey(User, on_delete=models.CASCADE)
    LoginTime_DateTime = models.DateTimeField()

    def __str__(self):
        return self.LoginTime_User.User_Name


class Appointment(models.Model):
    Appointment_Id = models.AutoField(primary_key=True)
    Appointment_Date = models.DateField()
    Appointment_Time = models.TimeField()
    Appointment_Doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Appointment_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Appointment_User.User_Name


class Relationship(models.Model):
    Relationships_Id = models.AutoField(primary_key=True)
    Relationships_Date = models.DateField()
    Relationships_Doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Relationships_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Relationships_Doc.Doctors_Name + '-' + self.Relationships_User.User_Name


class Contact(models.Model):
    Contact_ID = models.AutoField(primary_key=True)
    Contact_DateTime = models.DateTimeField()
    Contact_Name = models.CharField(max_length=255)
    Contact_Email = models.EmailField()
    Contact_Message = models.TextField(max_length=1000)
    Contact_User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Contact_Name + "-" + self.Contact_Email
