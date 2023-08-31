test = {
  'name': 'Question 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hog_gcd(15, 25)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(13, 17)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(0, 5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(12, 64)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(29, 79)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(39, 627)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(39)
          39
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(61)
          61
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(50)
          60
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(100)
          100
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(25)
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(75)
          79
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(80)
          84
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 5, 7, make_test_dice(2, 4))
          11
          >>> fuzzy_update(2, 5, 7, make_test_dice(2, 4)) # is 11 a fuzzy number?
          11
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(0, 14, 27) # what happens when you roll 0 dice?
          20
          >>> fuzzy_update(0, 14, 27) # is 20 a fuzzy number?
          24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 2, 3, make_test_dice(4))
          10
          >>> fuzzy_update(2, 2, 3, make_test_dice(4)) # is 10 a fuzzy number?
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(3, 11, 12, make_test_dice(4, 5, 6))
          26
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(2, 29, 17, make_test_dice(1, 3))
          30
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(0, 41, 42)
          60
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(2, 56, 56, make_test_dice(4))
          64
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> 'gcd' in dir() # do NOT import any new modules!
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> import types
          >>> def imports():
          ...     for name, val in globals().items():
          ...         if isinstance(val, types.ModuleType):
          ...             yield val.__name__
          >>> list(imports()) # do NOT import any new modules!
          ['tests.construct_check', 'types']
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> test.check('hog.py', 'hog_gcd', ['Import', 'ImportFrom']) # do NOT import any new modules!
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
