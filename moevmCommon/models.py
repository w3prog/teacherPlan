#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import forms
from django.utils.encoding import python_2_unicode_compatible
from djangotoolbox.fields import EmbeddedModelField
from djangotoolbox.fields import ListField


def filter_by_foreign_fields(model_manager, **filter_fields):

    def filter_condition(model):

        if not hasattr(model, 'user'):
            return False

        model_fields = model.__dict__.items()
        user_fields = model.user.__dict__.items()

        # merge model and user field dicts
        fields = dict(model_fields + user_fields +
                      [(k, model_fields[k] + user_fields[k])
                       for k in set(model_fields) & set(user_fields)])

        for arg_name, arg_value in filter_fields.items():
            if arg_name not in fields:
                continue

            if arg_value != fields[arg_name]:
                return False

        return True

    return list(filter(filter_condition, model_manager.all()))

@python_2_unicode_compatible
class UserProfileManager(models.Manager):
    # Для фильтрации по внешнему ключу UserProfile
    #def filter(self, **filter_fields):
    #   return filter_by_foreign_fields(super(UserProfileManager, self), **filter_fields)
    
    def create_all(self, username,
               password, email,
               **kwargs):

        user = User(username=username, email=email, password=password)

        user.first_name = kwargs.get('first_name')
        user.last_name = kwargs.get('last_name')
        user.is_superuser = kwargs.get('is_superuser', False)
        user.save()
        print "hell"
        return self.create(
            user=user,
            patronymic=kwargs.get('patronymic'),
            birth_date=kwargs.get('birth_date'),
            study_group=kwargs.get('study_group'),
            github_id=kwargs.get('github_id'),
            stepic_id=kwargs.get('stepic_id'),
            role=kwargs.get('role', 's'),
            election_date=kwargs.get('election_date'),
            position=kwargs.get('position'),
            contract_date=kwargs.get('contract_date'),
            academic_degree=kwargs.get('academic_degree'),
            year_of_academic_degree=kwargs.get('year_of_academic_degree'),
            academic_status=kwargs.get('academic_status'),
            year_of_academic_status=kwargs.get('year_of_academic_status')
        )

    def create_student(self,
                       username=None,
                       email=None,
                       password=None,
                       first_name=None,
                       last_name=None,
                       birth_date=None,
                       patronymic=None,
                       study_group=None,
                       github_id=None,
                       stepic_id=None,
                       **kwargs):
      user = User(username=username, email=email, password=password)

      user.first_name = first_name
      user.last_name = last_name
      user.is_superuser = False
      user.save()
      type = "s"
      return self.create(
        user=user,
        patronymic=patronymic,
        birth_date=birth_date,
        study_group=study_group,
        github_id=github_id,
        stepic_id=stepic_id,
        type=type
      )

    def create_head_student(self,
                       username=None,
                       email=None,
                       password=None,
                       first_name=None,
                       last_name=None,
                       birth_date=None,
                       patronymic=None,
                       study_group=None,
                       github_id=None,
                       stepic_id=None,
                       **kwargs):
      user = User(username=username, email=email, password=password)
      user.first_name = first_name
      user.last_name = last_name
      user.is_superuser = False
      user.save()
      type = "h"
      return self.create(
        user=user,
        patronymic=patronymic,
        birth_date=birth_date,
        study_group=study_group,
        github_id=github_id,
        stepic_id=stepic_id,
        type=type
      )

    def create_teacher(self,
                       username=None,
                       email=None,
                       password=None,
                       first_name=None,
                       last_name=None,
                       birth_date=None,
                       patronymic=None,
                       election_date=None,
                       position=None,
                       contract_date=None,
                       academic_degree=None,
                       year_of_academic_degree=None,
                       academic_status=None,
                       year_of_academic_status=None,
                       academic_state=None,
                       github_id=None,
                       stepic_id=None,
                       **kwargs):
      user = User(username=username, email=email, password=password)
      user.first_name = first_name
      user.last_name = last_name
      user.is_superuser = False
      user.save()
      type = "t"
      return self.create(
        user=user,
        patronymic=patronymic,
        birth_date=birth_date,
        election_date=election_date,
        github_id=github_id,
        stepic_id=stepic_id,
        position=position,
        contract_date=contract_date,
        academic_degree=academic_degree,
        year_of_academic_degree=year_of_academic_degree,
        academic_status=academic_status,
        year_of_academic_status=year_of_academic_status,
        academic_state=academic_state,
        type=type
      )


    def create_from_user(self,
                         user=None,
                         position=None,
                         contract_date=None,
                         academic_degree=None,
                         year_of_academic_degree=None,
                         academic_status=None,
                         patronymic=None,
                         **params):
        return  self.create(
            user=user,
            patronymic=patronymic,
            type=type,
            position=position,
            contract_date=contract_date,
            academic_degree=academic_degree,
            year_of_academic_degree=year_of_academic_degree,
            academic_status=academic_status,
        )

    def __str__(self):
      return 'UserProfileManager'

PERSON_TYPE_CHOICES = (
    ('s', 'Студент'),
    ('h', 'Староста'),
    ('t', 'Преподаватель'),
    ('a', 'Администратор'),
)
ACADEMIC_STATUS_CHOICES  = (
  ('a','Ассистент'),
  ('s','Старший преподаватель'),
  ('d','Доцент'),
  ('p','Профессор'),
)
ACADEMIC_DEGREE_CHOICES = (
  ('n','Без степени'),
  ('t','Кандидат наук'),
  ('d','Доктор наук'),
)
ACADEMIC_STATE_CHOICES  = (
  ('a','Аспирант'),
  ('d','Докторант'),
  ('s','Соискатель'),
  ('st','Стажер'),
)
RATE_CHOICES = (
    ('1','0,25 ставки'),
    ('2','0,5 ставки'),
    ('3','0,75 ставки'),
    ('4','1 ставки'),
)

@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="Ссылка на аккаунт для авторизации",
    )

    patronymic = models.CharField(
        max_length=30,
        null=True,
        verbose_name="Отчество",
        blank=True,
    )
    birth_date = models.DateField(
        null=True,
        verbose_name="Дата рождения",
        blank=True,
    )
    study_group = models.CharField(
        max_length=5,
        null=True,
        verbose_name="Учебная группа",
        blank=True,
    )
    github_id = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Профиль github",
        blank=True,
    )
    stepic_id = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Профиль stepic",
        blank=True,
    )

    type = models.CharField(
        max_length=2,
        choices=PERSON_TYPE_CHOICES,
        default='s',
        verbose_name="Тип",
    )

    election_date = models.DateField(
        null=True,
        verbose_name="Дата текущего избрания или зачисления на преподавательскую должность",
        blank=True,
    )

    position = models.CharField(
        max_length=40,
        null=True,
        verbose_name="Должность",
        blank=True,
    )

    contract_date = models.DateField(
        null=True,
        verbose_name="Срок окончания трудового договора",
        blank=True,
    )

    academic_degree = models.CharField(
        max_length=1,
        choices=ACADEMIC_DEGREE_CHOICES,
        null=True,
        verbose_name="Ученая степень",
        blank=True,
    )

    year_of_academic_degree = models.DateField(
        null=True,
        verbose_name="Год присвоения ученой степени",
        blank=True,
    )

    academic_status = models.CharField(
        max_length=1,
        choices=ACADEMIC_STATUS_CHOICES,
        null=True,
        verbose_name="Учебное звание",
        blank=True,
    )

    year_of_academic_status = models.DateField(
        null=True,
        verbose_name="Год получения учебного звания",
        blank=True,
    )

    rate = models.CharField(
        max_length=1,
        choices=RATE_CHOICES,
        null=True,
        verbose_name="Ставка",
        blank=True,
    )

    academic_state = models.CharField(
        max_length=1,
        choices=ACADEMIC_STATE_CHOICES,
        null=True,
        verbose_name="Академическое положение",
        blank=True,
    )

    objects = UserProfileManager()

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def login(self):
        return self.user.username

    @property
    def password(self):
        return self.user.password

    @property
    def email(self):
        return self.user.email

    @property
    def FIO(self):
        first_name = last_name = patronymic = ""
        if not self.first_name == None: first_name = self.first_name
        if not self.last_name == None: last_name = self.last_name
        if not self.patronymic == None: patronymic = self.patronymic
        return last_name + ' ' + first_name + ' ' +  patronymic

    def __str__(self):
        print self.type.__str__()
        if self.type.__str__() == u'a':
            return unicode(u'Администратор ' + self.FIO)

        if self.type.__str__() == u't':
            position = u"Преподаватель"
            if not self.position is None:
                position = self.position
            return unicode(position + " " + self.FIO)

        if self.type.__str__() == u'h':
            return unicode(u"Староста группы " + self.study_group + " " + self.FIO)

        if self.type.__str__() == u's':
            group = ""
            if not self.study_group is None:
                group = u" группы " + self.study_group
            return unicode(u"Студент" + group + " " + self.FIO)

        return unicode(u'Неопознанный пользователь')

    def __unicode__(self):
        return unicode(self.user) or u''

    @staticmethod
    def get_profile_by_user_id(user_id):
        return UserProfile.objects.get(user_id=user_id)

    @staticmethod
    def get_profile_by_user(user):
      us = None
      try:
        us = UserProfile.objects.get(user_id=user.id)
      #todo возможно не лучший способ определить ошибку.
      except :
        us = UserProfile.objects.create(user=user)
      return us

    @staticmethod
    def check_teacher(user):
      try:
        us = UserProfile.objects.get(user_id=user.id)
        return us.type == 't'
      except :
          return False

    @staticmethod
    def check_student(user):
      try:
        us = UserProfile.objects.get(user_id=user.id)
        return us.type == 's' or us.type == 'h'
      except :
          return False

    @staticmethod
    def check_head_student(user):
      try:
        us = UserProfile.objects.get(user_id=user.id)
        return us.type == 'h'
      except :
          return False

    class Meta:
        db_table = 'userprofiles'
        verbose_name = u"Профиль пользователя"
        verbose_name_plural = u"Профили пользователей"

@python_2_unicode_compatible
class StudyBook(models.Model):
  name = models.CharField(
    max_length=80,
    verbose_name="Название",
  )
  type = models.CharField(
    max_length=80,
    verbose_name="Вид издания",
    null=True,
    blank=True,
  )
  volume = models.FloatField(
    verbose_name="Объем",
    null=True,
    blank=True,
  )
  vulture = models.CharField(
    max_length=80,
    verbose_name="Вид грифа",
    null=True,
    blank=True,
  )
  finishDate = models.CharField(
    max_length=80,
    verbose_name="Срок сдачи рукописи",
    null=True,
    blank=True,
  )
  def __str__(self):
    name=""
    if not self.name is None:
      name = self.name
    return unicode(u"Учебная книга " + name)
  class Meta:
    verbose_name = u"Учебная книга"
    verbose_name_plural = u"Учебные книги"

@python_2_unicode_compatible
class AcademicDiscipline(models.Model):
  name = models.CharField(
    max_length=150,
    verbose_name="Наименование дисциплины",
  )
  type = models.CharField(
    max_length=40,
    verbose_name="Вид занятия",
    null=True,
    blank=True,
  )
  characterUpdate = models.CharField(
    max_length=250,
    verbose_name="Характер обновления",
    null=True,
    blank=True,
  )

  def __str__(self):
    return unicode(u"Учебная дисциплина " + self.name)

  class Meta:
    verbose_name = u"Академическая дисциплина"
    verbose_name_plural = u"Академические дисциплины"

@python_2_unicode_compatible
class NIR(models.Model):
  name = models.CharField(
    max_length=250,
    verbose_name="Название работ",
  )
  period = models.CharField(
    null=True,
    blank=True,
    verbose_name="Период работ",
    max_length=80
  )
  role = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    verbose_name="Должность",
  )
  organisation = models.CharField(
    max_length=250,
    null=True,
    blank=True,
    verbose_name="Организация",
  )
  def __str__(self):
    name=""
    if not self.name is None:
      name = self.name
    return unicode(u"Научно-исследовательская работа " + name)

  class Meta:
    verbose_name = u"Научно-исследовательская работа"
    verbose_name_plural = u"Научно-исследовательские работы"

@python_2_unicode_compatible
class Participation(models.Model):
  name = models.CharField(
    max_length=255,
    verbose_name="Название",
  )
  date = models.CharField(
    verbose_name="Дата проведения",
    null=True,
    blank=True,
    max_length=80,
  )
  level = models.CharField(
    max_length=20,
    null=True,
    blank=True,
    verbose_name="Уровень",
  )
  report = models.CharField(
    max_length=250,
    null=True,
    blank=True,
    verbose_name="Название доклада",
  )
  def __str__(self):
    name=""
    if not self.name is None:
      name = self.name
    return unicode(u"Участие " + name)
  class Meta:
    verbose_name = u"Участие"
    verbose_name_plural = u"Участия"

@python_2_unicode_compatible
class TeacherPublication(models.Model):
  name_work = models.CharField(max_length=200, verbose_name="Наименование работ")
  type = models.CharField(max_length=200, verbose_name="Вид публикации")
  volume = models.FloatField(verbose_name="Объем")
  name_publisher = models.CharField(max_length=200, verbose_name="Наименование издательства")
  def __str__(self):
    name = ""
    if not self.name_work is None:
      name = self.name_work
    return unicode(u"Публикация преподавателя " + name)

  class Meta:
    verbose_name = u"Публикация преподавателя"
    verbose_name_plural = u"Публикации преподавателя"

@python_2_unicode_compatible
class Qualification(models.Model):
  period = models.CharField(max_length=20, verbose_name="Период")
  form_training = models.CharField(max_length=200, verbose_name="Форма повышения квалификации")
  document = models.CharField(max_length=200, verbose_name="Документ")
  def __str__(self):
    name=""
    if not self.form_training is None:
      name = self.form_training
    return unicode(u"Квалификация " + name)

  class Meta:
    verbose_name = u"Повышение квалификации"
    verbose_name_plural = u"Повышения квалификации"

@python_2_unicode_compatible
class AnotherWork(models.Model):
  work_date = models.CharField(verbose_name="Период", max_length=80)
  type_work = models.CharField(max_length=200, verbose_name="Вид работы")
  def __str__(self):
    name=""
    if not self.type_work is None:
      name = self.type_work
    return unicode(u"Дополнительная работа " + name)

  class Meta:
    verbose_name = u"Дополнительная работа"
    verbose_name_plural = u"Дополнительные работы"

# class StringListField(forms.CharField):
#   def prepare_value(self, value):
#     return ', '.join(value)
#
#   def to_python(self, value):
#     if not value:
#       return []
#     return [item.strip() for item in value.split(',')]

@python_2_unicode_compatible
class TeacherPlan(models.Model):
  person_profile = models.ForeignKey(UserProfile)
  start_year = models.SmallIntegerField("Год начала")

  study_books = ListField(EmbeddedModelField("StudyBook"))
  disciplines = ListField(EmbeddedModelField("AcademicDiscipline"))
  NIRS = ListField(EmbeddedModelField("NIR"))
  participations = ListField(EmbeddedModelField("Participation"))
  publications = ListField(EmbeddedModelField("TeacherPublication"))
  qualifications = ListField(EmbeddedModelField("Qualification"))
  anotherworks = ListField(EmbeddedModelField("AnotherWork"))

  def __str__(self):
    return unicode(self.person_profile.first_name + " " + str(self.start_year) + '-' + str(self.start_year+1))

  class Meta:
    verbose_name = u"Учебный план"
    verbose_name_plural = u"Учебные планы"
