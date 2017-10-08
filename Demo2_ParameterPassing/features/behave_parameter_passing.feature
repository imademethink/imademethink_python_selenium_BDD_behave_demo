Feature: Parameter passing

  Scenario: Parameter passing check
    Given I start parameter passing check
    When I pass integer 99
    When I pass float 6.44
    When I pass boolean "False"
    When I pass string "Bonjour"
