import ctypes
import socket
import struct

# Load iphlpapi.dll
iphlpapi = ctypes.windll.iphlpapi

# Define constants
AF_INET = 2
AF_INET6 = 23
MAX_ADAPTER_DESCRIPTION_LENGTH = 128
MAX_ADAPTER_NAME_LENGTH = 256
MAX_ADAPTER_ADDRESS_LENGTH = 8
MIB_IF_TYPE_ETHERNET = 6

# Define structures
class IP_ADDR_STRING(ctypes.Structure):
    pass

IP_ADDR_STRING._fields_ = [
    ('Next', ctypes.POINTER(IP_ADDR_STRING)),
    ('IpAddress', ctypes.c_char * 16),
    ('IpMask', ctypes.c_char * 16),
    ('Context', ctypes.c_ulong)
]

class IP_ADAPTER_INFO(ctypes.Structure):
    pass

IP_ADAPTER_INFO._fields_ = [
    ('Next', ctypes.POINTER(IP_ADAPTER_INFO)),
    ('ComboIndex', ctypes.c_ulong),
    ('AdapterName', ctypes.c_char * (MAX_ADAPTER_NAME_LENGTH + 4)),
    ('Description', ctypes.c_char * (MAX_ADAPTER_DESCRIPTION_LENGTH + 4)),
    ('AddressLength', ctypes.c_uint),
    ('Address', ctypes.c_ubyte * MAX_ADAPTER_ADDRESS_LENGTH),
    ('Index', ctypes.c_ulong),
    ('Type', ctypes.c_uint),
    ('DhcpEnabled', ctypes.c_uint),
    ('CurrentIpAddress', ctypes.POINTER(IP_ADDR_STRING)),
    ('IpAddressList', IP_ADDR_STRING),
    ('GatewayList', IP_ADDR_STRING),
    ('DhcpServer', IP_ADDR_STRING),
    ('HaveWins', ctypes.c_uint),
    ('PrimaryWinsServer', IP_ADDR_STRING),
    ('SecondaryWinsServer', IP_ADDR_STRING),
    ('LeaseObtained', ctypes.c_ulong),
    ('LeaseExpires', ctypes.c_ulong)
]

# Allocate buffer
adapter_info = (IP_ADAPTER_INFO * 16)()
buffer_size = ctypes.c_ulong(ctypes.sizeof(adapter_info))

# Get adapters information
if iphlpapi.GetAdaptersInfo(ctypes.byref(adapter_info), ctypes.byref(buffer_size)) != 0:
    raise ctypes.WinError()

# Iterate over adapters
adapter = adapter_info[0]
while adapter:
    print(f"Adapter: {adapter.Description.decode()}")
    ip_list = adapter.IpAddressList
    while True:
        ip_addr = ip_list.IpAddress.decode().split('\x00', 1)[0]
        if ip_addr:
            print(f"IP Address: {ip_addr}")
        if not ip_list.Next:
            break
        ip_list = ip_list.Next.contents
    adapter = adapter.Next.contents if adapter.Next else None
