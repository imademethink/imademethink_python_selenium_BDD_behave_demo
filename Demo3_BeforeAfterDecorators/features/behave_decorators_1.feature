Feature: Decorators feature 1

  @tag1
  Scenario: Decorators check case 1
    Given I start decorators check
    When I perform step for decorators
     Then Decorators check step should be successful

  Scenario: Decorators check case 2
    Given I start decorators check case 2
    When I perform step for decorators case 2
     Then Decorators check case 2 step should be successful
