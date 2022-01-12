Log
===========

The Log class represents a depth or time referenced set of data displayed as a column in a borehole document. Logs can be added/removed/manipulated from the borehole document itself::

   import wellcad.com

   app = wellcad.com.Application()
   borehole = app.new_borehole()
   log = borehole.insert_new_log(1) # Create a new well log

.. autoclass:: wellcad.com.Log
   :members:
   :undoc-members:
