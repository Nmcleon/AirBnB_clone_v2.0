import pep8
import os
import console
import tests
import json
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestConsole(unittest.TestCase):
    # Other test cases to be added...

	def test_pep8_console(self):
            """Pep8 complience"""
            style = pep8.StyleGuide(quiet=True)
            p = style.check_files(["console.py"])
            self.assertEqual(p.total_errors, 0, 'fix Pep8')
            
	def test_docstrings_in_console(self):
          """checki docstring"""
          self.assertIsNotNone(console.__doc__)
          self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
          self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
          self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
          self.assertIsNotNone(HBNBCommand.do_create.__doc__)
          self.assertIsNotNone(HBNBCommand.do_show.__doc__)
          self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
          self.assertIsNotNone(HBNBCommand.do_all.__doc__)
          self.assertIsNotNone(HBNBCommand.do_update.__doc__)
          self.assertIsNotNone(HBNBCommand.do_count.__doc__)
          self.assertIsNotNone(HBNBCommand.default.__doc__)
	

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create qwerty")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="user" password="passwd"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertIn('"email": "user"', f.getvalue())
            self.assertIn('"password": "passwd"', f.getvalue())

if __name__ == "__main__":
    unittest.main()