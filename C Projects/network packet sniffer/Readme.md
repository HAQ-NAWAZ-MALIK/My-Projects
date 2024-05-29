
# Network Packet Sniffer in C

This project provides a basic implementation of a network packet sniffer in the C programming language using the `libpcap` library. The packet sniffer captures and displays information about TCP packets, including the source and destination MAC addresses, IP addresses, and TCP ports.

## Description

The provided code opens a specified network interface for packet capturing, sets a Berkeley Packet Filter (BPF) to capture only TCP packets, and then starts capturing packets. For each captured packet, the code extracts and prints information about the Ethernet, IP, and TCP headers.

## Prerequisites

To compile and run this packet sniffer, you need to have the `libpcap` library installed on your system. On Linux distributions, you can install it using your package manager (e.g., `apt-get install libpcap-dev` on Ubuntu). On macOS, you can install it using Homebrew (e.g., `brew install libpcap`).

## Compilation

To compile the packet sniffer code, follow these steps:

1. Open a terminal and navigate to the directory containing the `packet_sniffer.c` file.
2. Compile the code using a C compiler (e.g., `gcc`) and link against the `libpcap` library:

```
gcc -o packet_sniffer packet_sniffer.c -lpcap
```

If you encounter an error like "`#include <pcap.h>` not found", you may need to provide the include path for `libpcap` using the `-I` flag:

```
gcc -o packet_sniffer packet_sniffer.c -lpcap -I/path/to/libpcap/include
```

Replace `/path/to/libpcap/include` with the actual path where the `pcap.h` file is located on your system.

## Usage

To run the packet sniffer, follow these steps:

1. Open a terminal and navigate to the directory containing the compiled `packet_sniffer` executable.
2. Run the executable with root privileges (or with the appropriate permissions to access the network interface):

```
sudo ./packet_sniffer
```

The packet sniffer will start capturing TCP packets on the `en0` network interface (you may need to modify the code if your interface has a different name).

The output will display information about the captured TCP packets, including the source and destination MAC addresses, IP addresses, and TCP ports.

## Limitations

This implementation is a basic packet sniffer and doesn't include advanced features like packet filtering, payload inspection, or packet capture file handling. Additionally, running a packet sniffer may require elevated privileges or additional configuration depending on your system's security settings.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
