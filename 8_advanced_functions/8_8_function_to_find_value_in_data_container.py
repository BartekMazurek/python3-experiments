# FIND VALUE IN SET & FIND VALUE IN LIST - PERFORMANCE COMPARISON
from datetime import datetime

set_container = {i for i in range(100000000)}
list_container = [i for i in range(100000000)]


def get_current_datetime_string():
    now = datetime.now()

    return now.strftime("%d/%m/%Y %H:%M:%S")


def check_if_element_exist(value_to_check, container_to_check):
    if value_to_check in container_to_check:

        return True
    else:
        return False


# TYPE time python3 <SCRIPT_NAME> TO MEASURE SCRIPT REAL EXECUTION TIME IN SECONDS

# SET CONTAINER PERFORMANCE SEARCH CHECK
# print('Set summary: ')
# check_if_element_exist(99999999, set_container)

# LIST CONTAINER PERFORMANCE SEARCH CHECK
print('List summary: ')
check_if_element_exist(99999999, list_container)
