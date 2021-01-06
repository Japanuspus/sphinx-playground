r"""
my_module is a part of my_package

Docstrings must be ReST-formatted, so use `````` to enclose code (e.g. ``class Foo``). 

Links
-----
Single backtick (e.g. :any:`a_function`) will use the default_role of `any <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-any>`_,
so that single backticks will be displayed as code but link to symbol if possible.


Math
----
Math is fine, both inline (:math:`\int 2 x dx = x^2`) and 
as display form. Mark text block as raw to avoid backticks being treated as escapes.

.. math::
    :label: using_split

    x &= 2 \omega

    y &= 3

In equation :eq:`using_split`, we relied on a default ``split`` wrapper. It should be possible to use ``:unwrap`` to specify 
another wrapper, see the `v1.0 docs <https://www.sphinx-doc.org/en/1.0/ext/math.html>`_.


"""

def a_function(a: str) -> float:
    """
    Check for seveness
    """
    return 7.0 if a=="seven" else 0.0


def other_function(a: float, b:int, c: str) -> float:
    """
    This is the first line

    This is a more detailed description of other_function where
    the functionality is described in detail.
    Some of the args are detailed below.

    Args:
        c: String to be used for exception message if :math:`a^b > 10`
    """

    res=a**b
    if res>10.0:
        raise Exception(c)
    return res

