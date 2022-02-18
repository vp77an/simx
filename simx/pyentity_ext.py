# Copyright (c) 2013 Los Alamos National Security, LLC. 

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

#import simx
#import simx.core as core
import core
#import core_ext
import core.DebugStream as ds

"""

Extensions to the PyEntity class

"""


def install_service(self, service, address,
                    profile = None,
                    data = None
                    ):
    
    """
    
    A method of PyEntity. Installs the service at the given address
    with the given profile(optional) and data(optional) on this
    this entity. 
   
    """
    if not isinstance(self, core.PyEntity):
        ds.error.write("Argument ",self," not of type PyEntity")
        raise TypeError("install_service: Instance must be of type PyEntity")
    
    service = core.add_service(service.__name__, 
                               profile, data)
    
    ei = core.EntityInput()
    ei.load_services({address:service})
    self.create_services(ei)
    

core.PyEntity.install_service = install_service

