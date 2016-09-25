import requests
from typing import List

def get_json_from_url(url: str):
    """
    Wrapper around requests object to get the JSON object
    located at the given URL.

    :param url: The URL to be accessed
    :return: The JSON object found at the given URL
    """
    return requests.get(url).json()

def get_dependencies_from_json(analysis) -> List[str]:
    """
    Get all dependencies for the package with the
    given analysis.

    :param analysis: Dump of analysed data for a single package
    :return: Names of all dependencies of the given package
    """
    try:
        dependencies_with_versions = analysis["collected"]["metadata"]["dependencies"]
        return list(dependencies_with_versions.keys())
    except KeyError:
        return []

def get_dependencies_url(package_name: str) -> str:
    """
    Get the URL of the analysis page for the given package

    :param package_name: Name of package to look up
    :return: URL of analysis of the given package
    """
    return "https://api.npms.io/v2/package/{}".format(package_name)

def get_dependencies(package_name: str) -> List[str]:
    """
    Get all dependencies of the given package.

    :param package_name: Name of package to be browsed
    :return: List of dependencies of the given package
    """
    url = get_dependencies_url(package_name)
    return get_dependencies_from_json(get_json_from_url(url))