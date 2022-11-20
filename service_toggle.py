import os
import psutil

# define you service name and how you want the name displayed to the user
serviceName = 'postgresql-x64-13'
displayName = "PostgreSQL"


# get_service will find if the service you are looking for is available
def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as err:
        print(str(err))

    return service


service = get_service(serviceName)
default = "y"


# check service status and communicate to the user
if service and service['status'] == 'running':
    confirm = input(f'The {displayName} service is running. Do you want to STOP? \nY/n') or default
    if confirm.lower() == "y" or confirm == '':
        os.system("Elevate.exe net stop postgresql-x64-13")
    else:
        quit()
else:
    print()
    confirm = input(f'The {displayName} service not is running. Do you want to START? \nY/n') or default
    if confirm.lower() == "y" or confirm == '':
        os.system("Elevate.exe net start postgresql-x64-13")
    else:
        quit()


