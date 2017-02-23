.. image:: https://travis-ci.org/gengo/gengo-python.svg?branch=master
    :target: https://travis-ci.org/gengo/gengo-python

Post Jobs with Gengo Python Library (for the `Gengo API <http://gengo.com/api/>`_)
===================================================================
A sample code to post translation jobs in Gengo using their API


Post Job / Tests - Running Them, etc
-------------------------

Run a single test:

::

   python -m unittest -v tests.testPostJobs.NowTestJobPost

Posting Job Posts in Gengo Sandbox is pretty simple, find + view/edit PostJobs.py file to see the magic and how it works. Or if you want a quick result, simply run:

::

   python PostJobs.py


All function definitions can be found inside gengo/mockdb.py as a dictionary: the key of the dictionary entry is the function name, and the parameters
are exactly the same as specified in the `Gengo API docs <http://developers.gengo.com>`_.
