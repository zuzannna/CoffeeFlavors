# flavor wheel challenge

## Objective

Your goal is to write a library that identifies flavor categories from the [SCAA flavor wheel](http://www.scaa.org/chronicle/wp-content/uploads/2016/01/SCAA_FlavorWheel.01.18.15.jpg) in free-form coffee tasting notes. For example, given the following input:

`"An excellent cup of coffee. Notes of stone fruit, cherry and plum. Long finish with hints of milk chocolate and brown sugar."`

the library *might* return the following categories:

<pre>
[
    ["Fruity", "Other Fruit", "Cherry"],
    ["Sweet", "Brown Sugar"],
    ["Nutty/Cocoa", "Cocoa", "Chocolate"]
]
</pre>

## Guidelines

You can think of this as an automated tagging task that might be used to generate a search index of human-written tasting notes. As a result, your inputs might be messy and linguistically nuanced. For example, consider the behavior of your library given the following inputs:

* "blackberry"
* "blackberries"
* "blackbery"
* "sour"
* "sour aromatics"
* "not sweet"

The issues hinted at above are not exhaustive. You do not need to handle every possible contingency, but you should make a principled decision about the features that your library will support.

Two resources are included here to help you along:

* `scaa_flavor_wheel.json` - a JSON representation of the flavor wheel (to save you some effort in transcription)
* `tasting_notes.json` - A collection of real coffee tasting notes from around the web (more examples of inputs). Again, this is not meant to be exhaustive, but it may help you hone your intuitions or craft the design of the library. It should also provide some fodder for tests.

You may use any helper libraries that you like as long as the dependencies of your project are properly packaged (details below).

## Requirements

Your submission will be a link to the Github repository that implements your solution. At minimum we expect the following:

* Your library should define a function or method that takes a string representing tasting notes as input and returns an array of arrays representing categories as in the example above.
* Your repository should be properly structured as a package in the dominant package format of your chosen language (e.g. Ruby --> gem, Python --> egg, etc.).
* Your library should be properly tested.
* Your repository should contain a README detailing installation, usage and contribution instructions.
* Should you be invited on-site for further interviews, you should be prepared to discuss design tradeoffs in your implementation and the quality of the overall solution (with examples of successful categorizations and known failures).

Also, in order to help us improve this exercise, please keep track of how long this challenge takes you, and anything that you found unclear in its description. And, of course, if you have any questions as you work through this exercise, please do not hesitate to contact us.

## Evaluation

You will be evaluated along the following dimensions:

* Structure, clarity and quality of the code the implements the library (solution, tests, packaging, README, etc).
* Correctness of the library for the simplest use cases.
* Ability to discuss design tradeoffs in your code, and the strengths and weakenesses of your implementation.

And, for bonus points:

* Sophistication of your solution (i.e. its ability to handle more complex inputs).

The point of this exercise is not to test your NLP knowledge. Rather, it is meant to test your ability to write a complete, well-structured, and self-contained piece of code to perform a high-level task. Hence a solution that meets only the first three criteria, but that meets those criteria well, will be considered very good. One that also researches and implements a few extensions will be considered excellent.

_Good luck!_
