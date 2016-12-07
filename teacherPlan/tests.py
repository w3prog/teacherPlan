#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

c = Client()


class GetPagesTest(TestCase):
  """
    Тесты на получение страниц
  """
  def test_index(self):
    response = c.get('/')
    self.assertEqual(response.status_code, 302)

  def test_planlist(self):
    response = c.get('/listOfPlans')
    self.assertEqual(response.status_code, 302)

  def test_newPlan(self):
    response = c.get('/makeNewPlan')
    self.assertEqual(response.status_code, 302)

  def test_plan(self):
    response = c.get('/plan')
    self.assertEqual(response.status_code, 302)

  def test_simpleReport(self):
    response = c.get('/managerReport')
    self.assertEqual(response.status_code, 302)