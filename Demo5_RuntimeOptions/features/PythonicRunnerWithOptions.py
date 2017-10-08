#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    singleFeatureFilePath1 = ' feature_files_folder/behave_keywords1.feature '
    singleFeatureFilePath2 = ' feature_files_folder/behave_keywords2.feature '
    multipleFeatureFilePath = singleFeatureFilePath1 + '  ' + singleFeatureFilePath2
    featureFileFolder = ' feature_files_folder/feature2 '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
#    fullRunnerOptions = commonRunnerOptions + singleFeatureFilePath1
#    fullRunnerOptions = commonRunnerOptions + multipleFeatureFilePath
    fullRunnerOptions = commonRunnerOptions + featureFileFolder
    runner_with_options.main(fullRunnerOptions)
