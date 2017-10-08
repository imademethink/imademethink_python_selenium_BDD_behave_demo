#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    featureFilePath = ' feature_file_folder/Scenarios_tagged.feature '
    tagList = ' --tags=mytag1 '                        # any scenario tagged with this tag
#    tagList = ' --tags=-mytag2 '                       # any scenario except tagged with this tag
#    tagList = ' --tags=mytag1,mytag4 '             # mytag1 OR mytag4
#    tagList = ' --tags=mytag1 --tags=mytag4 '   # mytag1 AND mytag4
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = commonRunnerOptions + featureFilePath + tagList
    runner_with_options.main(fullRunnerOptions)
