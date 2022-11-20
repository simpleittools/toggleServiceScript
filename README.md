#Toggle Windows Service

##Explanation
I originally created this to toggle Postgresql on my testing computer (Docker is great, but my testing computer is direct system interactions). With this, I set up buttons on my Stream Deck to toggle various services as I need them.
By moving the Service Name and Display Names to variable, I was able to reuse the script for multiple services.

This script will check to see if a service is running on a Windows system.
If the service is running, it will ask the user if they want to STOP the service. If the service is not running, it will ask the user if they want to START the service.

##Dependancy
To start or stop a service, you do need to escalate to Admin Rights.
This script users Elevate.exe to signal UAC.
https://github.com/jpassing/elevate


Users will still need to answer the UAC challenge. This challenge should not be silenced. It is a critical security item.

##Usage
You will need to set Elevate.exe into your path variable, or edit lines 27 and 34 to show the full path of Elevate.exe

To select which service you want to toggle, edit the variable:

"serviceName" to match the Service name from Windows services.msc

example: postgresql-x64-13

For end user communication, edit the "displayName" variable to match the printed display name as you wish to see it.

example: PostgreSQL