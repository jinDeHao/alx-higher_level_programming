#!/usr/bin/python3
"""
The Base class serves as the base class
for other classes in the project.
"""
import json
import csv


class Base:
    """
    This class will be the “base” of
    all other classes in this project.

    description:
        manage id attribute in all
        my future classes
    class attribute:
        private:
            __nb_objects (int)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the object with the provided arguments.

        Args:
            id (int): attribute's id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the string object of an list dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of objects/anstances to a file
        """
        with open("{}.json\
".format(cls.__name__), 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_list = []
                for i in list_objs:
                    json_list.append(i.to_dictionary())
                file.write(Base.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        get the list of the JSON string
        representation json_string

        Args:
            json_string (str): the string from make
            list
        Return:
            list
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        the class method
        that get instance with all
        attributes already set
        """
        if cls.__name__ == "Square":
            my_dummy = cls(1)
        if cls.__name__ == "Rectangle":
            my_dummy = cls(1, 1)
        my_dummy.update(**dictionary)
        return my_dummy

    @classmethod
    def load_from_file(cls):
        """
        the class method
        that get instance with all
        attributes from a file
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save the csv to a file
        """
        with open("{}.csv".format(cls.__name__), "w", newline="") as csv_f:
            if list_objs is None or list_objs == []:
                csv_f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        the class method
        that get instance with all
        attributes from a csv file
        """
        try:
            with open("{}.csv".format(cls.__name__), "r", newline="") as csv_f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
