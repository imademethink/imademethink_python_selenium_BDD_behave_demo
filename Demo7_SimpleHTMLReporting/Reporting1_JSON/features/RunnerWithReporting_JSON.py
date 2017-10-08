#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    featureFilePath = ' feature_file_folder/Scenarios_tagged.feature '
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o reporting_folder_json '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + reportingRelated +  commonRunnerOptions
    runner_with_options.main(fullRunnerOptions)
