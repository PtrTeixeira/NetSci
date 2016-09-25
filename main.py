from get_dependencies import get_dependencies
from list_packages import get_packages
import itertools as it


def build_output():
    for package in get_packages():
        yield {
            "name": package,
            "dependencies": get_dependencies(package)
        }

if __name__ == '__main__':
    with open("output.txt", 'w') as f:
        # Temporarily limiting the output
        for package in it.islice(build_output(), 1000):
            f.write(str(package) + "\n")