#!/usr/bin/env python3

import json
import os
from datetime import datetime

# Get VMs
cmd = os.popen('cmk list virtualmachines listall=true')
output = cmd.read()
cmd.close()
vms = json.loads(output)["virtualmachine"]

# Get virtual routers
cmd = os.popen('cmk list routers listall=true')
output = cmd.read()
cmd.close()
routers = json.loads(output)["router"]

nodes = vms + routers

print("\nState of " + str(datetime.now()) + "\nName, Hostname")
for node in nodes:
    if node["state"] == "Running":
        print(node["name"] + ", " + node["hostname"])
print("\n")
