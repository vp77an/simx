# Copyright (c) 2014. Los Alamos National Security, LLC. 

# This material was produced under U.S. Government contract DE-AC52-06NA25396
# for Los Alamos National Laboratory (LANL), which is operated by Los Alamos 
# National Security, LLC for the U.S. Department of Energy. The U.S. Government 
# has rights to use, reproduce, and distribute this software.  

# NEITHER THE GOVERNMENT NOR LOS ALAMOS NATIONAL SECURITY, LLC MAKES ANY WARRANTY, 
# EXPRESS OR IMPLIED, OR ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  
# If software is modified to produce derivative works, such modified software should
# be clearly marked, so as not to confuse it with the version available from LANL.

# Additionally, this library is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License v 2.1 as published by the 
# Free Software Foundation. Accordingly, this library is distributed in the hope that 
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See LICENSE.txt for more details.

import simx.core as core
from simx.core.debug_stream import DebugStream as ds

#TODO: why does a resource have to be a simx entity?

#class Resource(core.PyEntity):
class Resource(object):
    """
    A resource is an object that is used by a process.
    For e.g., a computer CPU. A resource can
    be busy or idle; a busy resource is associated with exactly
    one process
    """
    # def __init__(self, id_, lp, entity_input, py_obj=None):
    #     if py_obj is None:
    #         py_obj = self
    #     super(Resource,self).__init__(id_, lp, entity_input, py_obj)
    def __init__(self):
        ds.debug2.write("Resource of type ",self.__class__.__name__,
                        " being created at time",
                        core.get_now())
        self.busy = False
        self.process = None
        self.process_queue = []
