"""File to store configuration values in case we want to change em"""

# Due to the nature of this file, it fails to reach the threshold set for
# static analysis.

# The administrative port
admin = 2048

# The lower bound of the port range to use.
lower_bound = 2049

# The upper bound of the port range to use.
upper_bound = 3072

# Visual version number because we lazy
version_number = "0.1.0"

# Group member names for ui
names = "Charles, Nick, Idan, Brendan"

# log path
log_addr = "./server.log"

# db path
db_addr = "./testdb.csv"

# tornado debug value
debug = False

# Length of endpoint str
endpoint_length = 5

# Dictionary used for endpoint gen
dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Ports for web server configuration.
web_test = 8080
web_prod = 80

# CHARLES HELP
MAXATTEMPTS = 10
