![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)<br/>

# Caracara
![PyPI - Status](https://img.shields.io/pypi/status/caracara)
[![PyPI](https://img.shields.io/pypi/v/caracara)](https://pypi.org/project/caracara/)
[![Pylint](https://github.com/CrowdStrike/caracara/actions/workflows/pylint.yml/badge.svg)](https://github.com/CrowdStrike/caracara/actions/workflows/pylint.yml)
[![Flake8](https://github.com/CrowdStrike/caracara/actions/workflows/flake8.yml/badge.svg)](https://github.com/CrowdStrike/caracara/actions/workflows/flake8.yml)
[![Bandit](https://github.com/CrowdStrike/caracara/actions/workflows/bandit.yml/badge.svg)](https://github.com/CrowdStrike/caracara/actions/workflows/bandit.yml)
[![CodeQL](https://github.com/CrowdStrike/caracara/actions/workflows/codeql.yml/badge.svg)](https://github.com/CrowdStrike/caracara/actions/workflows/codeql.yml)
![OSS Lifecycle](https://img.shields.io/osslifecycle/CrowdStrike/caracara)

A collection of tools for interacting with the CrowdStrike Falcon API.

## Basic usage example
The following example demonstrates using the Hosts Toolbox to retrieve a host AID,
and then using the RTR Toolbox to initiate a session and execute `ifconfig`.
```python
import os
import caracara

# Open the Hosts toolbox
hosts = caracara.toolbox("hosts",
                         key=os.environ["FALCON_CLIENT_ID"],
                         secret=os.environ["FALCON_CLIENT_SECRET"],
                         verbose=True
                         )
# Open the RTR toolbox
rtr = caracara.toolbox("rtr")

# Lookup the AID for our search string
target_aid = hosts.host.find_host_aid(hostname="SEARCH-STRING")
# Retrieve the hostname
hostname = hosts.host.get_host(target_aid)[0]["hostname"]
# RTR Single Target helper
target = rtr.single_target
# Initialize a RTR session
target_session = target.connect_to_host(target_aid)
# Execute a RTR command
command_result = target.execute_command("ifconfig", target_session)
# Disconnect from the RTR session
target.disconnect_from_host(target_session)
# Output the results
print(command_result)
```

## Installation
```shell
python3 -m pip install caracara
```

## Upgrading
```shell
python3 -m pip install caracara --upgrade
```

## Removal
```shell
python3 -m pip uninstall caracara
```