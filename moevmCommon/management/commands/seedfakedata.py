#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from django.core.management import BaseCommand
from moevmCommon.models.userProfile import *
from moevmCommon.models.academicDiscipline import *
from moevmCommon.models.nir import *
from moevmCommon.models.publication import *
from moevmCommon.models.scientificEvent import *
from django.contrib.auth.models import User
from faker import Factory
from optparse import make_option

class Command(BaseCommand):
  """
  Данная команда необходима чтобы наполнить базу новыми данными.
  """

  option_list = BaseCommand.option_list + (
    make_option('-n',
                '--numbers',
                dest="num",
                type="int",
                default=10,
                help='number of the fake data count'),
  )

  def handle(self, *args, **options):
    """
    Данная процедура создает новые данные в базу
    :param args:
    :param options:
    :return:
    """
    faker = Factory.create('ru-ru')
    engfaker = Factory.create('en-us')
    #todo реализовать процедуру.
    numbers =options['num']

    for i in range(1,numbers+1):
      fnametmp = faker.first_name()
      lnametmp = faker.last_name()
      usernametmp = engfaker.word()
      passwordtmp = faker.password()
      emailtmp = engfaker.email()

      user = User.objects.create(
        first_name = fnametmp,
        last_name = lnametmp,
        email = emailtmp,
        username = usernametmp,
        is_active=random.choice([True, False]),
        is_staff=random.choice([True, False]),
      )

      userProfile = UserProfile.objects.create_from_user(
        user=user,
        position=faker.word(),
        contract_date=faker.date(),
        academic_degree=random.choice(['n', 't','d']),
        year_of_academic_degree=faker.date(),
        academic_status=random.choice(['a', 's','p','d']),
        patronymic=faker.word(),
      )


      for j in range(5):
        NIRn = NIR.create(
          user=userProfile,
          startDate=faker.date(),
          finishDate=faker.date(),
          role=faker.word(),
          organisation=faker.company(),
          cipher=faker.word()
        )

      ad = AcademicDiscipline.create(
        name=faker.word()
      )

      AcademicDisciplineOfTeacher.create(
        teacher=userProfile,
        disc=ad,
      )

      for j in range(10):
        Publication.create(
          name=faker.word(),
          user=userProfile,
          volume=random.randint(0,250),
          publishingHouseName=faker.word(),
          publicationType=random.choice(['guidelines', 'book','journal','compilation','collection']),
          reiteration=random.choice(['disposable', 'repeating']),
          number=random.randint(0,10),
          place=faker.word(),
          date=faker.date(),
          unitVolume=faker.word(),
          edition=random.randint(0,10),
          type=faker.word(),
          isbn=faker.word(),
          editor=faker.name(),
        )

      for j in range(5):
        sv = ScientificEvent.create(
          eventName=faker.word(),
          level=faker.word(),
          date=faker.date(),
          place=faker.word(),
          type=random.choice(['k', 'v','c','q']),
        )
        Participation.create(
          scientificEvent=sv,
          user=userProfile,
          title=faker.word()
        )





    print("Случайные данные добавлены в базу данных")