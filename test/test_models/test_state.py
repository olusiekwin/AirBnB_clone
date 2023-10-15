import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """

    def test_child_class(self):
        """
        Test if State is a child class of BaseModel
        """
        state = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_attribute(self):
        """
        Test for the existence of its attribute
        """
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_empty_string(self):
        """
        Test for an empty string attribute
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        """
        Test case to convert State class into a dictionary
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_str(self):
        """
        Test case for str method in BaseModel class
        """
        state = State()
        string = str(state)
        self.assertIn('[State]', string)

    def test_save(self):
        """
        Test the save method
        """
        state = State()
        orig_time = state.created_at
        upd_time = state.updated_at
        state.save()
        self.assertNotEqual(orig_time, state.created_at)
        self.assertNotEqual(upd_time, state.updated_at)


if __name__ == '__main__':
    unittest.main()
