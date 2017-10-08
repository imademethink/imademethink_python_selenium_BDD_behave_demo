#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then


@given(u'Some precondition specific to this scenario')
def step_impl(context):
    print ('Precondition set up')


@when(u'I perform some action')
def step_impl(context):
    print ('Perform action 1')


@when(u'I perform additional action')
def step_impl(context):
    print ('Perform additional action')


@then(u'Expected results should be shown')
def step_impl(context):
    print ('Expected results are shown')


@then(u'Unwanted results should not be shown')
def step_impl(context):
    print ('Unwanted results removed\n\n\n')


@given(u'Consider mobile device with OS type as "{os_type}"')
def step_impl(context,os_type):
    print ('Considered following mobile device with OS type as ' + os_type)


@when(u'I perform mobile os specific action')
def step_impl(context):
    print ('Performed mobile OS specific action')


@then(u'Respective os specific "{preferred_browser}" browser should be launched')
def step_impl(context,preferred_browser):
    print ('Following ' + preferred_browser + ' browser is launched\n')


#  cd D:\Automation_project\Python_Projects\Python_Behave_Demo\Demo1_GettingStarted\Sample2
#  behave --no-capture --no-capture-stderr
