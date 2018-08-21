import logging

from behave import when, given

from veripy import custom_types  # noqa

from veripy.pages import Page


logger = logging.getLogger('navigation')


@given('that the browser is at "{name}"')
def given_browser_is_at(context, name):
    """ Tells the browser to load a specific page designated by an identifer.
    ::

        Given that the browser is at "google.com"

    In order to interact with a page, you must first perform this check. This
    statement sets the page context so that later steps can refer to the page
    by it's predefined identifiers.
    """
    logger.info(f'Navigating to page named "{name}"')
    context.page = Page(name, context.browser)
    context.page.browser.visit(context.page.url)


@given('the browser window is {width:d} by {height:d} pixels')
def given_resize_window(context, width, height):
    """ Tells the browser to resize the viewport.
    ::

        Given the browser window is 500 by 1000 pixels

    Resizing the browser viewport will be important for testing the web applciation
    in various device screen sizes such as desktop, phone, tablet, etc.
    """
    logger.info(f'Resizing the browser window to {width}x{height}')
    # Splinter does not support window resize, so we must do it via driver instead
    # https://stackoverflow.com/a/21062539/148781
    context.page.browser.driver.set_window_size(width, height)


@given('the user waits {seconds:d} seconds for the "{element_name}" to be visible')
@when('the user waits {seconds:d} seconds for the "{element_name}" to be visible')
def when_wait_for_element(context, seconds, element_name):
    """ Wait for a given element on the page to become visible.
    ::

        When the user waits 10 seconds for the "Search Field" to be visible
    """
    logger.info(f'Waiting {seconds} for "{element_name}" to be visible.')
    context.page.wait_for(element_name, wait_time=seconds)


@when('the user presses the "{keyboard_key:pressable_key_type}" key')
def when_press_key(context, keyboard_key):
    """ Press the given key.
    ::

        the user presses the "Return" key
    """
    logger.info(f'Pressing the "{keyboard_key}" key.')
    active_web_element = context.browser.driver.switch_to.active_element
    active_web_element.send_keys(keyboard_key)


@given('the user waits {seconds:d} seconds')
@when('the user waits {seconds:d} seconds')
def when_wait(context, seconds):
    """ Wait for a given element on the page to become visible.
    ::

        When the user waits 10 seconds for the "Search Field" to be visible
    """
    logger.info(f'Waiting {seconds}')
    context.page.wait_for('body', wait_time=seconds)


@given('the user clicks on the {position:d}{ordinal:ordinal_indicator} {sub_element:w} \
in the "{element_name}"')
@when('the user clicks on the {position:d}{ordinal:ordinal_indicator} {sub_element:w} \
in the "{element_name}"')
def when_click_nth_element(context, position, ordinal, sub_element, element_name):
    """ Tells the browser to click on the nth element within the element of the given identifier.
    ::

        When the user clicks 2nd Entry the "Table"
    """
    logger.info(f'Clicking on {position}{ordinal} "{sub_element}" \
    of the element: "{element_name}".')
    chosen_elements = context.page.find_children(sub_element, parent=element_name)
    chosen_elements[position-1].click()
