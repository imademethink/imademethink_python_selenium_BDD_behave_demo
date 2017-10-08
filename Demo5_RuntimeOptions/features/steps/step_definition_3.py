#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then, step


@given(u'I login to update user details')
def step_impl(context):
    print ('feature 2 specific - I login to update user details')


@when(u'I update following user detail "{item_name}" and "{item_detail}"')
def step_impl(context,item_name,item_detail):
    print ('feature 2 specific - Following user details are being updated')
    for row in context.table:
        context.temp_item_name = row['item_name']
        context.temp_item_detail = row['item_detail']
        print ('======  ' + context.temp_item_name + '  '+ context.temp_item_detail)


@then(u'User detail update should be successful')
def step_impl(context):
    print ('feature 2 specific - User details are updated successfully')
