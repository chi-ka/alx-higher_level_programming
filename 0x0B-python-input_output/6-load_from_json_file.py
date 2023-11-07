import json

def save_to_json_file(my_obj, filename):
    """
    Serialize the given object to a JSON representation and write it to the specified file.

    Args:
        my_obj (object): The object to be serialized to JSON.
        filename (str): The name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

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

