Feature: user login

Scenario: successful test for login
    Given I navigate to login page
    And I enter vaild <user_id> and <password>
    When I click on submit button
    Then I login in successful
    Examples:
      | user_id  |  password   |
      | stust    |  1312       |
      | 132      |  das        |
      | 123      |  123        |
      | 123      |  ###        |
      | @2/      |  123        |