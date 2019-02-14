# Readme
Supply the main function with a list of ports. Response is a list of dictionaries.
## Example
Input:

`port_lookup([80, 443])`

Response (trimmed):
```
[{'port': '80',
  'port_info': [{'Details': 'Hypertext Transfer Protocol (HTTP) (official)',
                 'Port(s)': '80',
                 'Protocol': 'tcp',
                 'Service': None,
                 'Source': 'Wikipedia'},
                {'Details': 'World Wide Web HTTP',
                 'Port(s)': '80',
                 'Protocol': 'tcp,udp',
                 'Service': 'www',
                 'Source': 'SANS'}]},
 {'port': '443',
  'port_info': [{'Details': 'Port used by Google talk. Games that use this '
                            'port: Final Fantasy XI',
                 'Port(s)': '443',
                 'Protocol': 'udp',
                 'Service': 'games',
                 'Source': 'SG'},
                {'Details': 'Hypertext Transfer Protocol over TLS/SSL (HTTPS) '
                            '(official)',
                 'Port(s)': '443',
                 'Protocol': 'tcp,udp',
                 'Service': None,
                 'Source': 'Wikipedia'}]}]
```
