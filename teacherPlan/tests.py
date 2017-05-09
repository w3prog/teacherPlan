#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from moevmCommon.models import *
c = Client()
pagePath = "/teacherPlan/"


class GetPagesTest(TestCase):
  """
    Тесты на получение страниц без авторизации
  """

  def setUp(self):
    # Создаем активного пользователя
    self.gc = Client(enforce_csrf_checks=False)
    self.username = 'admin'
    self.password = 'secret'
    self.type = "t"

    self.user = User.objects.create_user(self.username,
                                         'mail@example.com')
    self.user.set_password(self.password)
    self.user.first_name = "df"
    self.user.last_name = "dfsdf"

    self.user.save()
    self.userprofile = UserProfile.objects.create(user=self.user,type=type,patronymic="123")
    self.tp = TeacherPlan.objects.create(person_profile=self.userprofile,start_date=datetime.datetime.now().year)
    self.study_book = StudyBook.objects.create(name="hdf",type="sf",volume=1.0,vulture=1,finishDate="123")
    self.nir = NIR.objects.create(name="hdf",period="fdfa",role="123",organisation="231")
    self.participation = Participation.objects.create(name="hdf",date="123",level="12d",report="fadf")
    self.qualification = Qualification.objects.create(period="hdf",form_training="sda",document="fasd")
    self.another_work = AnotherWork.objects.create(work_date="hdf",type_work="ddf")
    self.teacher_publication = TeacherPublication.objects.create(name_work="hdf",
                                                                 type="12",
                                                                 volume=2.0,
                                                                 name_publisher="1234")
    self.academic_discipline = AcademicDiscipline.objects.create(name="hdf",type="123",characterUpdate="123")

    self.tp.study_books = [self.study_book]
    self.tp.NIRS = [self.nir]
    self.tp.participations = [self.participation]
    self.tp.qualifications = [self.qualification]
    self.tp.anotherworks = [self.another_work]
    self.tp.publications = [self.teacher_publication]
    self.tp.disciplines = [self.academic_discipline]

    self.tp.save()

    self.user.is_staff = True
    self.user.is_superuser = True
    self.user.save()
    # Создаем неактивного пользователя
    self.username2 = 'adminBloked'
    self.user2 = User.objects.create_user(self.username2,
                                          'mail@example.com')
    self.user2.set_password(self.password)
    self.user2.is_staff = True
    self.user2.is_superuser = True
    self.user2.is_active = False

    self.user2.save()
    self.gc.login(username=self.username, password=self.password)

  # тест на авторизацию с правильным логином и паролем
  def test_success(self):
    response = c.post(pagePath+ 'login', {'loginField': 'admin', 'passwordField': 'secret'})
    self.assertRedirects(response, pagePath, status_code=302, target_status_code=200, msg_prefix='')

  # Тест на отправку пустых полей.
  def test_void_user(self):
    response = c.post(pagePath+ 'login', {'loginField': '', 'passwordField': ''})
    self.assertRedirects(response, pagePath + "loginwitherror", status_code=302, target_status_code=200, msg_prefix='')

  # тест на авторизацию с неправильным логином
  def test_bad_login(self):
    response = c.post(pagePath+ 'login', {'loginField': 'admin2', 'passwordField': 'secret'})
    self.assertRedirects(response, pagePath+"loginwitherror", status_code=302, target_status_code=200, msg_prefix='')

  # тест на авторизацию с неправильным паролем
  def test_bad_password(self):
    response = c.post(pagePath+ 'login', {'loginField': 'admin', 'passwordField': 'secret1'})
    self.assertRedirects(response, pagePath + "loginwitherror", status_code=302, target_status_code=200, msg_prefix='')

  # тест на авторизацию неактивного пользователя
  def test_inactive_user(self):
    response = c.post(pagePath+ 'login', {'loginField': 'adminBloked', 'passwordField': 'secret'})
    self.assertRedirects(response, pagePath + "loginwitherror", status_code=302, target_status_code=200, msg_prefix='')


  # тест на главную
  def test_index(self):
    response = c.get(pagePath)
    self.assertEqual(response.status_code, 302)

  # тест на список планов
  def test_planlist(self):
    response = c.get(pagePath+ 'listOfPlans')
    self.assertEqual(response.status_code, 302)

  # тест на новый план
  def test_newPlan(self):
    response = c.get(pagePath + 'allplans')
    self.assertEqual(response.status_code, 301)

  # тест на текущий план
  def test_plan(self):
    response = c.get(pagePath + 'currentPlan')
    self.assertEqual(response.status_code, 301)

  # тест на страницу авторизации
  def test_login_page(self):
    response = c.get(pagePath + 'login')
    self.assertEqual(response.status_code, 200)

  # тест на редактирование настроек
  def test_edit_property(self):
    response = c.get(pagePath + 'editProperty')
    self.assertEqual(response.status_code, 301)

  # тест на страницу регистрации преподавателя
  def test_register_teacher(self):
    response = c.get(pagePath + 'registerTeacher')
    self.assertEqual(response.status_code, 301)

  # на вход авторизованного пользователя
  def test_auth_listOfPlans(self):
    response = self.gc.get(pagePath + 'listOfPlans')
    self.assertEqual(response.status_code, 200)

  def test_auth_currentPlan(self):
    response = self.gc.get(pagePath + 'currentPlan/')
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, pagePath + "plan/add/", status_code=302, target_status_code=200, msg_prefix='')

  def test_auth_plan_add(self):
    response = self.gc.get(pagePath + 'plan/add/')
    self.assertEqual(response.status_code, 200)

  def test_auth_allplans(self):
    response = self.gc.get(pagePath + 'allplans/')
    self.assertEqual(response.status_code, 200)

  # неполучается проверить logout.
  def test_auth_logout(self):
    cookies = self.gc.cookies
    response = self.gc.get(pagePath + 'logout')
    self.assertEqual(response.status_code, 302)
    #self.assertNotEquals(cookies, self.gc.cookies)

  def test_auth_plan(self):
    response = self.gc.get(pagePath + 'plan/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_studybookList_plan(self):
    response = self.gc.get(pagePath + 'studybookList/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_disciplineList_plan(self):
    response = self.gc.get(pagePath + 'disciplineList/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_scWorkList_plan(self):
    response = self.gc.get(pagePath + 'scWorkList/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_participationList_plan(self):
    response = self.gc.get(pagePath + 'participationList/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_publicationList_plan(self):
    response = self.gc.get(pagePath + 'publicationList/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_qualificationList_plan(self):
    response = self.gc.get(pagePath + 'qualificationList/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_difWorkList_plan(self):
    response = self.gc.get(pagePath + 'difWorkList/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  def test_auth_studybookList_plan(self):
    response = self.gc.get(pagePath + 'studybookList/' + self.tp.id + "/edit", {"idlink":self.study_book.id})
    self.assertEqual(response.status_code, 200)

  def test_auth_disciplineList_plan(self):
    response = self.gc.get(pagePath + 'disciplineList/' + self.tp.id + "/edit", {"idlink":self.academic_discipline.id})
    self.assertEqual(response.status_code, 200)

  def test_auth_scWorkList_plan(self):
    response = self.gc.get(pagePath + 'scWorkList/' + self.tp.id + "/edit", {"idlink":self.nir.id})
    self.assertEqual(response.status_code, 200)

  def test_auth_participationList_plan(self):
    response = self.gc.get(pagePath + 'participationList/' + self.tp.id + "/edit",{"idlink":self.participation.id})
    self.assertEqual(response.status_code, 200)

  def test_auth_publicationList_plan(self):
    response = self.gc.get(pagePath + 'publicationList/' + self.tp.id + "/edit",{"idlink":self.teacher_publication.id})
    self.assertEqual(response.status_code, 200)

  def test_auth_qualificationList_plan(self):
    response = self.gc.get(pagePath + 'qualificationList/' + self.tp.id + "/edit",{"idqual":self.qualification.id})
    self.assertEqual(response.status_code, 200)


  def test_auth_pdf(self):
    response = self.gc.get(pagePath + 'pdf/' + self.tp.id)
    self.assertEqual(response.status_code, 200)

  # еще нужно сделать тесты на грид операции

  def test_auth_studybookList_add_plan(self):
    response = self.gc.post(pagePath + 'studybookList/' + self.tp.id,
      {
        "name":"sda",
        "type":"Учебник",
        "volume":"1.0",
        "vulture":"fasdf2",
        "finishDate":"fasdf3"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'studybookList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.study_books[1].name,"sda")

  def test_auth_disciplineList_add_plan(self):
    response = self.gc.post(pagePath + 'disciplineList/' + self.tp.id,
      {
        "name":"sda",
        "type":"Лекции",
        "characterUpdate":"123"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'disciplineList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.disciplines[1].name,"sda")

  def test_auth_scWorkList_add_plan(self):
    response = self.gc.post(pagePath + 'scWorkList/' + self.tp.id,
      {
        "name":"sda",
        "period":"Учебник",
        "role":"1.0",
        "organisation":"fasdf2"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'scWorkList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.NIRS[1].name,"sda")

  def test_auth_participationList_add_plan(self):
    response = self.gc.post(pagePath + 'participationList/' + self.tp.id,
      {
        "name":"sda",
        "level":"Учебник",
        "report":"1.0",
        "date":"fasdf2"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'participationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.participations[1].name,"sda")

  def test_auth_publicationList_add_plan(self):
    response = self.gc.post(pagePath + 'publicationList/' + self.tp.id,
      {
        "name_work":"sda",
        "type":"Учебник",
        "volume":"1.0",
        "name_publisher":"fasdf2"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'publicationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.publications[1].name_work,"sda")

  def test_auth_qualificationList_add_plan(self):
    response = self.gc.post(pagePath + 'qualificationList/' + self.tp.id,
      {
        "period":"sda",
        "form_training":"Учебник",
        "document":"1.0"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'qualificationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.qualifications[1].period,"sda")

  def test_auth_difWorkList_add_plan(self):
    response = self.gc.post(pagePath + 'difWorkList/' + self.tp.id,
      {
        "work_date":"sda",
        "type_work":"Учебник"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'difWorkList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.anotherworks[1].work_date,"sda")
  ################################################################################################
  def test_auth_studybookList_update_plan(self):
    response = self.gc.post(pagePath + 'studybookList/' + self.tp.id + "/edit",
      {
        "idlink":self.study_book.id,
        "name":"sda",
        "type":"Учебник",
        "volume":"1.0",
        "vulture":"fasdf2",
        "finishDate":"fasdf3"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'studybookList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.study_books[0].name,"sda")

  def test_auth_disciplineList_update_plan(self):
    response = self.gc.post(pagePath + 'disciplineList/' + self.tp.id + "/edit",
      {
        "idlink":self.academic_discipline.id,
        "name":"sda",
        "type":"Лекции",
        "characterUpdate":"123"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'disciplineList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.disciplines[0].name,"sda")

  def test_auth_scWorkList_update_plan(self):
    response = self.gc.post(pagePath + 'scWorkList/' + self.tp.id + "/edit",
      {
        "idlink":self.nir.id,
                              "name": "sda",
                              "period": "Учебник",
                              "role": "1.0",
                              "organisation": "fasdf2"
                            }
                            )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'scWorkList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.NIRS[0].name, "sda")

  def test_auth_participationList_update_plan(self):
    response = self.gc.post(pagePath + 'participationList/' + self.tp.id + "/edit",
      {
        "idlink":self.participation.id,
        "name":"sda",
        "level":"Учебник",
        "report":"1.0",
        "date":"fasdf2"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'participationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.participations[0].name,"sda")

  def test_auth_publicationList_update_plan(self):
    response = self.gc.post(pagePath + 'publicationList/' + self.tp.id + "/edit",
      {
        "idlink":self.teacher_publication.id,
        "name_work":"sda",
        "type":"Учебник",
        "volume":"1.0",
        "name_publisher":"fasdf2"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'publicationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.publications[0].name_work,"sda")

  def test_auth_qualificationList_update_plan(self):
    response = self.gc.post(pagePath + 'qualificationList/' + self.tp.id + "/edit",
      {
        "idqual":self.qualification.id,
        "period":"sda",
        "form_training":"Учебник",
        "document":"1.0"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'qualificationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.qualifications[0].period,"sda")

  def test_auth_difWorkList_update_plan(self):
    response = self.gc.post(pagePath + 'difWorkList/' + self.tp.id + "/edit",
      {
        "idaw":self.another_work.id,
        "work_date":"sda",
        "type_work":"sda"
      }
    )
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertRedirects(response, pagePath + 'difWorkList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    self.assertEquals(tp.anotherworks[0].work_date,"sda")
  ###############################################################################################

  def test_auth_studybookList_delete_plan(self):
    response = self.gc.post(pagePath + 'studybookList/' + self.tp.id,
                            {"delete":"delete","id":self.study_book.id}
    )
    self.assertRedirects(response, pagePath + 'studybookList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertEquals(tp.study_books,[])

  def test_auth_disciplineList_delete_plan(self):
    response = self.gc.post(pagePath + 'disciplineList/' + self.tp.id,
                            {"delete":"delete", "id":self.academic_discipline.id}
    )
    self.assertRedirects(response, pagePath + 'disciplineList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertEquals(tp.disciplines,[])

  def test_auth_scWorkList_delete_plan(self):
    response = self.gc.post(pagePath + 'scWorkList/' + self.tp.id,
                            {"type": "delete", "id": self.nir.id}
                            )
    self.assertRedirects(response, pagePath + 'scWorkList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertEquals(tp.NIRS, [])

  def test_auth_participationList_delete_plan(self):
    response = self.gc.post(pagePath + 'participationList/' + self.tp.id,
                            {"delete":"delete","id":self.participation.id}
    )
    self.assertEqual(response.status_code, 200)

  def test_auth_publicationList_delete_plan(self):
    response = self.gc.post(pagePath + 'publicationList/' + self.tp.id,
                            {"delete":"delete","id":self.teacher_publication.id}
    )

    self.assertRedirects(response, pagePath + 'publicationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertEquals(tp.publications, [])

  def test_auth_qualificationList_delete_plan(self):
    response = self.gc.post(pagePath + 'qualificationList/' + self.tp.id,
                            {"type":"delete","id":self.qualification.id}
    )
    self.assertRedirects(response, pagePath + 'qualificationList/' + self.tp.id, status_code=302,
                         target_status_code=200, msg_prefix='')
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertEquals(tp.qualifications, [])

  def test_auth_difWorkList_delete_plan(self):
    response = self.gc.post(pagePath + 'difWorkList/' + self.tp.id,
                            {"type":"delete","id":self.another_work.id}
    )
    self.assertRedirects(response, pagePath + 'difWorkList/' + self.tp.id, status_code=302, target_status_code=200,
                         msg_prefix='')
    tp = TeacherPlan.objects.get(id=self.tp.id)
    self.assertEquals(tp.anotherworks, [])

