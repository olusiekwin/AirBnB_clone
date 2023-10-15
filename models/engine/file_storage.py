from json import dumps, loads
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class that provides a file storage module for serializing instances to a
    JSON file
    and deserializing JSON files to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects stored in the storage.

        Returns:
            dict: A dictionary containing all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize the objects dictionary to a JSON file.
        """
        final_dict = {key: value.to_dict() for key, value in
                      FileStorage.__objects.items()}
        json_string = dumps(final_dict)
        filename = FileStorage.__file_path
        with open(filename, "w") as f:
            f.write(json_string)

    def reload(self):
        """
        Deserialize the JSON file and update the objects dictionary.
        If the JSON file (__file_path) exists, it reads the file and loads
        objects.
        If the file doesn't exist, it does nothing.
        """
        allowed_classes = ["BaseModel", "User", "State", "City", "Amenity",
                           "Place", "Review"]
        filename = FileStorage.__file_path

        if isfile(filename):
            with open(filename, "r") as f:
                json_string = f.read()
                final_dict = loads(json_string)

            for key, value in final_dict.items():
                class_name, obj_id = key.split(".")
                if class_name in allowed_classes:
                    eval("self.new({}(**value))".format(class_name))
