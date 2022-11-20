##Toggle PostgreSQL

This script will check to see if a service is running on a Windows system.
If the service is running, it will ask the user if they want to STOP the service. If the service is not running, it will ask the user if they want to START the service.

To start or stop a service, you do need to escalate to Admin Rights.
This script users Elevate.exe to signal UAC.
https://github.com/jpassing/elevate


Users will still need to answer the UAC challenge. This challenge should not be silenced.

