#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then
import os
import sys


@given(u'I launch browser on desktop PC')
def step_impl(context):
    print ('Desktop browser is launched')


@when(u'I search for any product')
def step_impl(context):
    print ('Backend system still searching for your product')


@then(u'Relevant search results should be shown')
def step_impl(context):
    print ('Here are search results you are looking for')


#  cd D:\Automation_project\Python_Projects\Python_Behave_Demo\Demo1_GettingStarted\Sample1
#  behave
#  behave --no-capture --no-capture-stderr
