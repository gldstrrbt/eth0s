# stranger-friends
A Python script for collecting the mac addresses of wlan interfaces via a monitor mode enabled wireless adapter connected to a Raspberry Pi. 

Those MAC addresses are then pushed into a JSON file. 

The JSON file is parsed and the MAC addresses are converted from hexadecimal values into values that can be used for attribute values within Cinema 4D and Blender. 

A 3D model template was designed in Cinema 4D and one is generated per unique MAC address.

Another Python script is used to interface with Cinema 4D and Blender to batch import each model, and the values collected and converted from each MAC address are then used to modify different features of the model. 

The next step is to create a 3D virtual reality environment where these models can be interacted with. The ideal outcome is to showcase this in a gallery setting and setup in a way that individuals from the public would have to provide some form of personal information (phone number, email, name, age, address, etc). From there, interface with the Pipl API to search for the individual and any images of them or people related to that individual. Then taking the images collected and mapping them to the models within the environment. 

The purpose is to raise awareness with people who are unaware of the dangers of, not only providing seemingly innocuous personal information at random, but also the dangers of being tracked via monitor mode when a device's wlan interface is on and NOT connected to a wifi network. Combine this unknowing give away of a device's wlan interface's unique address, the government's access to phone records, the government's unchecked and unlawful spying on citizens, and the current administration's mission of hunting down people who are deemed "illegal" with U.S. Immigration and Customs Enforcement (ICE) agency, then the dangers are not so harmless.
