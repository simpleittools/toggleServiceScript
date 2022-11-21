import os
import psutil

# define you service name and how you want the name displayed to the user
serviceName = 'postgresql-x64-13'
displayName = "PostgreSQL"


# get_service will find if the service you are looking for is available
def get_service(name):
    service_check = None
    try:
        service_check = psutil.win_service_get(name)
        service_check = service_check.as_dict()
    except Exception as err:
        print(str(err))

    return service_check


service = get_service(serviceName)
default = "y"


# check service status and communicate to the user
if service and service['status'] == 'running':
    confirm = input(f'The {displayName} service is running. Do you want to STOP? (Y/n) \n') or default
    if confirm.lower() == "y" or confirm == '':
        os.system(f'Elevate.exe net stop {serviceName}')
    else:
        quit()
else:
    confirm = input(f'The {displayName} service not is running. Do you want to START? (Y/n) \n') or default
    if confirm.lower() == "y" or confirm == '':
        os.system(f'Elevate.exe net start {serviceName}')
    else:
        quit()


