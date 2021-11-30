Log
===========

The Log class represents a depth or time referenced set of data displayed as a column in a borehole document. Logs can be added/removed/manipulated from the borehole document itself::

   import wellcad

   app = wellcad.Application()
   borehole = app.new_borehole()
   log = borehole.new_log(1) # Create a new well log

.. autoclass:: wellcad.log.Log
   :members:
   :undoc-members:
