@web @google
Feature: Google Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # Web scenarios can be highly declarative, which focuses on behavior.
  # Don't get caught up in button names and layouts at the Gherkin level.
  # Note that these scenarios use Selenium WebDriver to do browser interactions.

  Background:
    Given the Calculator_web page is displayed

  Scenario Outline: do simple operations
    Given I enter <expression>
    When I press "=" button
    Then I get the answer <answer>
    Examples:
      | expression  | answer        |
      | 3 + 2       | 5             |
      | 3 - 2       | 1             |
      | 3 * 2       | 6             |
      | 3 / 2       | 1.5           |
      | 3 +-*/ 2    | Invalid Input |
      | hello world | Invalid Input |
  Scenario Outline: satisfy commutative property
    Given I enter <expression1>
    When I press "=" button 
    Then I get the same answer <expression2>
    Examples:
      | expression1 | expression2 |
      | 3 + 4       | 4 + 3       |
      | 2 * 5       | 5 * 2       |
  Scenario Outline: satisfy associative property
    Given I enter <expression1>
    When I press "=" button 
    Then I get the same answer <expression2>
    Examples:
      | expression1 | expression2 |
      | (2 + 3) + 4 | 2 + (3 + 4) |
      | 2 * (3 * 4) | (2 * 3) * 4 |
  Scenario Outline: satisfy distributive property
    Given I enter <expression1>
    When I press "=" button 
    Then I get the same answer <expression2>
    Examples:
      | expression1 | expression2   |
      | 2 * (1 + 3) | (2*1) + (2*3) |
      | (1 + 3) * 2 | (1*2) + (3*2) |