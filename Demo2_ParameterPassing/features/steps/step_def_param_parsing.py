#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then


@given(u'I start parameter passing check')
def step_impl(context):
    print ('===Parameter passing check begins')


@when(u'I pass integer {sample_integer:d}')
def step_impl(context,sample_integer):
    print ('===Integer parsing successful : ' + str(sample_integer))


@when(u'I pass float {sample_float:f}')
def step_impl(context,sample_float):
    print ('===Float parsing successful : ' + str(sample_float))


@when(u'I pass boolean "{sample_boolean}"')
def step_impl(context,sample_boolean):
    print ('===Boolean parsing successful : ' + str(bool(sample_boolean)))


@when(u'I pass string "{sample_string}"')
def step_impl(context,sample_string):
    print ('===String parsing successful : ' + sample_string)


#   cd D:\Automation_project\Python_Projects\Python_Behave_Demo\Demo2_ParameterPassing
#   behave --no-capture --no-capture-stderr