Feature: Demo3 for various keywords used in Behave

 Scenario: Update user detail
    Given I login to update user details via mobile site
    When I update following user detail "<item_name>" and "<item_detail>" via mobile site
          | item_name| item_detail                |
          | address     | Dragon street  Brazil |
          | contact      | 001 85208520 00      |
          | name         | Uncle scrooge           |
          | surname    | Mcduck                     |
     Then User detail update should be successful via mobile site
