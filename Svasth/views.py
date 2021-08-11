from .models import User, Doctor, Hospital, Report, LoginTime, Event, Appointment, Specialisation, Relationship, Contact
from django.shortcuts import render, redirect
import datetime
from django.contrib import messages
from passlib.apps import custom_app_context as pwd_context

today = datetime.date.today()
now = datetime.datetime.now()


def Check(x):
    return bool(x == True)


def index(resquest):
    All_Doctors = Doctor.objects.all()
    All_Event = Event.objects.all()
    context = {'All_Doctors': All_Doctors, 'All_Event': All_Event}
    return render(resquest, 'Svasth/Index.html', context)


def home(resquest, UserID):
    ActiveUser = User.objects.get(User_Id=UserID)
    All_Event = Event.objects.all()
    context = {'All_Event': All_Event, 'ActiveUser': ActiveUser, 'UserID': UserID}
    return render(resquest, 'Svasth/Home.html', context)


def MyDocters(resquest, UserID):
    global flag2
    flag2 = True
    if resquest.method == 'POST':
        date = resquest.POST['appointment_date']
        time = resquest.POST['appointment_time']
        doc = resquest.POST['Doc']
        if Appointment.objects.filter(Appointment_Date=date, Appointment_Time=time,
                                      Appointment_User__User_Id=UserID).exists():
            flag2 = False
            messages.error(resquest,"Appointment Couldn't Be Book.")
            return redirect('Svasth:MyDoctors',UserID=UserID)
        if Check(flag2):
            main = Appointment.objects.create(Appointment_Date=date, Appointment_Time=time, Appointment_User_id=UserID,
                                              Appointment_Doc_id=doc)
            main.save()
        return redirect("Svasth:Home")
    All_Relationships = Relationship.objects.filter(Relationships_User__User_Id=UserID)
    Docs = Doctor.objects.all()
    Specs = Specialisation.objects.all()
    All_Doctors = Doctor.objects.all()
    context = {'All_Doctors': All_Doctors, 'Docs': Docs, 'Specs': Specs, 'All_Relationships': All_Relationships,
               'UserID': UserID}
    return render(resquest, 'Svasth/MyDoctors.html', context)


def LogIn(resquest):
    if resquest.method == "POST":
        User_Mail = resquest.POST['email']
        User_Password = resquest.POST['password']

        if User.objects.filter(User_Email=User_Mail).exists():
            UserEmail = User.objects.get(User_Email=User_Mail)
            if pwd_context.verify(User_Password, UserEmail.User_Password):
                log = LoginTime.objects.create(LoginTime_User=UserEmail, LoginTime_DateTime=now)
                log.save()
                UserID = UserEmail.User_Id
                return redirect("Svasth:Home", UserID=UserID)
            else:
                messages.error(resquest, 'Invalid Password')
                return redirect("Svasth:LogIn")

        else:
            messages.error(resquest, 'Invalid Username')
            return redirect("Svasth:LogIn")

    return render(resquest, 'Svasth/LoginPage.html')


def Reports(resquest, UserID):
    All_Reports = Report.objects.filter(Report_User__User_Id=UserID)
    context = {'All_Reports': All_Reports, 'UserID': UserID}
    return render(resquest, 'Svasth/Reports.html', context)


def SignIn(resquest):
    if resquest.method == 'POST':
        Name = resquest.POST['name']
        Email = resquest.POST['email']
        Password = resquest.POST['password']
        PasswordHash = pwd_context.hash(Password)
        Null = None
        if User.objects.filter(User_Email=Email).exists():
            messages.error(resquest, 'Following Email Exist')
            return redirect("Svasth:SignIn")
        else:
            Main = User.objects.create(User_Name=Name, User_Email=Email, User_Password=PasswordHash)
            Main.save()
            UserIDsign = User.objects.get(User_Email=Email)
            return redirect("Svasth:Home", UserID=UserIDsign.User_Id)

    return render(resquest, 'Svasth/SignInPage.html')


def Appointments(resquest, UserID):
    global flag1
    flag1 = True

    if resquest.method == 'POST':
        date = resquest.POST['appointment_date']
        time = resquest.POST['appointment_time']
        doc = resquest.POST['Doc']
        if Appointment.objects.filter(Appointment_Date=date, Appointment_Time=time,
                                      Appointment_User__User_Id=UserID).exists():
            flag1 = False
            messages.error(resquest, "Appointment Couldn't Be Book")
            return redirect("Svasth:Appointments",UserID=UserID)
        if Check(flag1):
            main = Appointment.objects.create(Appointment_Date=date, Appointment_Time=time, Appointment_User_id=UserID,
                                              Appointment_Doc_id=doc)
            main.save()
        # Appointment.objects.filter(Appointment_Id=delete).delete()
        return redirect("Svasth:Appointments",UserID=UserID)

    Apps = Appointment.objects.filter(Appointment_User__User_Id=UserID)
    Docs = Doctor.objects.all()
    Specs = Specialisation.objects.all()
    context = {'Apps': Apps, 'today': today, 'Docs': Docs, 'Specs': Specs, 'UserID': UserID}
    return render(resquest, 'Svasth/Appointments.html', context)


def Hospitals(resquest, UserID):
    Hosps = Hospital.objects.all()
    context = {'Hosps': Hosps, 'UserID': UserID}
    return render(resquest, 'Svasth/Hospital.html', context)


def Special(resquest, HopId, UserID):
    Specs = Specialisation.objects.filter(Specialisation_Hospital__Hospital_Id=HopId)
    context = {'Specs': Specs, 'HopId': HopId, 'UserID': UserID}
    return render(resquest, 'Svasth/Specialisations.html', context)


def DoctersSpecial(resquest, SpecId, UserID):
    global flag
    flag = True
    if resquest.method == 'POST':
        date = resquest.POST['appointment_date']
        time = resquest.POST['appointment_time']
        doc = resquest.POST['Doc']

        if Appointment.objects.filter(Appointment_Date=date,Appointment_Time=time,Appointment_User__User_Id=UserID).exists():
            flag = True
            messages.error(resquest, "Appointment Couldn't Be Book")
            return redirect('Svasth:DoctoresSpecial',SpecId=SpecId,UserID=UserID)
        if Check(flag):
            main = Appointment.objects.create(Appointment_Date=date, Appointment_Time=time, Appointment_User_id=UserID,
                                              Appointment_Doc_id=doc)
            main.save()
        return redirect("Svasth:Home", UserID=UserID)
    Docs = Doctor.objects.filter(Doctors_Specialisation_id=SpecId)
    Specs = Specialisation.objects.all()
    All_Doctors = Doctor.objects.all()
    context = {'All_Doctors': All_Doctors, 'Docs': Docs, 'Specs': Specs, 'UserID': UserID}
    return render(resquest, 'Svasth/DoctorsSpecial.html', context)


def Contacts(resquest):
    if resquest.method == 'POST':
        fname = resquest.POST['fname']
        lname = resquest.POST['lname']
        email = resquest.POST['email']
        message = resquest.POST['message']

        name = fname + ' ' + lname
        if User.objects.filter(User_Email=email).exists():
            UserMade = User.objects.get(User_Email=email)
            con = Contact.objects.create(Contact_DateTime=now, Contact_Email=email, Contact_Message=message,
                                         Contact_Name=name, Contact_User_id=UserMade.User_Id)
            con.save()
        else:
            con = Contact.objects.create(Contact_DateTime=now, Contact_Email=email, Contact_Message=message,
                                         Contact_Name=name)
            con.save()

    return render(resquest, 'Svasth/contact.html')
