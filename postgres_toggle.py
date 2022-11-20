import os
import psutil


def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))

    return service


service = get_service('postgresql-x64-13')


if service and service['status'] == 'running':
    print('The PostgreSQL service is running. Do you want to STOP? y/n')
    confirm = input()
    if confirm == "y":
        # change path to the location of E
        os.system("Elevate.exe net stop postgresql-x64-13")
    else:
        quit()
else:
    print('The PostgreSQL service not is running. Do you want to START? y/n')
    confirm = input()
    if confirm == "y":
        os.system("Elevate.exe net start postgresql-x64-13")
    else:
        quit()


