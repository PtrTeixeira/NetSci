from lxml import html
import requests


def get_depends_package_url(package_name: str) -> str:
    """
    Get the URL of a web-page that is lists all the dependents
    of the given package.

    :param package_name: Name of the package to look up
    :return: URL listing all packages that depend on the given package
    """
    return "https://npmjs.com/browse/depended/{}".format(package_name)


def get_html_from_url(url: str) -> html.Element:
    """
    Get a remote HTML resource and transform it into a
    query-able Python object.

    :param url: URL to make an HTTP request to
    :return: HTML Element that to be queried
    """
    page = requests.get(url)
    return html.fromstring(page.content)

def parse_depends_to_links(page: html.HtmlElement):
    """
    Get the names of all the dependents of the package on
    :param page:
    :return:
    """
    return [x.text_content() for x in page.find_class("name")]

def depends_has_next(page: html.HtmlElement) -> bool:
    return len(page.find_class("next")) == 0

def get_depends_next_page(page: html.HtmlElement) -> html.HtmlElement:
    url = page.find_class("next")[0].get("href")
    return get_html_from_url(url)