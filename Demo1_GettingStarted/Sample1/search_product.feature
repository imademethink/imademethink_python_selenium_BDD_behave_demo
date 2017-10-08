Feature: Search product feature

Scenario: Search product using desktop website
    Given I launch browser on desktop PC
    When I search for any product
    Then Relevant search results should be shown
    