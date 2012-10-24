Theme Examples
======================================

This page is to serve as example of how the theme handles various pieces of documentation.


Python Code
--------------------------------------

.. code-block:: python

    import random

    if random.random() < 0.5:
        print 'You win!'
    else:
        print 'You lose.'


HTML Code
--------------------------------------

.. code-block:: html

    <form method='post' action=''>
        <input type='text' name='username'>
        <input type='password' name='passowrd'>
        <button type='submit'>Submit</button>
    </form>


Lists
--------------------------------------

Ordered Lists

1. One
2. Two
3. Three

Unurdered Lists

- Foo
- Bar
- Baz


Block Quotes
--------------------------------------

This is a quote

    Quotation, n: The act of repeating erroneously the words of another.
    
    -- Ambrose Bierce 


Notes
--------------------------------------

.. note::

    This is a note

.. warning::

    This is a warning

.. versionchanged:: 0.1

    This changed in some version

.. deprecated:: 0.1

    This was deprecated in some version

.. seealso::

    You should see some other section for more info
