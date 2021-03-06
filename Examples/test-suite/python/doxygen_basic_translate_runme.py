#!/usr/bin/python

import doxygen_basic_translate
import string
import sys
import commentVerifier

commentVerifier.check(doxygen_basic_translate.function.__doc__,
  """
  Brief description.

  The comment text.

  Author: Some author

  Return: Some number

  See also: function2
  """
)
commentVerifier.check(doxygen_basic_translate.function2.__doc__,
  """
  A test of a very very very very very very very very very very very very very very very very
  very very very very very long comment string.
  """
)
commentVerifier.check(doxygen_basic_translate.function3.__doc__,
  """
  ----------------------------------------------------------------
  Overload 1:
  ----------------------------------------------------------------
  A test for overloaded functions
  This is function __one__

  ----------------------------------------------------------------
  Overload 2:
  ----------------------------------------------------------------
  A test for overloaded functions
  This is function __two__

  """
)
commentVerifier.check(doxygen_basic_translate.function4.__doc__,
  """
  A test of some mixed tag usage
  If: CONDITION {
  This _code_ fragment shows us something .
  Title: Minuses:
   -it\'s senseless
   -it\'s stupid
   -it\'s null

  Warning: This may not work as expected

  int main() { while(true); }

  }
  """
)
commentVerifier.check(doxygen_basic_translate.function5.__doc__,
  """
  This is a post comment. 
  """
)
commentVerifier.check(doxygen_basic_translate.function6.__doc__,
  """
  Test for default args
  Arguments:
    a (int) -- Some parameter, default is 42
  """
)
commentVerifier.check(doxygen_basic_translate.function7.__doc__,
  """
  Test for a parameter with difficult type
  (mostly for python)
  Arguments:
    a (Shape::superType *[10]) -- Very strange param
  """
)
