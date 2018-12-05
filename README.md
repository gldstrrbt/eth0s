# eth[0]s
A Python script for converting collected MAC addresses into values to be used in Blender. 

The MAC addresses used for this project were gathered using a Raspberry Pi fitted with an Alfa wireless card set to monitor mode, Tshark software, a power bank, and a miniature touch screen. 

Each collected MAC address has been added to a JSON file. A function within the Python script is used to parse the JSON file and convert the MAC addresses from hexadecimal values into values compatible with a range of parameters available in the ManuelbastioniLab Blender plugin.  

Another script interfaces with the ManuelbastioniLab plugin to generate humanoid figures whose parameters are dictated by the values generated from the converted MAC address. 
