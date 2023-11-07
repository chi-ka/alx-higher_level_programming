import json

def load_from_json_file(filename):
    """
    Load an object from a JSON file and return it.

    Args:
        filename (str): The name of the JSON file from which to load the object.

    Returns:
        object: The deserialized object from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

