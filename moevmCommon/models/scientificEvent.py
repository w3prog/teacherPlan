#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models.userProfile import UserProfile

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
    verbose_name="Пользователь",
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