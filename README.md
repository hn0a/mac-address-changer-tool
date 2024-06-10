# MAC Address Changer

## Overview

The MAC Address Changer is a Python script designed to change the MAC address of a specified network interface on Linux systems. This can be useful for privacy, security testing, or network troubleshooting.

## Prerequisites

- Python 3.x
- Root or superuser privileges
- `ifconfig` utility installed

## Installation

1. Clone this repository

2. Ensure you have the necessary permissions to run the script:

    ```sh
    chmod +x mac_changer.py
    ```

## Usage

Run the script with `sudo` to ensure you have the necessary permissions to change the MAC address:

```sh
sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
```

### Arguments

- `-i` or `--interface`: The network interface whose MAC address you want to change (e.g., `eth0`, `wlan0`).
- `-m` or `--mac`: The new MAC address you want to assign to the interface (e.g., `00:11:22:33:44:55`).

### Example

```sh
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

### Help

For more information and help on using the script, you can use the `-h` or `--help` flag:

```sh
python3 mac_changer.py -h
```

### Output

The script will display the current MAC address of the specified interface, change it to the new MAC address provided, and then verify if the change was successful.

## Troubleshooting

- Ensure you have `ifconfig` installed. You can install it using:

    ```sh
    sudo apt-get install net-tools
    ```
- Ensure you run the script with `sudo` or as a root user to have the necessary permissions to change the MAC address.


That's it! You are now ready to use the MAC Address Changer script.

