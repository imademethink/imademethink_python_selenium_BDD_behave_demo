Feature: Demo2 for various keywords used in Behave

 Scenario: Normal test case stages with And But keywords
    Given Some precondition specific to this scenario
     When I perform some action
      And I perform additional action
     Then Expected results should be shown
      But Unwanted results should not be shown

 Scenario Outline: Search product using mobile system with Examples
    Given Consider mobile device with OS type as "<os_type>"
     When I perform mobile os specific action
     Then Respective os specific "<preferred_browser>" browser should be launched

   Examples:
   | os_type | preferred_browser    |
   | android | chrome                  |
   | ios        | safari                     |
   | windows | internet_explorer |
