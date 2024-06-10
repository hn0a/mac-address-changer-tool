     import re
     import subprocess
     import optparse

     def search_mac_address(string):
         match = re.search(r'([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})', string)
         if match:
             return match.group(0)
         else:
             return None

     def get_arguments():
         parser = optparse.OptionParser()
         parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
         parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
         (options, arguments) = parser.parse_args()
         
         if not options.interface:
             parser.error("[-] Please specify an interface, use --help for more info.")
         elif not options.new_mac:
             parser.error("[-] Please specify a new MAC address, use --help for more info.")
         
         return options

     def set_new_mac(interface, new_mac_address):
         print(f"[+] Changing MAC address for {interface} to {new_mac_address}")
         subprocess.call(["sudo", "ifconfig", interface, "down"])
         subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac_address])
         subprocess.call(["sudo", "ifconfig", interface, "up"])

     def get_mac_address_from_interface(interface):
         try:
             ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
             mac_address = search_mac_address(ifconfig_result)
             if mac_address:
                 return mac_address
             else:
                 print("[-] No MAC address found in ifconfig output.")
                 return None
         except subprocess.CalledProcessError as e:
             print(f"[-] Failed to execute ifconfig: {e}")
             return None

     if __name__ == "__main__":
         options = get_arguments()
         current_mac_address = get_mac_address_from_interface(options.interface)
         if current_mac_address:
             print(f"Current MAC address for interface {options.interface} is {current_mac_address}")
         else:
             print(f"[-] Could not get the current MAC address for interface {options.interface}")
         
         set_new_mac(options.interface, options.new_mac)
         
         new_mac_address = get_mac_address_from_interface(options.interface)
         if new_mac_address == options.new_mac:
             print(f"[+] MAC address was successfully changed to {new_mac_address}.")
         else:
             print("[-] MAC address did not get changed.")
             print(f"Current MAC address is still {new_mac_address if new_mac_address else 'unknown'}")
