#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then


@given(u'I start decorators check')
def step_impl(context):
    print ('I start decorators check')


@when(u'I perform step for decorators')
def step_impl(context):
    print ('Decorators individual step')


@then(u'Decorators check step should be successful')
def step_impl(context):
    print ('Decorators check successful\n')


@given(u'I start decorators check case 2')
def step_impl(context):
    print ('I start decorators check case 2')


@when(u'I perform step for decorators case 2')
def step_impl(context):
    print ('Decorators individual step case 2')


@then(u'Decorators check case 2 step should be successful')
def step_impl(context):
    print ('Decorators check successful part 2\n')


@given(u'I start decorators check case 3')
def step_impl(context):
    print ('I start decorators check case 3')


@when(u'I perform step for decorators case 3')
def step_impl(context):
    print ('Decorators individual step case 3')


@then(u'Decorators check case 3 step should be successful')
def step_impl(context):
    print ('Decorators check successful part 3\n')


@given(u'I start decorators check case 4')
def step_impl(context):
    print ('I start decorators check case 4')


@when(u'I perform step for decorators case 4')
def step_impl(context):
    print ('Decorators individual step case 4')


@then(u'Decorators check case 4 step should be successful')
def step_impl(context):
    print ('Decorators check successful part 4\n')


#   cd D:\Automation_project\Python_Projects\Python_Behave_Demo\Demo3_BeforeAfterDecorators
#   behave --no-capture --no-capture-stderr
