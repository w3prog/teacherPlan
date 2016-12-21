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
    )
    birth_date = models.DateField(
        null=True,
        verbose_name="Дата рождения",
    )
    study_group = models.CharField(
        max_length=5,
        null=True,
        verbose_name="Учебная группа",
    )
    github_id = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Профиль github",
    )
    stepic_id = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Профиль stepic",
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
    )

    position = models.CharField(
        max_length=40,
        null=True,
        verbose_name="Должность",
    )

    contract_date = models.DateField(
        null=True,
        verbose_name="Срок окончания трудового договора",
    )

    academic_degree = models.CharField(
        max_length=1,
        choices=ACADEMIC_DEGREE_CHOICES,
        null=True,
        verbose_name="Ученая степень",
    )

    year_of_academic_degree = models.DateField(
        null=True,
        verbose_name="Год присвоения ученой степени",
    )

    academic_status = models.CharField(
        max_length=1,
        choices=ACADEMIC_STATUS_CHOICES,
        null=True,
        verbose_name="Учебное звание",
    )

    year_of_academic_status = models.DateField(
        null=True,
        verbose_name="Год получения учебного звания",
    )

    academic_state = models.CharField(
        max_length=1,
        choices=ACADEMIC_STATE_CHOICES,
        null=True,
        verbose_name="Академическое положение",
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
            return str(u'Администратор ' + self.FIO)

        if self.type.__str__() == u't':
            position = u"Преподаватель"
            if not self.position is None:
                position = self.position
            return position + " " + self.FIO

        if self.type.__str__() == u'h':
            return u"Староста группы " + self.study_group + " " + self.FIO

        if self.type.__str__() == u's':
            group = ""
            if not self.study_group is None:
                group = u" группы " + self.study_group
            return u"Студент" + group + " " + self.FIO

        return u'Неопознанный пользователь'

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


class AcademicDiscipline(models.Model):
  name = models.CharField(
    max_length=150,
    verbose_name="Наименование дисциплины",
  )
  type = models.CharField(
    max_length=40,
    null=True,
    verbose_name="Вид занятия",
  )
  characterUpdate = models.CharField(
    max_length=250,
    null=True,
    verbose_name="Характер обновления",
  )

  @staticmethod
  def create(**params):
    academicDiscipline = AcademicDiscipline.objects.create(
      disc=params.get('name'),
      type=params.get('type'),
      characterUpdate=params.get('characterUpdate'),
    )
    academicDiscipline.save()

    return academicDiscipline

  def __str__(self):
    return self.teacher + " " + self.disc

class NIR(models.Model):
  user = models.ForeignKey(
    UserProfile,
    verbose_name="Сотрудник",
  )
  workName = models.CharField(
    max_length=250,
    verbose_name="Название работ",
  )
  startDate = models.DateField(
    null=True,
    verbose_name="Дата начала работ",
  )
  finishDate = models.DateField(
    null=True,
    verbose_name="Дата конца работ",
  )
  role = models.CharField(
    max_length=100,
    null=True,
    verbose_name="Должность",
  )
  organisation = models.CharField(
    max_length=250,
    null=True,
    verbose_name="Организация",
  )
  cipher = models.CharField(
    max_length="100",
    null=True,
    verbose_name = "Шифр",
  )

  @staticmethod
  def create(**params):
    nir = NIR.objects.create(
      user=params.get('user'),
      startDate=params.get('startDate'),
      finishDate = params.get('finishDate'),
      role = params.get('role'),
      organisation = params.get('organisation'),
      cipher = params.get('cipher'),
    )

    nir.save()

    return nir

  def __str__(self):
    return self.workName + " " + self.organisation + " " + self.cipher

TYPE_PUBLICATION_CHOICES = (
  ('guidelines', 'Методическое указание'),
  ('book', 'Книга'),
  ('journal', 'Статья в журнале'),
  ('compilation', 'Конспект лекции/сборник докладов'),
  ('collection ', 'Сборник трудов')
)

reIter = (
  ('disposable', 'одноразовый'),
  ('repeating', 'повторяющийся')
)

class Publication(models.Model):
  user = models.ForeignKey(
    UserProfile,
    verbose_name="Сотрудник",
    related_name='author'
  )

  name = models.CharField(
    max_length=250,
    verbose_name="Название",
  )

  

  # объем
  volume = models.IntegerField(
    verbose_name="Объем",
    null=True,
  )

  # название издательства
  publishingHouseName = models.CharField(
    max_length="100",
    null=True,
    verbose_name="Название издательства",
  )

  publicationType = models.CharField(
    max_length="20",
    choices=TYPE_PUBLICATION_CHOICES,
    default="book",
    verbose_name="Тип публикации",
  )

  # вид повторения сборника
  reiteration = models.CharField(
    choices=reIter,
    max_length="10",
    default="disposable",
    verbose_name = "Вид повторения сборника",
    )

  # номер издания
  number = models.IntegerField(
    verbose_name="Номер издания",
    null=True,
  )

  # место издания
  place = models.CharField(
    verbose_name="Место издания",
    max_length="100",
    null=True,
  )

  # дата издания
  date = models.DateField(
    verbose_name="Дата издания",
    null=True,
  )

  # единицы объема
  unitVolume = models.CharField(
    verbose_name="Единицы объёма",
    max_length="100",
  )
  # тираж
  edition = models.IntegerField(
    verbose_name="Тираж",
    null=True,
  )

  # вид методического издания / книги
  type = models.CharField(
    verbose_name="Вид",
    max_length="100",
    help_text="Поле заполняется, если тип вашей публикации" " \"Книга\" или \"Методическое указание\"",
    null=True,
  )

  # ISBN
  isbn = models.CharField(
    verbose_name="ISBN",
    max_length="100",
    help_text="Поле заполняется, если тип вашей публикации" "\"Книга\" или \"Методическое указание\"",
    null=True,
  )

  # редактор сборника
  editor = models.CharField(
    verbose_name="Редактор сборника",
    max_length="100",
    null=True,
  )

  @staticmethod
  def create(**params):
    publication = Publication.objects.create(
      name=params.get('name'),
      user=params.get('user'),
      volume=params.get('volume'),
      publishingHouseName=params.get('publishingHouseName'),
      publicationType=params.get('publicationType'),
      reiteration=params.get('reiteration'),
      number=params.get('number'),
      place=params.get('place'),
      date=params.get('date'),
      unitVolume=params.get('unitVolume'),
      edition=params.get('edition'),
      type=params.get('type'),
      isbn=params.get('isbn'),
      editor=params.get('editor'),
    )

    publication.save()

    return publication

  def __str__(self):
    return self.publicationType + ' ' + self.name + ' ' + self.isbn

EVENT_TYPE_CHOISES = (
  ('k','Конкурс'),
  ('v','Выставка'),
  ('с','Конференция'),
  ('q','Семинар'),
)

reIter = (
        ('disposable', 'одноразовый'),
        ('repeating', 'повторяющийся')
)

class ScientificEvent(models.Model):
  event_name = models.CharField(
    max_length=255,
    verbose_name="Название",
  )
  level = models.CharField(
    max_length=20,
    null=True,
    verbose_name="Уровень",
  )
  date = models.DateField(
    verbose_name="Дата проведения",
    null=True,
  )  # дата проведения
  place = models.CharField(
    verbose_name="Место проведения",
    max_length="100",
    null = True,
  )
  type = models.CharField(
    max_length=1,
    choices=EVENT_TYPE_CHOISES,
    default='c',
    verbose_name = "Тип",
  )

  def __src__(self):
    return self.event_name

  @staticmethod
  def create(**params):
    scientificEvent = ScientificEvent.objects.create(
      event_name=params.get('eventName'),
      level=params.get('level'),
      date=params.get('date'),
      place=params.get('place'),
      type=params.get('type'),
    )

    scientificEvent.save()

    return scientificEvent

  def __str__(self):
    # todo проверить корректность вывода
    return self.type + " " + self.level + " " + self.event_name

class Participation(models.Model):
  scientific_event = models.ForeignKey(
    ScientificEvent,
    verbose_name="Мероприятие",
  )
  user = models.ForeignKey(
    UserProfile,
    related_name='author_part'
  )
  title = models.CharField(
    max_length=250,
    null=True,
    verbose_name="Заголовок",
  )

  @staticmethod
  def create(**params):
    participation = Participation.objects.create(
      scientific_event=params.get('scientificEvent'),
      user=params.get('user'),
      title=params.get('title'),
    )

  def __str__(self):
    return self.user + " на " + self.scientific_event.event_name

@python_2_unicode_compatible
class Qualification(models.Model):
  ql_date = models.CharField(max_length=20, verbose_name="Период")
  for_ql = models.CharField(max_length=200, verbose_name="Форма повышения квалификации")
  doc = models.CharField(max_length=200, verbose_name="Документ")

@python_2_unicode_compatible
class AnotherWork(models.Model):
  work_date = models.CharField(verbose_name="Период", max_length=20)
  v_work = models.CharField(max_length=200, verbose_name="Вид работы")

@python_2_unicode_compatible
class TeacherPublication(models.Model):
  name_work = models.CharField(max_length=200, verbose_name="Наименование работ")
  type = models.CharField(max_length=200, verbose_name="Вид публикации")
  volume = models.IntegerField(verbose_name="Объем")
  name_publisher = models.CharField(max_length=200, verbose_name="Наименование издательства")


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

  study_books = ListField(EmbeddedModelField("Publication"))
  disciplines = ListField(EmbeddedModelField("AcademicDiscipline"))
  sw_work = ListField(EmbeddedModelField("NIR"))
  participations = ListField(EmbeddedModelField("Participation"))
  publications = ListField(EmbeddedModelField("TeacherPublication"))
  qualifications = ListField(EmbeddedModelField("Qualification"))
  anotherworks = ListField(EmbeddedModelField("AnotherWork"))

  def __src__(self):
    return self.person_profile.first_name + " " + str(self.start_year) + '-' + str(self.start_year+1)
