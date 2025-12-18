# Network Lab Setup Plan

## Problem Statement

The current project has a Makefile in the root directory that calls `make -C netlab setup`, but the netlab directory lacks a Makefile with the required targets. This causes the `make setup` command to fail.

## Analysis

- The `netlab/topology.yml` file is configured for ContainerLab (clab)
- The topology defines two nodes: R1 (router) and S1 (switch)
- Missing Makefile in the netlab directory with appropriate targets

## Solution Components

### 1. Create Makefile for ContainerLab Operations

The Makefile should include targets for:

- `setup`: Deploy the network lab using clab deploy
- `stop`: Stop the network lab using clab destroy
- `destroy`: Alias for stop (destroy the network lab)
- `connect`: Connect to a specific host/container
- `restart`: Restart the network lab
- `status`: Check the status of the network lab
- `logs`: Show logs for containers
- `help`: Display help information

### 2. Prerequisites Verification

Before running the lab, ensure:

- ContainerLab (clab) is installed
- Docker is running
- Internet connectivity to pull required images

### 3. Implementation Steps

1. Create Makefile in netlab directory with appropriate targets
2. Ensure the topology.yml file is properly configured
3. Test all make commands to verify functionality
4. Update documentation if needed

## Proposed Makefile Content

```makefile
.PHONY: setup stop destroy help restart status

# Default variables
LAB_NAME := lab
TOPOLOGY_FILE := topology.yml

setup:
 @echo "Starting network lab..."
 clab deploy -t $(TOPOLOGY_FILE) --reconfigure

stop:
 @echo "Stopping network lab..."
 clab destroy -t $(TOPOLOGY_FILE)

destroy: stop

connect:
 @echo "Connecting to container..."
ifdef host
 clab exec -t $(TOPOLOGY_FILE) -c "$(host)" -- bash
else
 @echo "Please specify a host to connect to, e.g., make connect host=R1"
endif

restart:
 @echo "Restarting network lab..."
 clab destroy -t $(TOPOLOGY_FILE)
 clab deploy -t $(TOPOLOGY_FILE) --reconfigure

status:
 @echo "Checking network lab status..."
 clab inspect -t $(TOPOLOGY_FILE)

logs:
 @echo "Showing logs for containers..."
 clab logs -t $(TOPOLOGY_FILE)

help:
 @echo "Available commands:"
 @echo " make setup                    - Deploy the network lab"
 @echo "  make stop                     - Stop the network lab"
 @echo "  make destroy                  - Destroy the network lab (same as stop)"
 @echo "  make connect host=<host>      - Connect to a specific host (e.g., R1)"
 @echo "  make restart                  - Restart the network lab"
 @echo "  make status                   - Check the status of the network lab"
 @echo "  make logs                     - Show logs for containers"
 @echo ""
 @echo "Prerequisites:"
 @echo "  - ContainerLab (clab) must be installed"
 @echo "  - Docker must be running"
 @echo "  - Internet connection to pull required images"
```

## Dependencies

- ContainerLab (clab): <https://containerlab.dev/>
- Docker: Required for container orchestration
- Images specified in topology.yml: asifsyd/cisco_iol:17.12.01 and asifsyd/cisco_iol:l2-17.12.01

## Expected Outcome

After implementing this solution:

1. The `make setup` command from the root directory will successfully deploy the network lab
2. All related commands (stop, destroy, connect, etc.) will work as expected
3. Users can easily interact with the network lab through familiar make commands
