#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then, step


@given(u'Step for simple scenario 1_1')
def step_impl(context):
    print ('Step for simple scenario 1_1 tagged with mytag1')


@given(u'Step for simple scenario 1_2')
def step_impl(context):
    print ('Step for simple scenario 1_2 tagged with mytag2')


@given(u'Step for simple scenario 1_1 and 1_2')
def step_impl(context):
    print ('Step for simple scenario 1_1 and 1_2 tagged with two tags -- mytag1 and mytag2')


@given(u'Step for simple scenario 1_4')
def step_impl(context):
    print ('Step for simple scenario 1_4 tagged with mytag4')
    assert False, ('*************************Asserting for demo purpose only')
