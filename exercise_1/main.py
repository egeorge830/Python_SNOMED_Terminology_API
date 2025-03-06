from pprint import pprint
import requests

BASE_HERMES_URL = 'http://159.65.173.51:8080/v1/snomed/concepts'


def task_1(concept_id):
    try:
        # Construct the full URL
        url = f'{BASE_HERMES_URL}/{concept_id}'
        # Make the GET request
        response = requests.get(url)
        print(response.url)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            print(f"Effective time: {data['effectiveTime']}")
            print(f"Concept ID: {data['id']}")
        else:
            return {
                "error": f"Failed to fetch data. HTTP Status Code: {response.status_code}",
                "details": response.text
            }
    except requests.RequestException as e:
        # Handle network-related errors
        return {"error": "Network error occurred", "details": str(e)}


def task_2(concept_id):
    response = requests.get(f'{BASE_HERMES_URL}/{concept_id}/descriptions')
    print(response.url)
    data = response.json()
    for item in data:
        status = 'Inactive'
        if item['active']:
            status = 'Active'
        print(f"{status} | Effective time: {item['effectiveTime']} | Term: {item['term']}")

def task_3(concept_id):
    response = requests.get(f'{BASE_HERMES_URL}/{concept_id}/extended')
    print(response.url)

    if response.status_code == 200:
        data = response.json()


        preferred_description = data.get('preferredDescription', {}).get('term', 'N/A')

        print(f"Preferred Description: {preferred_description}\n")
        print("Process finished with exit code 0")


if __name__ == "__main__":
    snomed_concept_id = "80967001"
    task_1(concept_id=snomed_concept_id)
    task_2(concept_id=snomed_concept_id)
    task_3(concept_id=snomed_concept_id)

