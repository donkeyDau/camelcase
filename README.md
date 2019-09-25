=========
camelcase
=========

Python port of javascript [camelcase](https://github.com/sindresorhus/camelcase) library

Usage
=====

This library takes strings and list of strings to convert them to camelCase.
CamelCased parts of the string will be preserved.

Example usage:

.. code-block:: python
    >>> from camelcase import camelcase
    >>> camelcase('foo-Bar')
    'fooBar'
    >>> camelcase('fooBar')
    'fooBar'
    >>> camelcase(['foo', 'Bar'])
    'fooBar'

Installing
==========

You'll need Python 2.7 or Python 3.
