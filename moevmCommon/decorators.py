#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test

from moevmCommon.models import UserProfile

REDIRECT_FIELD_NAME = 'next'

def login_teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
  """
  Decorator for views that checks that the user is logged in, redirecting
  to the log-in page if necessary.
  """

  actual_decorator = user_passes_test(
    lambda u: u.is_authenticated() and (UserProfile.check_teacher(u) or u.is_superuser),
    login_url=login_url,
    redirect_field_name=redirect_field_name
  )
  if function:
    return actual_decorator(function)
  return actual_decorator