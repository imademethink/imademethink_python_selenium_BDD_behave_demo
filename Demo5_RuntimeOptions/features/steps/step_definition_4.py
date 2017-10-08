#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then, step


@given(u'I login to update user details via mobile site')
def step_impl(context):
    print ('feature 1 specific - I login to update user details')


@when(u'I update following user detail "{item_name}" and "{item_detail}" via mobile site')
def step_impl(context,item_name,item_detail):
    print ('feature 1 specific - Following user details are being updated via mobile site')
    for row in context.table:
        context.temp_item_name = row['item_name']
        context.temp_item_detail = row['item_detail']
        print ('======  ' + context.temp_item_name + '  '+ context.temp_item_detail)


@then(u'User detail update should be successful via mobile site')
def step_impl(context):
    print ('feature 1 specific - User details are updated successfully via mobile site')


@given(u'Step for simple scenario 2_1')
def step_impl(context):
    print ('Step for simple scenario 2_1')


@given(u'Step for simple scenario 2_2')
def step_impl(context):
    print ('Step for simple scenario 2_2')


@given(u'Step for simple scenario 2_3')
def step_impl(context):
    print ('Step for simple scenario 2_3')
