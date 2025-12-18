# Network Lab Setup Guide

## Overview

This guide explains how to set up and use the ContainerLab-based network automation lab.

## Prerequisites

- ContainerLab (clab) installed
- Docker running
- Internet connection to pull required images

## Topology

The network lab consists of:

- Router R1 (Cisco IOL)
- Switch S1 (Cisco IOL in L2 mode)
- Connection between R1 and S1 via eth1 interfaces

## Available Commands

### Setup the Network Lab

```bash
make setup
```

Deploys the network lab with the defined topology.

### Check Status

```bash
make status
```

Shows the status of all nodes in the network lab.

### Stop the Network Lab

```bash
make stop
```

Stops all containers in the network lab.

### Destroy the Network Lab

```bash
make destroy
```

Completely removes the network lab containers and associated resources.

### Restart the Network Lab

```bash
make restart
```

Stops and then redeploys the network lab.

### Connect to a Node

```bash
make connect host=R1
```

Connects to a specific node in the network lab (replace R1 with the desired node name).

### View Logs

```bash
make logs
```

Shows logs for all containers in the network lab.

### Help

```bash
make help
```

Displays help information about available commands.

## Troubleshooting

### Network Subnet Conflicts

If you encounter subnet conflicts, the lab is configured to use:

- IPv4 subnet: 172.30.30.0/24
- IPv6 subnet: 3fff:172:30:30::/64

### Image Pull Issues

If images fail to pull, ensure you have internet connectivity and the correct image names in `netlab/topology.yml`.

## Topology Configuration

The topology is defined in `netlab/topology.yml` and can be modified as needed for different scenarios.
