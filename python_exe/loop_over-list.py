### =======================================
"""Looping over lists in Python"""
### =======================================

# define the network part of our IP Add
network_part = "192.168.2."
# define the host part for each device as list
host_parts = [20, 40, 60]
# Now, we can use a for loop to iterate and combine the two parts
for host in host_parts:
    ip = network_part + str(host)  # convert host into integer
    print("The router IP is: " + ip)

# for loop using range() & len() function
network_part = "10.20.30."
host_parts = [40, 50, 60]
for i in range(len(host_parts)):
    ip = network_part + str(i)
    print("The IP of device is: " + ip)
