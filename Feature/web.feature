@web @google
Feature: Google Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # Web scenarios can be highly declarative, which focuses on behavior.
  # Don't get caught up in button names and layouts at the Gherkin level.
  # Note that these scenarios use Selenium WebDriver to do browser interactions.

  Background:
    Given the Google home page is displayed

  Scenario: Basic Google Search
    When the user searches for "stust"
    Then results are shown for "stust"

  Scenario: Lengthy Google Search
    When the user searches for "When in the Course of human events"
    Then one of the results contains "When in the Course of Human Events"