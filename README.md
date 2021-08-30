# WhatsApp Bulk Messages - Bot to send bulk whatsapp messages
It is a python script that sends WhatsApp message automatically from WhatsApp web application without saved contact numbers. It can be configured to send advertising messages to recipients. It read data from an excel sheet and send a configured message to people.

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed and the contact number should be saved in your phone (You can use bulk contact number saving procedure of email). There is a way without saving the contact number but has the limitation to send the attachment.

### Usage : 
    python pip install -r requirements.txt
    
    python script.py

### Dependencies
* [Python 2/3][python]
* [Selienum][selenium]
* [Chrome][chrome]
* [Pandas](https://pandas.pydata.org/)
* [Xlrd](https://pypi.org/project/xlrd/)
* [Webdriver Manager](https://pypi.org/project/webdriver-manager/)
* [openpyxl](https://pypi.org/project/openpyxl/)

### How to contribute
All contributions are welcome, from code to documentation to bug reports. Please use GitHub to its fullest-- contribute Pull Requests, contribute tutorials or other wiki content-- whatever you have to offer, we can use it!

## Important Note
* If this repository helped you to understand at least something new please give star this repository which motivates me to work further for the similar kinds for projects.

## Approach
* First need to clone this respiratory
* Run python script script.py using py script.py in the terminal
* The script opens WhatsApp web using chrome.
* User needs to scan QR code from his/her phone.
* Enter in command prompt to execute further.
* The script hit url with contact number and message from excel sheet.
* Once all the message will be sent chrome driver will automatically closed.

Note: If you wish to send an image instead of text you can write attachment selection python code.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.

Note: The script may not work in case if the HTML of web WhatsApp is changed. If you face any problem please do let me know. Surely I will help you out. You can expect response on weekend only others days extremely busy with my routine activities.

### License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

### Disclaimer
***I take no responsibility for any harm caused by the usage of this script. Have fun!***

[selenium]:http://docopt.org/
[python]:https://www.python.org/downloads/
[chrome]:https://www.google.com/chrome/
