Feature: flask to-do list functional test

  Background: 
    Given I go to "https://flask.io/bClNDCUhkKoX" in a browser

### Scneario 1 ###
  Scenario: Check flask website online
    When Default task description "Write your next task here..." is shown
    Then Test passed

## Scenario 2 ###
  Scenario Outline: Add new todo item
    When I add new todo item "<todo-item>"
    Then the new todo item "<todo-item>" is added

    Examples: 
      | todo-item   |
      | todo-item-1 |
      | todo-item-2 |
      | todo-item-3 |

### Scenario 3 ###
  Scenario Outline: Rename todo list
    When I click the todo list name
    And I type "<todo-list-name>"
    And I hit ENTER
    Then todo list name is renamed to "<todo-list-name>"

    Examples: 
      | todo-list-name   |
      | todo-list-name-1 |
      | todo-list-name-2 |

### Scenario 4 ###
  Scenario Outline: Star an todo item
    When I click the start button on the todo item "<todo-item>"
    Then the todo item "<todo-item>" is starred

    Examples: 
      | todo-item  |
      | todo-item-1 |
      | todo-item-2 |
      # | todo-item-3 |

### Scenario 5 ###
  Scenario Outline: Delete the existing todo item
    When I click the X button on the todo item "<todo-item>"
    And I click OK in the confirmation window
    Then the "<todo-item>" todo item is deleted

    Examples: 
      | todo-item  |
      | todo-item-1 |
      | todo-item-2 |
      | todo-item-3 |



    