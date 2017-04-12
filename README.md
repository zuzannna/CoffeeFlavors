To do:

1. detailing installation, usage and contribution instructions.

requirements
test
tradeoffs
time spent
egg packaging

## Introduction

The goal of this library is to identify flavor categories from the SCAA flavor wheel](http://www.scaa.org/chronicle/wp-content/uploads/2016/01/SCAA_FlavorWheel.01.18.15.jpg).

![flavor_wheel](flavor_wheel.png)

## Testing

To test the code to make sure it works run the following command in your terminal shell from the <code>/CoffeeFlavors/</code>directory:

	py.test tests	

You will then see a report on the testing results.

## Validation

In order to validate my approach I manually tagged 18 review notes and compared it to the output of the <code>/coffee_flavors.py/</code>, which overalpped in 88%. Examining the errors was interesting. I noticed, for example, that *caramel* and *fruit* (but not *fruity*) was consistently missing in the output of the <code>/coffee_flavors.py/</code> while *green tea* was falsely tagged as *Green / Vegetative*. I discuss why these errors most likely occur and how to fix them in the section "Further steps".

![validation](validation.png)

To do with the actual code:
input output

testing
egg / wheel packaging 


What would I do if I had more time? [Not supported in the library]:
- spelling errors (https://github.com/mattalcock/blog/blob/master/2012/12/5/python-spell-checker.rst)
- bigrams (this includes negations and phrases such as "dark chocolate")
- tree structure for flavor_table. or one large dictionary with keys processed flavors and values of original flavors and parent. highest level flavors have parent 'None', and then have a find_label function such that it looks for a parent as long as it does not equal to None.
- synonyms / fuzzy matching (e.g. toffee / carmelized, apricot / peach)
- case of green tea (tagged as green / vegetative)
