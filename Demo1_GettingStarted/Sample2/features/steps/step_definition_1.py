#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then


@given(u'Start web server')
def step_impl(context):
    print ('background - Web browser started')


@given(u'Connect required database')
def step_impl(context):
    print ('background - Connected to required database')


@given(u'Launch web application')
def step_impl(context):
    print ('background - Web application launched')


@given(u'Launch browser')
def step_impl(context):
    print ('Browser launched')


@when(u'I register with valid credentials')
def step_impl(context):
    print ('Registration completed with valid credential')


@then(u'User registration should be successful')
def step_impl(context):
    print ('User registration is successful\n\n')


@when(u'I login with valid credentials')
def step_impl(context):
    print ('Login attempted with valid credentials')


@then(u'Login should be successful')
def step_impl(context):
    print ('Login is successful\n\n')

#  cd D:\Automation_project\Python_Projects\Python_Behave_Demo\Demo1_GettingStarted\Sample2
#  behave --no-capture --no-capture-stderr