import string
from pytest_bdd import scenarios, parsers, given, when, then
from functools import partial
from cucumbers import CucumberBasket

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}

scenarios('../features/cucumbers.feature')

#parse_num = partial (parsers.cfparse, extra_types=EXTRA_TYPES)

# @given(parse_num('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture='basket')
@given(parsers.parse('the basket has {initial} cucumbers'), converters=CONVERTERS, target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)


# @when(parse_num('"{some:Number}" cucumbers are added to the basket'))
@when(parsers.parse('{some} cucumbers are added to the basket'), converters=CONVERTERS)
def add_cucumbers(basket, some):
    basket.add(some)
    
# @when(parse_num('"{some:Number}" cucumbers are removed from the basket'))
@when(parsers.parse('{some} cucumbers are removed from the basket'), converters=CONVERTERS)
def remove_cucumbers(basket, some):
    basket.remove(some)


# @then(parse_num('the basket contains "{total:Number}" cucumbers'))
@then(parsers.parse('the basket contains {total} cucumbers'), converters=CONVERTERS)
def basket_has_total(basket, total):
    assert basket.count == total
