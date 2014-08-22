# dexy-with-lyx-examples

This is a very simple project to collect and test out some Dexy + LyX workflows.

[Dexy](http://dexy.it/) is an open source, language agnostic automated
build system and document templating + filtering system, originally
written by Dr. Ana Nelson.

[LyX](http://www.lyx.org/) is a "What You See Is What You _Mean_" (WYSIWYM)
document processor which uses LaTeX as a back end. It is basically the
highly semantic and structured answer to word processors.

Obviously the combination of the two technologies is potentially explosive!
The possibility of automating the entire

Data processing -> Analysis -> Publication Quality Document Generation

pipeline in a language and platform agnostic way has the potential to
revolutionise current scientific practice, especially in regards to
reproducibility.

However, getting started is not always easy, and the documentation is never
quite up to par. Nothing is better than a good set of worked examples. That
is the reason for this repo:

1. To teach it to myself - don't expect expert level code (yet),
2. To hopefully be useful to anyone else hoping to explore automated reproducible
documentation.

# Get going

First you need dexy, which should be as simple as

`pip install dexy`

Then clone the repo

`git clone https://github.com/mikejbrown/dexy-with-lyx-examples.git`

and `cd` into it

`cd dexy-with-lyx-examples/`

Next you need to run

`dexy setup`

in order to initialise the special `.dexy` directory. Finally you can run dexy:

`dexy`

If all goes well you should have an `output/` directory containing the final documents
in sub-directories for each example.

# Dependencies

This has currently been tested and works on Fedora 20 with dexy 1.0.14, Python 2.7.5
and LyX 2.1.1. Apart from these some of the examples may require additional libraries.
So far these are:

* [NumPy](http://www.numpy.org/) (tested version 1.8.0)
* [matplotlib](http://matplotlib.org/) (tested version 1.3.1)

but everything should be pretty portable (make an issue or a pull request if not!).

# Contribution Guide

* Each example is self-contained in its own directory (apart from the dexy.yaml - so far).
* Keep each example simple, demonstrating one or at most two related things.
* Try to avoid adding any new dependencies.
* Only one example per pull request please. Feel free to send _x_ pull requests in a row
if you have _x_ examples to share.
* The user should be able to completely build the example using only the `dexy` command
or at worst a short shell script included in the example directory.
* The build process should be completely automated, requiring no interactive input from the
user.

Enjoy! :-)
