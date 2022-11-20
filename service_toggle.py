import os
import psutil

serviceName = 'postgresql-x64-13'
displayName = "PostgreSQL"


def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))

    return service


service = get_service(serviceName)


if service and service['status'] == 'running':
    print(f'The {displayName} service is running. Do you want to STOP? \ny/n')
    confirm = input()
    if confirm == "y":
        os.system("Elevate.exe net stop postgresql-x64-13")
    else:
        quit()
else:
    print(f'The {displayName} service not is running. Do you want to START? \ny/n')
    confirm = input()
    if confirm == "y":
        os.system("Elevate.exe net start postgresql-x64-13")
    else:
        quit()


