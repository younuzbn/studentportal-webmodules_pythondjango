import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import redirect

from myapp.models import *


# Create your views here.


def login(request):
    l=Login()
    l.username="admin"
    l.password='123'
    l.type='admin'
    l.save()

    return render(request,"index_login.html")

def login_post(request):
    username = request.POST["username"]
    password = request.POST["password"]

    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        var1 = Login.objects.get(username=username, password=password)
        request.session['lid']=var1.id
        if var1.type=='admin':
            return HttpResponse('''<script>alert('login success');window.location='/myapp/home/'</script>"''')
        if var1.type=='club':
            return HttpResponse('''<script>alert('login success');window.location='/myapp/home_club/'</script>"''')
        if var1.type=='collegeofficestaff':
            return HttpResponse('''<script>alert('login success');window.location='/myapp/home_collegeofficestaff/'</script>"''')
        if var1.type=='teacher':
            return HttpResponse('''<script>alert('login success');window.location='/myapp/home_teachers/'</script>"''')
        else:
            return HttpResponse('''<script>alert('invalid username or password');window.location='/myapp/login/'</script>"''')
    else:
        return HttpResponse('''<script>alert('invalid username or password');window.location='/myapp/login/'</script>"''')



# def logout_post(request):
#     request.session['lid']=""
#     return redirect('/myapp/login/')
#
# def home(request):
#     if request.session['lid']=="":
#         return HttpResponse(
#             '''<script>alert('Please Login..');window.location='/myapp/login/'</script>"''')
#     return render(request,"Admin/admin_home.html")

def logout(request):
    # Clear session data upon logout
    request.session.clear()
    # Redirect the user to the login page or any other page after logout
    return redirect('/myapp/login/')

def home(request):
    if not request.session.get('lid'):
        return redirect('/myapp/login/')
    return render(request, "Admin/admin_home.html")




def add_course(request):
    if request.session['lid']=="":
        return HttpResponse(
            '''<script>alert('Please Login..');window.location='/myapp/login/'</script>"''')
    res=Department.objects.all()
    return render(request,"Admin/add course.html",{'data': res})

def add_course_post(request):
    course = request.POST["course"]
    dept=request.POST["select"]
    semester = request.POST["semester"]
    obj = Course()
    obj.Course_name = course
    obj.Semester = semester
    obj.DEPARTMENT_id=dept
    obj.save()
    return HttpResponse('''<script>alert("course added succesfully");window.location='/myapp/add_course/'</script>''')
res=Department.objects.all()
def add_department(request):
    return render(request,"Admin/add department.html")

def add_department_post(request):
    department_name = request.POST["department_name"]
    obj = Department()
    obj.department_name = department_name
    obj.save()
    return HttpResponse('''<script>alert("department added succesfully");window.location='/myapp/add_department/'</script>''')

def add_office_staff(request):
    return render(request,"Admin/add office staff.html")

def add_office_staff_post(request):
    office_staff_name = request.POST["office_staff_name"]
    office_staff_phone_number = request.POST["office_staff_phone_number"]
    email_id = request.POST["email_id"]
    office_staff_photo = request.FILES["office_staff_photo"]

    from datetime import datetime
    date = 'office_staff/'+datetime.now().strftime('%Y%m%d-%H%m%d') + office_staff_photo.name
    fs = FileSystemStorage()
    fs.save(date, office_staff_photo)
    path = fs.url(date)


    l = Login()
    l.username = email_id
    l.password = office_staff_phone_number
    l.type = 'collegeofficestaff'
    l.save()

    obj = Office_staff()
    obj.LOGIN = l
    obj.office_staff_name = office_staff_name
    obj.office_staff_phone_number = office_staff_phone_number
    obj.email_id = email_id
    obj.office_staff_photo = path
    obj.save()
    return HttpResponse('''<script>alert("office staff added succesfully");window.location='/myapp/add_office_staff/'</script>''')
def add_student(request):
    res = Course.objects.all()
    return render(request,"Admin/add student.html",{'data': res})

def add_student_post(request):
    student_name = request.POST["student_name"]
    house_name = request.POST["house_name"]
    street_name = request.POST["street_name"]
    pin = request.POST["pin"]
    email_id = request.POST["email"]
    phone_number = request.POST["phone_number"]
    post = request.POST["post"]
    register_number = request.POST["register_number"]
    course = request.POST["course"]
    admission_year = request.POST["admission_year"]
    date_of_birth = request.POST["date_of_birth"]
    gender = request.POST["gender"]
    photo = request.FILES["photo"]

    from datetime import datetime
    date  = 'student/'+datetime.now().strftime('%Y%m%d-%H%m%d')+photo.name
    fs = FileSystemStorage()
    fs.save(date,photo)
    path = fs.url(date)

    lobj = Login()
    lobj.username = register_number
    lobj.password = phone_number
    lobj.type = 'student'
    lobj.save()

    obj = Student()
    obj.name = student_name
    obj.house_name = house_name
    obj.street = street_name
    obj.pin = pin
    obj.email_id = email_id
    obj.phone_number = phone_number
    obj.post = post
    obj.register_number = register_number
    obj.COURSE_id = course
    obj.admission_year = admission_year
    obj.date_of_birth = date_of_birth
    obj.gender = gender
    obj.photo = path
    obj.LOGIN = lobj
    obj.save()
    return HttpResponse('''<script>alert("student added succesfully");window.location='/myapp/add_student/'</script>''')

def add_subject(request):
    res=Course.objects.all()
    return render(request,"Admin/add subject.html", {'data':res})

def add_subject_post(request):
    subject = request.POST["subject"]
    cid = request.POST["select"]
    sem = request.POST["semester"]
    obj = Subject()
    obj.subject = subject
    obj.COURSE_id=cid
    obj.sem=sem
    obj.save()
    return HttpResponse('''<script>alert("subject added succesfully");window.location='/myapp/add_subject/'</script>''')
def add_teacher(request):
    res = Department.objects.all()
    return render(request,"Admin/add teacher.html",{'data':res})

def add_teacher_post(request):
    teacher_name = request.POST["teacher_name"]
    department = request.POST["department"]
    teacher_email_id = request.POST["teacher_email_id"]
    teacher_phone_no = request.POST["teacher_phone_no"]
    teacher_photo = request.FILES["teacher_photo"]

    from datetime import datetime
    date = 'teacher/'+datetime.now().strftime('%Y%m%d-%H%m%d') + teacher_photo.name
    fs = FileSystemStorage()
    fs.save(date, teacher_photo)
    path = fs.url(date)

    lobj = Login()
    lobj.username = teacher_email_id
    lobj.password = teacher_phone_no
    lobj.type = 'teacher'
    lobj.save()

    obj = Teachers()
    obj.name = teacher_name
    obj.DEPARTMENT_id=department
    obj.email_id = teacher_email_id
    obj.phone_number = teacher_phone_no
    obj.photo = path
    obj.LOGIN = lobj
    obj.save()
    return HttpResponse('''<script>alert("teacher added successfully");window.location='/myapp/add_teacher/'</script>''')
def change_password_admin(request):
    return render(request,"Admin/change password.html")

def change_password_admin_post(request):
    current_password = request.POST["current_password"]
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]
    log = Login.objects.filter(password=current_password)
    if log.exists():
        log1 = Login.objects.get(password=current_password,id = request.session['lid'])
        if new_password == confirm_password:
            log1 = Login.objects.filter(password=current_password,id = request.session['lid']).update(password=new_password)
            return HttpResponse('''<script>alert('password changed');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_admin/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_admin/'</script>''')


def edit_department(request,id):
    res = Department.objects.get(id=id)
    return render(request,"Admin/edit department.html",{'data':res})

def edit_department_post(request):
    department_name = request.POST["department_name"]
    id = request.POST["id"]
    res = Department.objects.get(id=id)
    res.department_name = department_name
    res.save()
    return HttpResponse('''<script>alert("edited department successfully");window.location='/myapp/view_department/'</script>''')

def send_complaint_reply_admin(request,id):
    return render(request,"Admin/send complaint reply.html",{'id':id})

def send_complaint_reply_admin_post(request):
    reply = request.POST["reply"]
    id = request.POST["id"]
    res = Complaint.objects.filter(id=id).update(reply=reply,status='replied')
    return HttpResponse('''<script>alert("replied successfully");window.location='/myapp/view_complaint_admin/'</script>''')

def send_notification_admin(request):
    return render(request,"Admin/send notification.html")

def send_notification_admin_post(request):
    notification = request.POST["notification"]
    obj = Notification()
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.notification = notification
    obj.save()
    return HttpResponse('''<script>alert("send notification successfully");window.location='/myapp/home/'</script>''')

def view_complaint_admin(request):
    res = Complaint.objects.all()
    return render(request,"Admin/view complaint.html",{'data':res})

def view_complaint_admin_post(request):
    from_date = request.POST["from_date"]
    to_date = request.POST["to_date"]
    res = Complaint.objects.filter(date__range=(from_date, to_date))
    return render(request,"Admin/view complaint.html",{'data':res})
def view_course(request):
    res=Course.objects.all()
    return render(request,"Admin/view course.html",{'data':res})

def view_course_post(request):
    search = request.POST["textfield"]
    res = Course.objects.filter(Course_name__icontains=search)
    return render(request,"Admin/view course.html",{'data':res})

def delete_course(request,id):
    data=Course.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("course deleted succesfully");window.location='/myapp/view_course/'</script>''')



def view_department(request):
    res = Department.objects.all()
    return render(request,"Admin/view department.html",{"data":res})

def delete_department(request,id):
    data=Department.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("department deleted succesfully");window.location='/myapp/view_department/'</script>''')

def view_department_post(request):
    textfield = request.POST["textfield"]
    res = Department.objects.filter(department_name__icontains=textfield)
    return render(request, "Admin/view department.html", {"data": res})


def view_office_staff(request):
    res = Office_staff.objects.all()
    return render(request,"Admin/view office staff.html",{'data':res})

def delete_office_staff(request,id):
    data=Office_staff.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("office staff deleted successfully");window.location='/myapp/view_office_staff/'</script>''')

def view_office_staff_post(request):
    textfield = request.POST["textfield"]
    res = Office_staff.objects.filter(office_staff_name__icontains=textfield)
    return render(request,"Admin/view office staff.html",{'data':res})

def view_student_admin(request):
    res=Student.objects.all()
    return render(request,"Admin/view student.html",{'data':res})

def delete_student_admin(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("student deleted successfully");window.location='/myapp/view_student_admin/'</script>''')

def view_student_admin_post(request):
    textfield = request.POST["textfield"]
    res = Student.objects.filter(name__icontains=textfield)
    return render(request, "Admin/view student.html", {"data": res})

def view_teachers(request):
    res=Teachers.objects.all()
    return render(request,"Admin/view teachers.html",{"data":res})

def delete_teachers(request,id):
    data=Teachers.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("teacher deleted successfully");window.location='/myapp/view_teachers/'</script>''')

def view_teachers_post(request):
    textfield = request.POST["textfield"]
    res = Teachers.objects.filter(name__icontains=textfield)
    return render(request, "Admin/view teachers.html", {"data": res})







def edit_course(request,id):
    res1 = Course.objects.get(id=id)
    res = Department.objects.all()
    return render(request,"Admin/edit course.html",{'data':res,'data1':res1})

def edit_course_post(request):
    Course_name = request.POST["Course_name"]
    Semester = request.POST["Semester"]
    dept=request.POST["select"]
    id = request.POST["id"]

    obj = Course.objects.get(id=id)
    obj.Course_name = Course_name
    obj.Semester = Semester
    obj.save()
    return HttpResponse('''<script>alert("course updated succesfully");window.location='/myapp/view_course/'</script>''')


def view_subjects(request):
    res=Subject.objects.all()
    return render(request,"Admin/view subjects.html",{'data':res})

def delete_subjects(request,id):
    data=Subject.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("subject deleted successfully");window.location='/myapp/view_subjects/'</script>''')

def view_subjects_post(request):
    textfield = request.POST["textfield"]
    res = Subject.objects.filter(subject__icontains=textfield)

    return render(request, "Admin/view subjects.html", {"data": res})

def edit_subject(request,id):
    res = Subject.objects.get(id=id)
    return render(request,"Admin/edit subject.html",{'data': res})

def edit_subject_post(request):
    subject = request.POST["subject"]
    id = request.POST["id"]
    res = Subject.objects.get(id=id)
    res.subject = subject
    res.save()
    return HttpResponse('''<script>alert("edited subject successfully");window.location='/myapp/view_subjects/'</script>''')

def edit_teacher(request,id):
    res = Teachers.objects.get(id=id)
    res1 = Department.objects.all()

    return render(request,"Admin/edit teacher.html",{'data':res,'data1':res1})

def edit_teacher_post(request):
    name = request.POST["name"]
    department = request.POST["department"]
    phone_number = request.POST["phone_number"]
    email_id = request.POST["email_id"]
    id = request.POST["id"]

    obj = Teachers.objects.get(id=id)
    if 'photo' in request.FILES:
        photo = request.FILES["photo"]
        from datetime import datetime
        date = 'teacher/'+datetime.now().strftime('%Y%m%d-%H%m%d') + photo.name
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path
        obj.save()
    obj.name = name
    obj.DEPARTMENT_id = Department.objects.get(id=department).id
    obj.email_id = email_id
    obj.phone_number = phone_number
    obj.save()
    return HttpResponse('''<script>alert("teacher edited successfully");window.location='/myapp/view_teachers/'</script>''')

def edit_office_staff(request,id):
    res = Office_staff.objects.get(id=id)
    return render(request,"Admin/edit office staff.html",{'data':res})

def edit_office_staff_post(request):
    office_staff_name = request.POST["office_staff_name"]
    office_staff_phone_number = request.POST["office_staff_phone_number"]
    email_id = request.POST["email_id"]
    id = request.POST['id']



    obj = Office_staff.objects.get(id=id)
    if 'office_staff_photo' in request.FILES:
        office_staff_photo = request.FILES["office_staff_photo"]
        from datetime import datetime
        date = 'office_staff/'+datetime.now().strftime('%Y%m%d-%H%m%d') + office_staff_photo.name
        fs = FileSystemStorage()
        fs.save(date, office_staff_photo)
        path = fs.url(date)
        obj.office_staff_photo = path

    obj.office_staff_name = office_staff_name
    obj.office_staff_phone_number = office_staff_phone_number
    obj.email_id = email_id
    Login.objects.filter(id=obj.LOGIN_id).update(username=email_id)
    obj.save()
    return HttpResponse('''<script>alert("office staff edited successfully");window.location='/myapp/view_office_staff/'</script>''')

def edit_student(request,id):
    res = Student.objects.get(id=id)
    res1 = Course.objects.all()
    return render(request,"Admin/edit student.html",{'data':res,'data1':res1})




def edit_student_post(request):
    name = request.POST["name"]
    house_name = request.POST["house_name"]
    street = request.POST["street"]
    pin = request.POST["pin"]
    email_id = request.POST["email_id"]
    post = request.POST["post"]
    register_number = request.POST["register_number"]
    course = request.POST["course"]
    admission_year = request.POST["admission_year"]
    phone_number = request.POST["phone_number"]
    date_of_birth = request.POST["date_of_birth"]
    gender = request.POST["gender"]
    id = request.POST["sid"]
    print(id+"vhhhg")
    obj = Student.objects.get(id=id)
    if 'photo' in request.FILES:
        photo = request.FILES["photo"]
        from datetime import datetime
        date = 'students/'+datetime.now().strftime('%Y%m%d-%H%m%d') + photo.name
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path
        obj.save()

    obj.name = name
    obj.house_name = house_name
    obj.street = street
    obj.pin = pin
    obj.email_id = email_id
    obj.post = post
    obj.register_number = register_number
    obj.COURSE_id = course
    obj.admission_year = admission_year
    obj.register_number = register_number
    obj.phone_number = phone_number
    obj.date_of_birth = date_of_birth
    obj.gender = gender
    obj.save()

    return HttpResponse('''<script>alert("student edited successfully");window.location='/myapp/view_student_admin/'</script>''')

def change_password_collegeofficestaff(request):
    return render(request,"college office staff/change password.html")

def change_password_collegeofficestaff_post(request):
    current_password = request.POST["current_password"]
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]
    log = Login.objects.filter(password=current_password)
    if log.exists():
        log1 = Login.objects.get(password=current_password,id = request.session['lid'])
        if new_password == confirm_password:
            log1 = Login.objects.filter(password=current_password,id = request.session['lid']).update(password=new_password)
            return HttpResponse('''<script>alert('password changed');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_collegeofficestaff/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_collegeofficestaff/'</script>''')


def send_complaint_reply_collegeofficestaff(request,id):
    return render(request,"Admin/send complaint reply.html",{'id':id})

def send_complaint_reply_collegeofficestaff_post(request):
    reply = request.POST["reply"]
    id = request.POST["id"]
    res = Complaint.objects.filter(id=id).update(reply=reply,status='replied')
    return HttpResponse('''<script>alert("replied successfully");window.location='/myapp/view_complaint_collegeofficestaff/'</script>''')

def staff_view_profile(request):
    obj = Office_staff.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"college office staff/staff view profile.html",{'data':obj})

def edit_club(request,id):
    res = Club.objects.get(id=id)
    return render(request,"college office staff/edit club.html",{'data':res})

def edit_club_post(request):
    name = request.POST["name"]
    description = request.POST["description"]
    id = request.POST['id']



    obj = Club.objects.get(id=id)
    if 'club_logo' in request.FILES:
        logo = request.FILES["club_logo"]
        from datetime import datetime
        date = 'club/'+datetime.now().strftime('%Y%m%d-%H%m%d') + logo.name
        fs = FileSystemStorage()
        fs.save(date, logo)
        path = fs.url(date)
        obj.logo = path
        obj.save()

    obj.name = name
    obj.description = description
    # Login.objects.filter(id=obj.LOGIN_id).update(username=email_id)
    obj.save()
    return HttpResponse('''<script>alert("club edited successfully");window.location='/myapp/view_club/'</script>''')


def view_approved_bus_pass(request):
    var = Bus_pass.objects.filter(status='approved')
    return render(request,"college office staff/view approved bus pass.html",{'data':var})

def edit_approved_bus_pass_post(request):
    textfield = request.POST["textfield"]
    return HttpResponse("success")





def view_complaint_collegeofficestaff(request):
    res = Complaint.objects.all()
    return render(request,"college office staff/view complaint.html",{'data':res})

def view_complaint_collegeofficestaff_post(request):
    from_date = request.POST["from_date"]
    to_date = request.POST["to_date"]
    res = Complaint.objects.filter(date__range=(from_date, to_date))
    return render(request,"college office staff/view complaint.html",{'data':res})

def view_id_card_approved(request):
    var = Id_card.objects.filter(status='approved')
    return render(request,"college office staff/view id card approved.html",{'data':var})

def view_id_card_approved_post(request):
    textfield = request.POST["textfield"]
    return HttpResponse("success")

def view_id_card_rejected(request):
    var = Id_card.objects.filter(status='rejected')
    return render(request,"college office staff/view id card rejected.html",{'data':var})

def view_id_card_rejected_post(request):
    textfield = request.POST["textfield"]
    return HttpResponse("success")

def view_bus_pass_request(request):
    var = Bus_pass.objects.filter(status='pending')
    return render(request,"college office staff/view bus pass request.html",{'data':var})

def view_id_card_request(request):
    var = Id_card.objects.filter(status='pending')
    return render(request,"college office staff/view id card request.html",{'data':var})
def view_rejected_bus_pass(request):
    var = Bus_pass.objects.filter(status='rejected')
    return render(request,"college office staff/view rejected bus pass.html",{'data':var})

def view_rejected_bus_pass_post(request):
    textfield = request.POST["textfield"]
    return HttpResponse("success")





def view_student_collegeofficestaff(request):
    res=Student.objects.all()
    return render(request,"college office staff/view student.html",{'data':res})

def view_student_collegeofficestaff_post(request):
    textfield = request.POST["textfield"]
    res = Student.objects.filter(name__icontains=textfield)
    return render(request, "college office staff/view student.html", {"data": res})

def send_notification_collegeofficestaff(request):
    return render(request,"college office staff/send notification.html")

def send_notification_collegeofficestaff_post(request):
    notification = request.POST["notification"]
    obj = Notification_office_staff()
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.notification = notification
    obj.OFFICE_STAFF = Office_staff.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("send notification successfully");window.location='/myapp/home_collegeofficestaff/'</script>''')






def change_password_teacher(request):
    return render(request,"teachers/change password.html")

def change_password_teacher_post(request):
    current_password = request.POST["current_password"]
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]
    log = Login.objects.filter(password=current_password)
    if log.exists():
        log1 = Login.objects.get(password=current_password,id = request.session['lid'])
        if new_password == confirm_password:
            log1 = Login.objects.filter(password=current_password,id = request.session['lid']).update(password=new_password)
            return HttpResponse('''<script>alert('password changed');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_teacher/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_teacher/'</script>''')

def send_notification_teacher(request):
    return render(request,"teachers/send notification.html")

def send_notification_teacher_post(request):
    notification = request.POST["notification"]
    obj = Notification_teacher()
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.notification = notification
    obj.TEACHERS = Teachers.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("send notification successfully");window.location='/myapp/home_teachers/'</script>''')



def teacher_view_profile(request):
    obj = Teachers.objects.get(LOGIN_id=request.session['lid'])
    return render(request, "teachers/teacher view profile.html", {'data': obj})

def view_student_teacher(request):
    res=Student.objects.all()
    return render(request,"teachers/view student.html",{'data':res})

def view_student_teacher_post(request):
    textfield = request.POST["textfield"]
    res = Student.objects.filter(name__icontains=textfield)
    return render(request, "teachers/view student.html", {"data": res})


# Club.objects.get(LOGIN_id=110).delete()
def attendance(request,id):
    sub_obj=Subject.objects.get(id=id)
    res=Student.objects.filter(COURSE_id=sub_obj.COURSE_id,)
    year=0
    if sub_obj.sem=="1" or sub_obj.sem=="2":
        year=1
    elif sub_obj.sem=="3" or sub_obj.sem=="4":
        year=2
    elif sub_obj.sem=="5" or sub_obj.sem=="6":
        year=3
    data=[]
    for i in res:
        diff=datetime.datetime.now().year-int(i.admission_year)
        print(diff)
        if diff==year:
            data.append({
                "photo":i.photo, "name":i.name,"register_number":i.register_number,"id":i.id
            })



    return render(request,"teachers/attendance.html",{'data':data,'id':id})

def attendance_post(request):
    atmark = request.POST.getlist("atmark")
    sid=request.POST['sid']
    hour=request.POST['hourSelect']
    sub_obj = Subject.objects.get(id=sid)
    res = Student.objects.filter(COURSE_id=sub_obj.COURSE_id, )
    year=0
    if sub_obj.sem == "1" or sub_obj.sem == "2":
        year = 1
    elif sub_obj.sem == "3" or sub_obj.sem == "4":
        year = 2
    elif sub_obj.sem == "5" or sub_obj.sem == "6":
        year = 3
    data = []
    for i in res:
        diff = datetime.datetime.now().year - int(i.admission_year)
        print(diff)
        if diff == year:
            data.append({
                "photo": i.photo, "name": i.name, "register_number": i.register_number, "id": int(i.id)
            })
    for i in data:
        if str(i['id']) in atmark:
            res = Attendance()
            res.STUDENT_id=i['id']
            res.SUBJECT_id=sid
            res.date=datetime.datetime.now().strftime('%Y-%m-%d')
            res.hour=hour
            res.status="Present"
            res.save()
        else:
            res = Attendance()
            res.STUDENT_id=i['id']
            res.SUBJECT_id=sid
            res.date=datetime.datetime.now().strftime('%Y-%m-%d')
            res.hour=hour
            res.status="Absent"
            res.save()

    # print(atmark)

    # for i in atmark:

    return HttpResponse('''<script>alert("Attendance Marked Succesfully");window.location='/myapp/teacher_view_subject_allocation/'</script>''')

# Student.objects.all().delete()

def subjectallocation(request):
    res = Subject.objects.all()
    res2 = Teachers.objects.all()
    return render(request,"Admin/subjectallocation.html",{'data':res,'data2':res2})

def subjectallocation_post(request):
    subject = request.POST['select']
    teacher = request.POST['select2']
    s = Sujectallocation()
    s.SUBJECT_id = subject
    s.TEACHERS_id = teacher
    s.save()

    return HttpResponse('''<script>alert("Allocated Successfully");window.location='/myapp/home/'</script>''')




def view_allocation(request):
    res=Sujectallocation.objects.all()
    return render(request,"Admin/viewallocation.html",{'data':res})

def view_allocation_post(request):
    textfield = request.POST["textfield"]
    res = Sujectallocation.objects.filter(TEACHERS__name__icontains=textfield)
    return render(request, "Admin/viewallocation.html", {"data": res})


def teacher_view_subject_allocation(request):
    res=Sujectallocation.objects.filter(TEACHERS__LOGIN_id=request.session['lid'])
    return render(request,"teachers/teacherviewsubjectallocation.html",{'data':res})

def teacher_view_subject_allocation_post(request):
    textfield = request.POST["textfield"]
    res = Sujectallocation.objects.filter(name__icontains=textfield)
    return render(request, "teachers/teacherviewsubjectallocation.html", {"data": res})


def delete_allocation(request,id):
    data=Sujectallocation.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("Allocation Deleted successfully");window.location='/myapp/view_allocation/'</script>''')






def home_club(request):
    return render(request,"club portal/club_home.html")


def change_password_club(request):
    return render(request,"club portal/change password.html")

def change_password_club_post(request):
    current_password = request.POST["current_password"]
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]
    log = Login.objects.filter(password=current_password)
    if log.exists():
        log1 = Login.objects.get(password=current_password,id = request.session['lid'])
        if new_password == confirm_password:
            log1 = Login.objects.filter(password=current_password,id = request.session['lid']).update(password=new_password)
            return HttpResponse('''<script>alert('password changed');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_club/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid password');window.location='/myapp/change_password_club/'</script>''')
def club_view_profile(request):
    obj = Club.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"club portal/club view profile.html",{'data':obj})




def view_member_request(request):
    res = Club_members.objects.filter(CLUB__LOGIN_id=request.session['lid'],status='pending')
    req = []
    print(res)
    for i in res:
        print(i)
        if i.LOGIN.type == 'student':
            std = Student.objects.get(LOGIN_id=i.LOGIN_id)
            req.append(
                {'id': i.id, 'date': i.date, 'status': i.status, 'name': std.name, 'photo': std.photo, 'house_name': std.house_name,
                 'street': std.street, 'pin': std.pin, 'post': std.post, 'register_number': std.register_number,
                 'date_of_birth': std.date_of_birth, 'phone_number': std.phone_number, 'email_id': std.email_id})
    return render(request, "club portal/view member request and accept request.html", {'data': req})

        # name= ''
        # photo= ''
        # house_name= ''
        # street= ''
        # pin= ''
        # post= ''
        # register_number= ''
        # date_of_birth= ''
        # phone_number= ''
        # email_id= ''
        # if Club_members.objects.filter(LOGIN_id=i.LOGIN_id).exists():
        #     continue

            # name= std.name
            # photo= std.photo
            # house_name= std.house_name
            # street= std.street
            # pin= std.pin
            # post= std.post
            # register_number= std.register_number
            # date_of_birth= std.date_of_birth
            # phone_number= std.phone_number
            # email_id= std.email_id


def approved_member_request(request):
    res = Club_members.objects.filter(CLUB__LOGIN_id=request.session['lid'],status='approved')
    req = []
    for i in res:
        name= ''
        photo= ''
        house_name= ''
        street= ''
        pin= ''
        post= ''
        register_number= ''
        date_of_birth= ''
        phone_number= ''
        email_id= ''
        if i.LOGIN.type=='student':
            std = Student.objects.get(LOGIN_id=i.LOGIN_id)
            name= std.name
            photo= std.photo
            house_name= std.house_name
            street= std.street
            pin= std.pin
            post= std.post
            register_number= std.register_number
            date_of_birth= std.date_of_birth
            phone_number= std.phone_number
            email_id= std.email_id
        req.append({'id': i.id,'date':i.date,'status':i.status,'name':name,'photo':photo,'house_name':house_name,'street':street,'pin':pin,'post':post,'register_number':register_number,'date_of_birth':date_of_birth,'phone_number':phone_number,'email_id':email_id})
    return render(request,"club portal/view approved members.html",{'data':req})

def rejected_member_request(request):
    res = Club_members.objects.filter(CLUB__LOGIN_id=request.session['lid'],status='rejected')
    req = []
    for i in res:
        name= ''
        photo= ''
        house_name= ''
        street= ''
        pin= ''
        post= ''
        register_number= ''
        date_of_birth= ''
        phone_number= ''
        email_id= ''
        if i.LOGIN.type=='student':
            std = Student.objects.get(LOGIN_id=i.LOGIN_id)
            name= std.name
            photo= std.photo
            house_name= std.house_name
            street= std.street
            pin= std.pin
            post= std.post
            register_number= std.register_number
            date_of_birth= std.date_of_birth
            phone_number= std.phone_number
            email_id= std.email_id
        req.append({'id': i.id,'date':i.date,'status':i.status,'name':name,'photo':photo,'house_name':house_name,'street':street,'pin':pin,'post':post,'register_number':register_number,'date_of_birth':date_of_birth,'phone_number':phone_number,'email_id':email_id})
    return render(request,"club portal/view rejected members.html",{'data':req})


def delete_club_member(request,id):
    data=Club_members.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("member deleted successfully");window.location='/myapp/approved_member_request/'</script>''')

def delete_rejected_member(request,id):
    data=Club_members.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("member deleted successfully");window.location='/myapp/rejected_member_request/'</script>''')

def delete_bus_pass(request,id):
    data=Bus_pass.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("bus pass request deleted successfully");window.location='/myapp/view_approved_bus_pass/'</script>''')

def delete_id_card_rejected(request,id):
    data=Id_card.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("deleted successfully");window.location='/myapp/view_id_card_rejected/'</script>''')

def delete_id_card_approved(request,id):
    data=Id_card.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("deleted successfully");window.location='/myapp/view_approved_id_card/'</script>''')


def approve_member_request(request,id):
    Club_members.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert("member approved");window.location='/myapp/view_member_request/'</script>''')

def approve_bus_pass_request(request,id):
    Bus_pass.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert("bus pass approved");window.location='/myapp/view_bus_pass_request/'</script>''')

def approve_id_card_request(request,id):
    Id_card.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert("id card approved");window.location='/myapp/view_id_card_request/'</script>''')

def reject_member_request(request,id):
    Club_members.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert("member rejected");window.location='/myapp/view_member_request/'</script>''')

def reject_bus_pass_request(request,id):
    Bus_pass.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert("bus pass rejected");window.location='/myapp/view_bus_pass_request/'</script>''')

def reject_id_card_request(request,id):
    Id_card.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert("id card rejected");window.location='/myapp/view_bus_pass_request/'</script>''')
def view_member_request_post(request):
    textfield = request.POST["textfield"]
    textfield2 = request.POST["textfield2"]
    return HttpResponse("success")


def view_member_post(request):
    textfield = request.POST["textfield"]
    return HttpResponse("success")
def send_notification_club(request):
    return render(request,"club portal/send notification.html")

def send_notification_club_post(request):
    notification = request.POST["notification"]
    obj = Notification_club()
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.notification = notification
    obj.CLUB = Club.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("send notification successfully");window.location='/myapp/home_club/'</script>''')



def home_collegeofficestaff(request):
    return render(request,"college office staff/office_staff_home.html")

def add_club(request):
    return render(request,"college office staff/add club.html")

def add_club_post(request):
    name = request.POST["name"]
    description = request.POST["description"]
    club_logo = request.FILES["club_logo"]
    from datetime import datetime
    date = 'club/'+datetime.now().strftime('%Y%m%d-%H%m%d') + club_logo.name
    fs = FileSystemStorage()
    fs.save(date, club_logo)
    path = fs.url(date)

    lobj = Login()
    lobj.username = name

    password='0000'
    lobj.password = password
    lobj.type = 'club'
    lobj.save()
    obj = Club()
    obj.name = name
    obj.description = description
    obj.OFFICE_STAFF = Office_staff.objects.get(LOGIN=request.session['lid'])
    obj.logo = path
    obj.LOGIN = lobj
    obj.save()
    return HttpResponse('''<script>alert("club added succesfully");window.location='/myapp/add_club/'</script>''')

def view_club(request):
    res = Club.objects.all()
    return render(request,"college office staff/view club.html",{'data':res})

def delete_club(request,id):
    data=Club.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert("club deleted successfully");window.location='/myapp/view_club/'</script>''')

def view_club_post(request):
    textfield = request.POST["textfield"]
    res = Club.objects.filter(name__icontains=textfield)
    return render(request,"college office staff/view club.html",{'data':res})


def home_teachers(request):
    return render(request,"teachers/teacher_home.html")





def login_student(request):
    username = request.POST["username"]
    password = request.POST["password"]
    var = Login.objects.filter(username=username, password=password)
    if var.exists():
        var1 = Login.objects.get(username=username, password=password)
        lid = var1.id
        if var1.type == 'student':
            return JsonResponse({"status": "ok",'lid':str(lid)})
        else:
            return JsonResponse({"status": "no"})
    else:
        return JsonResponse({"status":"no"})


def view_profile_student(request):
    lid = request.POST["lid"]
    prof = Student.objects.get(LOGIN_id=lid)
    date = Notification.objects.all().order_by('-date')
    l = date[0]
    d=l.date.strftime("%d-%B-%Y")
    print(l)
    return JsonResponse({"status":"ok",'name':prof.name,'photo':prof.photo,
                         'house_name':prof.house_name,'street':prof.street,
                         'pin':prof.pin,'post':prof.post,'register_number':prof.register_number,
                         'date_of_birth':prof.date_of_birth.strftime("%d-%m-%Y"),'phone_number':prof.phone_number,'date':d,'email_id':prof.email_id,'admission_year':prof.admission_year})

def send_bus_pass_request(request):
    lid = request.POST["lid"]
    department = request.POST["department"]
    f_place = request.POST["f_place"]
    to_place = request.POST["to_place"]
    academic_year = request.POST["academic_year"]
    file = request.POST["file"]
    bus = Bus_pass()
    bus.DEPARTMENT_id = Student.objects.get(LOGIN_id=lid).COURSE.DEPARTMENT.id
    bus.STUDENT = Student.objects.get(LOGIN_id=lid)
    bus.f_place = f_place
    bus.to_place = to_place
    bus.academic_year = academic_year
    import datetime
    bus.date = datetime.datetime.now().date()
    bus.status = "pending"
    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a = base64.b64decode(file)
    fh = open("//Users//younuz//PycharmProjects//studentportal//media//"+date+".jpg","wb")
    fh.write(a)
    fh.close()
    path = "/media/"+date+".jpg"
    bus.file = path
    bus.date = datetime.datetime.now().date()
    bus.status = 'pending'
    bus.save()


    return JsonResponse({"status": "ok"})
def send_id_card_request(request):
    lid = request.POST["lid"]
    # department = request.POST["department"]
    # print(department)
    academic_year = request.POST["academic_year"]
    file = request.POST["photo"]
    id_card = Id_card()
    id_card.DEPARTMENT_id= Student.objects.get(LOGIN_id=lid).COURSE.DEPARTMENT.id
    id_card.STUDENT = Student.objects.get(LOGIN_id=lid)
    id_card.academic_year = academic_year
    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a = base64.b64decode(file)
    fh = open("//Users//younuz//PycharmProjects//studentportal//media//" + date + ".jpg", "wb")
    fh.write(a)
    fh.close()
    path = "/media/" + date + ".jpg"
    id_card.file = path
    id_card.date = datetime.datetime.now().date()
    id_card.status = 'pending'
    id_card.save()
    return JsonResponse({"status":"ok"})

def view_club_student(request):
    clubnames = Club.objects.all()
    l = []
    for i in clubnames:
        l.append({'id': i.id, 'name': i.name,'logo': i.logo,'description': i.description})
    return JsonResponse({"status": "ok", 'data': l})

def join_club(request):
    lid = request.POST["lid"]
    club = request.POST["club"]
    print(club)
    clb = Club_members()
    from datetime import datetime
    clb.date = datetime.now().today()
    clb.status = 'pending'
    clb.LOGIN_id = lid
    clb.CLUB_id = club
    clb.save()
    return JsonResponse({"status":"ok"})

def view_club_request_status(request):
    lid = request.POST["lid"]
    clubstat = Club_members.objects.filter(LOGIN_id=lid)
    l = []
    for i in clubstat:
        l.append({'id': i.id, 'CLUB': i.CLUB.name, 'description': i.CLUB.description, 'logo': i.CLUB.logo, 'status': i.status,'date': i.date})
    return JsonResponse({"status":"ok",'data':l})

def view_attendance(request):
    lid = request.POST["lid"]
    att = Attendance.objects.filter(STUDENT__LOGIN_id=lid)
    l = []
    for i in att:
        l.append({'id': i.id,'subject': i.SUBJECT.subject, 'date': i.date,'hour': i.hour, 'status': i.status})
    return JsonResponse({"status": "ok", 'data': l})

def view_attendancesea(request):
    lid = request.POST["lid"]
    date = request.POST["date"]
    att = Attendance.objects.filter(STUDENT__LOGIN_id=lid,date=date)
    l = []
    for i in att:
        l.append({'id': i.id,'subject': i.SUBJECT.subject, 'date': i.date,'hour': i.hour, 'status': i.status})
    return JsonResponse({"status": "ok", 'data': l})

def send_complaint(request):
    lid = request.POST["lid"]
    complaint = request.POST["complaint"]
    com = Complaint()
    com.complaint = complaint
    com.STUDENT = Student.objects.get(LOGIN_id=lid)
    com.reply = 'pending'
    com.status = 'pending'
    from datetime import datetime
    com.date = datetime.now().date()
    com.save()
    return JsonResponse({"status":"ok"})

def view_complaint_reply(request):
    lid = request.POST["lid"]
    comreply = Complaint.objects.filter(STUDENT__LOGIN_id=lid)
    l = []
    for i in comreply:
        l.append({'id':i.id,'complaint':i.complaint,'date':i.date,'status':i.status,'reply':i.reply})
    return JsonResponse({"status":"ok",'data':l})

def view_department_student(request):
    lid = request.POST["lid"]
    viewdep = Department.objects.filter()
    l = []
    for i in viewdep:
        l.append({'id':i.id,'department':i.department_name})
    return JsonResponse({"status":"ok",'data':l})

def change_password_student(request):
    current_password = request.POST["current_password"]
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]
    lid = request.POST["lid"]
    log = Login.objects.filter(password=current_password)
    if log.exists():
        log1 = Login.objects.get(password=current_password, id=lid)
        if new_password == confirm_password:
            log1 = Login.objects.filter(password=current_password, id=lid).update(
                password=new_password)
            return JsonResponse({"status":"ok"})
        else:
            return JsonResponse({"status":"no"})
    else:
        return JsonResponse({"status":"no"})



def view_notification(request):
    lid = request.POST["lid"]
    notify = Notification.objects.all().order_by('-date', '-id')
    notifyclub= Notification_club.objects.filter(CLUB__LOGIN__student__LOGIN_id=lid).order_by('-date', '-id')
    notifyoffice= Notification_office_staff.objects.all().order_by('-date', '-id')
    notifyteacher= Notification_teacher.objects.filter(TEACHERS__LOGIN__student__LOGIN_id=lid).order_by('-date', '-id')
    l = []
    for i in notify:
        l.append({'id':i.id,'notification':i.notification,'date':i.date})
    # for i in notifyclub:
    #     l.extend({'id':i.id,'notification':i.notification,'date':i.date})
    # for i in notifyoffice:
    #     l.extend({'id':i.id,'notification':i.notification,'date':i.date})
    # for i in notifyteacher:
    #     l.extend({'id':i.id,'notification':i.notification,'date':i.date})
    print(l)
    return JsonResponse({"status":"ok",'data':l})


def view_push_notification(request):
    nid = request.POST["nid"]
    res=Notification.objects.filter(id__gt=nid).order_by('id')
    if res.exists():
        i=res[0]
        return JsonResponse({"status":"ok",'nid':i.id,"message":i.notification})
    else:
        return JsonResponse({"status":"no"})


# def view_date_notification(request):
#     # lid = request.POST["lid"]
#     notify = Notification.objects.all().order_by('-date')
#     l = notify[0]
#     print(l)
#     return JsonResponse({"status":"ok",'date':l.date})


def view_id_card_request_student(request):
    lid = request.POST["lid"]
    notify = Id_card.objects.filter(STUDENT__LOGIN_id=lid).order_by('-date')
    l = []
    for i in notify:
        l.append({'id':i.id,'photo':i.file,'date':i.date,'academic_year':i.academic_year,'status':i.status})
    return JsonResponse({"status":"ok",'data':l})


def view_bus_pass_request_student(request):
    lid = request.POST["lid"]
    notify = Bus_pass.objects.filter(STUDENT__LOGIN_id=lid).order_by('-date')
    l = []
    for i in notify:
        l.append({'id':i.id,'photo':i.file,'date':i.date,'from_location':i.f_place,'to_location':i.to_place,'academic_year':i.academic_year,'status':i.status})
    return JsonResponse({"status":"ok",'data':l})



def logout_student(request):
    return JsonResponse({"status":"ok"})




