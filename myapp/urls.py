
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
   path('login/',views.login),
   path('logout/',views.logout),
   path('home/',views.home),



   path('add_course/',views.add_course),
   path('add_department/',views.add_department),
   path('add_office_staff/',views.add_office_staff),
   path('add_student/',views.add_student),
   path('add_subject/',views.add_subject),
   path('add_teacher/',views.add_teacher),
   path('change_password_admin/',views.change_password_admin),
   path('change_password_teacher/',views.change_password_teacher),
   path('change_password_club/',views.change_password_club),
   path('change_password_collegeofficestaff/',views.change_password_collegeofficestaff),
   path('edit_department/<id>',views.edit_department),
   path('send_complaint_reply_admin/<id>',views.send_complaint_reply_admin),
   path('send_complaint_reply_collegeofficestaff/<id>',views.send_complaint_reply_collegeofficestaff),
   path('send_notification_admin/',views.send_notification_admin),
   path('send_notification_club/',views.send_notification_club),
   path('send_notification_collegeofficestaff/',views.send_notification_collegeofficestaff),
   path('send_notification_teacher/',views.send_notification_teacher),
   path('view_complaint_admin/',views.view_complaint_admin),
   path('view_complaint_collegeofficestaff/',views.view_complaint_collegeofficestaff),
   path('view_course/',views.view_course),
   path('delete_course/<id>',views.delete_course),
   path('delete_club/<id>',views.delete_club),
   path('view_department/',views.view_department),
   path('delete_department/<id>', views.delete_department),
   path('view_office_staff/',views.view_office_staff),
   path('delete_office_staff/<id>', views.delete_office_staff),
   path('view_student_admin/',views.view_student_admin),
   path('view_student_admin_post/',views.view_student_admin_post),
   path('view_student_teacher/',views.view_student_teacher),
   path('attendance/<id>',views.attendance),
   path('attendance_post/',views.attendance_post),
   path('subjectallocation/',views.subjectallocation),
   path('subjectallocation_post/',views.subjectallocation_post),
   path('view_allocation/',views.view_allocation),
   path('view_allocation_post/',views.view_allocation_post),
   path('teacher_view_subject_allocation/',views.teacher_view_subject_allocation),
   path('teacher_view_subject_allocation_post/',views.teacher_view_subject_allocation_post),
   path('delete_allocation/<id>',views.delete_allocation),
   path('delete_student_admin/<id>', views.delete_student_admin),
   path('view_student_collegeofficestaff/',views.view_student_collegeofficestaff),
   path('view_teachers/',views.view_teachers),
   path('delete_teachers/<id>', views.delete_teachers),
   path('edit_course/<id>',views.edit_course),
   path('view_subjects/',views.view_subjects),
   path('delete_subjects/<id>', views.delete_subjects),
   path('edit_teacher/<id>',views.edit_teacher),
   path('edit_office_staff/<id>',views.edit_office_staff),
   path('edit_student/<id>',views.edit_student),
   path('edit_subject/<id>', views.edit_subject),
   path('edit_subject_post/', views.edit_subject_post),
   path('edit_club/<id>',views.edit_club),
   path('staff_view_profile/',views.staff_view_profile),
   path('club_view_profile/',views.club_view_profile),
   path('view_member_request/',views.view_member_request),
   path('approve_member_request/<id>',views.approve_member_request),
   path('approved_member_request/',views.approved_member_request),
   path('rejected_member_request/',views.rejected_member_request),
   path('delete_club_member/<id>',views.delete_club_member),
   path('delete_rejected_member/<id>',views.delete_rejected_member),
   path('delete_bus_pass/<id>',views.delete_bus_pass),
   path('reject_member_request/<id>',views.reject_member_request),
   path('add_club/',views.add_club),
   path('teacher_view_profile/',views.teacher_view_profile),
   path('view_approved_bus_pass/',views.view_approved_bus_pass),
   path('view_bus_pass_request/',views.view_bus_pass_request),
   path('approve_bus_pass_request/<id>',views.approve_bus_pass_request),
   path('reject_bus_pass_request/<id>',views.reject_bus_pass_request),
   path('view_club/',views.view_club),
   path('view_complaint_admin/',views.view_complaint_admin),
   path('view_complaint_collegeofficestaff/',views.view_complaint_collegeofficestaff),
   path('view_id_card_approved/',views.view_id_card_approved),
   path('view_id_card_rejected/',views.view_id_card_rejected),
   path('delete_id_card_rejected/<id>',views.delete_id_card_rejected),
   path('delete_id_card_approved/<id>',views.delete_id_card_approved),
   path('view_id_card_request/',views.view_id_card_request),
   path('approve_id_card_request/<id>',views.approve_id_card_request),
   path('reject_id_card_request/<id>',views.reject_id_card_request),
   path('view_rejected_bus_pass/',views.view_rejected_bus_pass),
   path('login_post/',views.login_post),
   path('add_course_post/',views.add_course_post),
   path('add_department_post/',views.add_department_post),
   path('add_office_staff_post/',views.add_office_staff_post),
   path('add_student_post/',views.add_student_post),
   path('add_subject_post/',views.add_subject_post),
   path('add_teacher_post/',views.add_teacher_post),
   path('change_password_admin_post/',views.change_password_admin_post),
   path('change_password_teacher_post/',views.change_password_teacher_post),
   path('change_password_club_post/',views.change_password_club_post),
   path('change_password_collegeofficestaff_post/',views.change_password_collegeofficestaff_post),
   path('edit_department_post/',views.edit_department_post),
   path('send_complaint_reply_admin_post/',views.send_complaint_reply_admin_post),
   path('send_complaint_reply_collegeofficestaff_post/', views.send_complaint_reply_collegeofficestaff_post),
   path('send_notification_admin_post/', views.send_notification_admin_post),
   path('send_notification_club_post/', views.send_notification_club_post),
   path('send_notification_collegeofficestaff_post/', views.send_notification_collegeofficestaff_post),
   path('send_notification_teacher_post/', views.send_notification_teacher_post),
   path('view_complaint_admin_post/', views.view_complaint_admin_post),
   path('view_complaint_collegeofficestaff_post/', views.view_complaint_collegeofficestaff_post),
   path('view_course_post/', views.view_course_post),
   path('view_department_post/', views.view_department_post),
   path('view_office_staff_post/', views.view_office_staff_post),
   path('view_student_teacher_post/', views.view_student_teacher_post),
   path('view_student_collegeofficestaff_post/', views.view_student_collegeofficestaff_post),
   path('view_teachers_post/', views.view_teachers_post),

   path('view_subjects_post/', views.view_subjects_post),
   path('edit_teacher_post/', views.edit_teacher_post),
   path('edit_course_post/', views.edit_course_post),
   path('edit_office_staff_post/', views.edit_office_staff_post),
   path('edit_student_post/', views.edit_student_post),
   path('edit_club_post/', views.edit_club_post),
   path('view_member_request_post/', views.view_member_request_post),
   path('view_member_post/', views.view_member_post),
   path('add_club_post/', views.add_club_post),
   path('send_complaint_reply_admin_post/', views.send_complaint_reply_admin_post),
   path('send_complaint_reply_collegeofficestaff_post/', views.send_complaint_reply_collegeofficestaff_post),
   path('view_club_post/', views.view_club_post),
   path('view_complaint_admin_post/', views.view_complaint_admin_post),
   path('view_complaint_collegeofficestaff_post/', views.view_complaint_collegeofficestaff_post),
   path('view_id_card_approved_post/', views.view_id_card_approved_post),
   path('view_id_card_rejected_post/', views.view_id_card_rejected_post),
   path('view_rejected_bus_pass_post/', views.view_rejected_bus_pass_post),
   path('view_course_post/', views.view_course_post),
   path('view_push_notification/', views.view_push_notification),

   path('login_student/', views.login_student),
   path('view_profile_student/', views.view_profile_student),
   path('send_bus_pass_request/', views.send_bus_pass_request),
   path('view_department_student/', views.view_department_student),
   path('send_id_card_request/', views.send_id_card_request),
   path('join_club/', views.join_club),
   path('view_club_student/', views.view_club_student),
   path('view_club_request_status/', views.view_club_request_status),
   path('view_attendance/', views.view_attendance),
   path('view_attendancesea/', views.view_attendancesea),
   path('send_complaint/', views.send_complaint),
   path('view_complaint_reply/', views.view_complaint_reply),
   path('change_password_student/', views.change_password_student),
   path('view_notification/', views.view_notification),
   path('view_id_card_request_student/', views.view_id_card_request_student),
   path('view_bus_pass_request_student/', views.view_bus_pass_request_student),
   # path('view_date_notification/', views.view_date_notification),

   path('logout_student/', views.logout_student),


   #====club=======
   path('home_club/', views.home_club),
   path('home_collegeofficestaff/', views.home_collegeofficestaff),
   path('home_teachers/', views.home_teachers),
   ]