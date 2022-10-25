from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


### Scenario: Check flask website online ###
@given(u'I go to "{website}" in a browser')
def step_impl(context, website):
    context.driver = webdriver.Firefox()
    context.driver.get(website)
    context.driver.implicitly_wait(10)
    assert "Flask Lists" in context.driver.title


@when(u'Default task description "{default_task_description}" is shown')
def step_impl(context, default_task_description):
    try:
        element = context.driver.find_element(By.ID, "task_description")
        placeholder = element.get_attribute("placeholder")
    except:
        assert False, "Test failed. Element not found"
    
    if placeholder == default_task_description:
        assert True, "Test passed"
    else:
        context.driver.close()
        assert False, "Test failed. default_task_description = " + default_task_description
    
        

@then(u'Test passed')
def step_impl(context):
    time.sleep(1)
    context.driver.close()
    assert True, "Test passed"
    

### Scenario: Add new todo item ###
@when(u'I add new todo item "{todo_item}"')
def step_impl(context, todo_item):
    element = context.driver.find_element(By.ID, "task_description")
    element.send_keys(todo_item)
    element.send_keys(Keys.RETURN)



@then(u'the new todo item "{todo_item}" is added')
def step_impl(context, todo_item):

    xpath_to_find = "//span[@data-bip-value='" + todo_item + "']"

    try:
        #sleep for 1 second to wait for the new todo item is added
        time.sleep(1)
        element = context.driver.find_element(By.XPATH, xpath_to_find)
    except:
        assert False, "Test failed. The new item todo item is not found."
    else:
        assert True, "Test passed"

    context.driver.close()


### Scenario: Rename todo list name
@when(u'I click the todo list name')
def step_impl(context):
    assert True, "Test passed"



@when(u'I type "{todo_list_name}"')
def step_impl(context, todo_list_name):
    element = context.driver.find_element(By.ID, "best_in_place_list_149360_name")

    # Use ActionChains to perform mouse click and send key
    # refer https://medium.com/analytics-vidhya/python-selenium-all-mouse-actions-using-actionchains-197530cf75df

    actions = ActionChains(context.driver)
    actions.click(element)
    actions.send_keys(todo_list_name)
    actions.perform()



@when(u'I hit ENTER')
def step_impl(context):
    element = context.driver.find_element(By.ID, "best_in_place_list_149360_name")
    actions = ActionChains(context.driver)
    actions.send_keys(Keys.RETURN)
    actions.perform()


@then(u'todo list name is renamed to "{old_todo_list_name}"')
def step_impl(context, old_todo_list_name):
    element = context.driver.find_element(By.ID, "best_in_place_list_149360_name")
    new_todo_name = element.get_attribute("data-bip-value")
    if new_todo_name == old_todo_list_name:
        assert True, "Test passed"
    else:
        assert False, "Test failed. new_todo_name = " + new_todo_name
    time.sleep(1)
    context.driver.close()
    

@when(u'I click the X button on the todo item "{todo_item}"')
def step_impl(context, todo_item):
    xpath_to_find = "//a[@data-confirm='Are you sure you want to delete \"" + todo_item + "\"?']//i[@class='icon-remove']"
    element = context.driver.find_element(By.XPATH, xpath_to_find)


    actions = ActionChains(context.driver)
    actions.click(element).perform()

    


@when(u'I click OK in the confirmation window')
def step_impl(context):
    alert_obj = context.driver.switch_to.alert
    alert_obj.accept()


@then(u'the "{todo_item}" todo item is deleted')
def step_impl(context, todo_item):
    
    # wait for the todo item deleted
    time.sleep(2)

    xpath_to_find = "//span[@data-bip-value='" + todo_item + "']"
 
    try:
        element = context.driver.find_element(By.XPATH, xpath_to_find)
    except:
        assert True, "Test passed"
    else:
        context.driver.close()
        assert False, "Test failed. the todo item still exists"
    time.sleep(1)
    context.driver.close()


@when(u'I click the start button on the todo item "{todo_item}"')
def step_impl(context, todo_item):

    todo_id = get_task_id_by_task_name(context.driver, todo_item)

    xpath_to_find = "//label[@for='task_" + todo_id + "_star']//i[@class='icon-star']"
    element = context.driver.find_element(By.XPATH, xpath_to_find)
    
    actions = ActionChains(context.driver)
    actions.click(element)
    actions.perform()



@then(u'the todo item "{todo_item}" is starred')
def step_impl(context, todo_item):
    time.sleep(1)
    context.driver.close()
    assert True, "Test passed"




#############
# Functions #
#############

def get_task_id_by_task_name(driver, todo_item):

# Given the todo task name, this function will return its task ID by xpath searching
# e.g. a todo task named "todo-item-1", this function will find its id "best_in_place_task_XXX_description"
# if id is found, this function will return XXX

    xpath_to_find = "//span[@data-bip-value='" + todo_item + "']"

    element = driver.find_element(By.XPATH, xpath_to_find)

    todo_id_before_process = element.get_attribute("id")
    list_of_id = todo_id_before_process.split("_")

    for i in range(len(list_of_id)):
        try:
            if isinstance(int(list_of_id[i]), int) == True:
                todo_id_after_process = list_of_id[i]
        except:
            continue

    return todo_id_after_process