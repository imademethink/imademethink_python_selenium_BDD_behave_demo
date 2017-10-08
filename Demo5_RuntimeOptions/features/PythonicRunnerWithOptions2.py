#!/usr/bin/python
# -*- coding: utf-8 -*-
from json2html import *
import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    featureFileFolder = ' feature_files_folder/feature2 '
#    tagList = ' --tags=mytag2 '  # all scenarios tagged with this tag
    tagList = ' --tags=-mytag2 '  # all scenarios except tagged with this tag
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = commonRunnerOptions + featureFileFolder + tagList
    runner_with_options.main(fullRunnerOptions)
