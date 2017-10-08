#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from json2html import *
import sys
from behave import __main__ as runner_with_options
import shutil

if __name__ == '__main__':
    sys.stdout.flush()
    reporting_folder_name = 'reporting_folder_json_html'
    #
    # remove if any reporting folder exists
    shutil.rmtree(reporting_folder_name, ignore_errors=True)
    #
    # allure reporting related command line arguments
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o ' + reporting_folder_name + '  '
    #
    # run Behave + BDD + Python code
    featureFilePath = ' feature_file_folder/Scenarios_tagged.feature '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + reportingRelated + commonRunnerOptions
    runner_with_options.main(fullRunnerOptions)
    #
    # read resultant json file
    listOfJson = glob.glob(reporting_folder_name + "/*.json")
    finalJson = ''
    for cnt in range(0, len(listOfJson)):
        listOfJson[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJson[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJson)):
            listOfJson[cnt] = listOfJson[cnt] + ','
        finalJson = finalJson + listOfJson[cnt]
    finalJson = '[ ' + finalJson + ' ]'
    #
    # convert json to html using simple utility and publish report
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(reporting_folder_name + '/' + 'index.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()
