import requests
from typing import List, Generator

def get_json_from_url(url: str):
    """
    Wrapper around requests object to get the JSON object
    located at the given URL.

    :param url: The URL to be accessed
    :return: The JSON object found at the given URL
    """
    return requests.get(url).json()

def get_package_list_json(start_index: int):
    """

    :return: A JSON object containing a list of packages
    """
    size = 50
    url = "https://api.npms.io/v2/search?q=not:deprecated&from={}&size={}" \
        .format(start_index, size)
    return get_json_from_url(url)

def get_package_names(packages_json) -> List[str]:
    """
    Extract the list of package names from the given JSON list.

    :param packages_json: JSON object containing list of all packages
    :return: Extracted list of package names
    """
    return [package["package"]["name"] for package in packages_json["results"]]

def get_package_count(packages_json) -> int:
    return packages_json["total"]



def get_packages() -> Generator[str, None, None]:
    start_index = 0
    initial_packages_json = get_package_list_json(start_index)
    total = get_package_count(initial_packages_json)
    packages = get_package_names(initial_packages_json)
    while packages:
        to_return = packages.pop(0)
        start_index += 1
        if len(packages) == 0 and start_index < total:
            packages = get_package_names(get_package_list_json(start_index))
        yield to_return
    return