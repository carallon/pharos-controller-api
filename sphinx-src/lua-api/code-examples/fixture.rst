.. code-block:: lua

   -- get a list of all offline fixtures
   local offlineFixtures = get_fixtures(STATUS_OFFLINE)
   log('Offline fixtures in project:')
   for _, fixtureNum in pairs(offlineFixtures) do
      -- get details of fixture
      local fixture = get_fixture(fixtureNum)
      log('- Number: ' .. fixtureNum)
      log('- Name: ' .. fixture.name)
      if (fixture.protocol == PROTOCOL_DMX) then
         log('- Protocol: ' .. DMX)
      elseif (fixture.protocol == PROTOCOL_DALI ) then
         log('- Protocol: ' .. DALI)
      end
      log('- Last updated: ' .. tostring(fixture.updated_at))
   end
