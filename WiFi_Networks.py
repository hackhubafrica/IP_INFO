import ctypes
import ctypes.wintypes as wintypes

# Define constants
WLAN_MAX_PHY_TYPE_NUMBER = 8
WLAN_AVAILABLE_NETWORK_INCLUDE_ALL_MANUAL_HIDDEN_PROFILES = 0x00000002

# Define structures
class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", ctypes.c_uint32),
        ("Data2", ctypes.c_uint16),
        ("Data3", ctypes.c_uint16),
        ("Data4", ctypes.c_byte * 8)
    ]

class WLAN_INTERFACE_INFO(ctypes.Structure):
    _fields_ = [
        ("InterfaceGuid", GUID),
        ("strInterfaceDescription", ctypes.c_wchar * 256),
        ("isState", ctypes.c_uint32),
    ]

class WLAN_INTERFACE_INFO_LIST(ctypes.Structure):
    _fields_ = [
        ("dwNumberOfItems", ctypes.c_uint32),
        ("dwIndex", ctypes.c_uint32),
        ("InterfaceInfo", WLAN_INTERFACE_INFO * 1),  # Placeholder for array of interfaces
    ]

class DOT11_SSID(ctypes.Structure):
    _fields_ = [
        ("uSSIDLength", ctypes.c_uint32),
        ("ucSSID", ctypes.c_byte * 32)
    ]

class WLAN_AVAILABLE_NETWORK(ctypes.Structure):
    _fields_ = [
        ("strProfileName", ctypes.c_wchar * 256),
        ("dot11Ssid", DOT11_SSID),
        ("dot11BssType", ctypes.c_uint32),
        ("uNumberOfBssids", ctypes.c_uint32),
        ("bNetworkConnectable", ctypes.c_bool),
        ("wlanNotConnectableReason", ctypes.c_uint32),
        ("uNumberOfPhyTypes", ctypes.c_uint32),
        ("dot11PhyTypes", ctypes.c_uint32 * WLAN_MAX_PHY_TYPE_NUMBER),
        ("bMorePhyTypes", ctypes.c_bool),
        ("wlanSignalQuality", ctypes.c_uint32),
        ("bSecurityEnabled", ctypes.c_bool),
        ("dot11DefaultAuthAlgorithm", ctypes.c_uint32),
        ("dot11DefaultCipherAlgorithm", ctypes.c_uint32),
        ("dwFlags", ctypes.c_uint32),
        ("dwReserved", ctypes.c_uint32)
    ]

class WLAN_AVAILABLE_NETWORK_LIST(ctypes.Structure):
    _fields_ = [
        ("dwNumberOfItems", ctypes.c_uint32),
        ("dwIndex", ctypes.c_uint32),
        ("Network", WLAN_AVAILABLE_NETWORK * 1)  # Placeholder for array of networks
    ]

# Load wlanapi.dll
wlanapi = ctypes.windll.wlanapi

# Open handle
client_handle = ctypes.c_void_p()
negotiated_version = ctypes.c_uint32()
ret = wlanapi.WlanOpenHandle(2, None, ctypes.byref(negotiated_version), ctypes.byref(client_handle))
if ret != 0:
    raise ctypes.WinError()

# Enumerate interfaces
iface_list_ptr = ctypes.POINTER(WLAN_INTERFACE_INFO_LIST)()
ret = wlanapi.WlanEnumInterfaces(client_handle, None, ctypes.byref(iface_list_ptr))
if ret != 0:
    raise ctypes.WinError()

iface_list = iface_list_ptr.contents
for i in range(iface_list.dwNumberOfItems):
    iface_info = iface_list.InterfaceInfo[i]
    print(f"Interface: {iface_info.strInterfaceDescription}")

    # Get available networks
    network_list_ptr = ctypes.POINTER(WLAN_AVAILABLE_NETWORK_LIST)()
    ret = wlanapi.WlanGetAvailableNetworkList(
        client_handle,
        ctypes.byref(iface_info.InterfaceGuid),
        WLAN_AVAILABLE_NETWORK_INCLUDE_ALL_MANUAL_HIDDEN_PROFILES,
        None,
        ctypes.byref(network_list_ptr)
    )
    if ret != 0:
        raise ctypes.WinError()

    network_list = network_list_ptr.contents
    for j in range(network_list.dwNumberOfItems):
        # Calculate the offset to get the correct network structure
        offset = ctypes.sizeof(WLAN_AVAILABLE_NETWORK) * j
        network = ctypes.cast(ctypes.addressof(network_list.Network) + offset, ctypes.POINTER(WLAN_AVAILABLE_NETWORK)).contents
        ssid = ctypes.string_at(network.dot11Ssid.ucSSID, network.dot11Ssid.uSSIDLength).decode('utf-8', errors='ignore')
        print(f"SSID: {ssid}, Signal Quality: {network.wlanSignalQuality}")

# Free memory
wlanapi.WlanFreeMemory(iface_list_ptr)
wlanapi.WlanFreeMemory(network_list_ptr)
wlanapi.WlanCloseHandle(client_handle, None)
