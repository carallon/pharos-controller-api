.. code-block:: lua

   tl = get_timeline(1)
   name = tl.name
   state = tl.state

   if (tl.source_bus == TCODE_1) then
     -- do something
   end
