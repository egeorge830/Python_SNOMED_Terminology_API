from pprint import pprint
import requests

BASE_HERMES_URL = 'http://159.65.173.51:8080/v1/snomed'

"""
https://www.hddaccess.com/tips/searching-in-snomed-ct-using-ecl-2
"""


def constraint_1():
    constraint = """
<< 404684003 |Clinical finding (finding)| :

<< 116676008 |Associated morphology (attribute)| = << 44132006 |Abscess (morphologic abnormality)|

AND << 363698007 |Finding site (attribute)| = << 113279002 |Gingival structure (body structure)|
    """
    return constraint


def expression_constraint(search_string):
    response = requests.get(f'{BASE_HERMES_URL}/search?constraint={search_string}')
    data = response.json()
    for item in data:
        print(f"{item['term']} | {item['preferredTerm']} | {item['conceptId']}" )


if __name__ == '_main_':
    string_value = constraint_1().strip()
    print()
    expression_constraint(search_string=string_value)