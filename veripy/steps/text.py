import logging

from behave import then


logger = logging.getLogger('text')


@then('the page title should be "{title}"')
def check_page_title(context, title):
    """ Asserts that the browser page's current title is the given value. """
    logger.info(f'Asserting that the page title is "{title}".')
    assert context.page.browser.title == title


@then('the "{element}" contains the text "{text}"')
def check_element_text(context, element, text):
    """ Asserts that the element contains the given value as text. """
    logger.info(f'Asserting that the element "{element}" contains the text "{text}".')
    assert text in context.page[element].text


@then('the "{element}" is {not_:optional_not}visible')
def check_element_visible(context, element, not_):
    """ Asserts that the element is the visible on the page. """
    try:
        assert context.page[element].visible != not_
    except AttributeError:
        assert not_


@then('the {position:d}{ordinal:ordinal_indicator} {sub_element:w} in the "{element_name}" \
contains the text "{text}"')
def check_nth_element_text(context, position, ordinal, sub_element, element_name, text):
    """ Asserts that the nth element contains the given value as text
    ::

        the 3rd label of the "Form" contains the text "First Name"
    """
    logger.info(f'Asserting that the {position}{ordinal} "{sub_element}" \
    of the element: "{element_name}" contains the text "{text}".')
    chosen_elements = context.page.find_children(sub_element, parent=element_name)
    assert text in chosen_elements[position-1].text
