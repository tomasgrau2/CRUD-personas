import unittest
import personaservice
from unittest.mock import patch

from personaservice import Persona


class TestPersona(unittest.TestCase):
    def test_constructor(self):
        persona = Persona()
        self.assertEqual(persona.__dict__, {'documento':"",'apellido':'', 'nombre':'', 'personas':[]})

    @patch('builtins.input', side_effect=[3, 'Trump', 'Donald'])
    def test_add_persona(self, mock_input):
        persona = Persona()
        persona.addPersona()
        self.assertEqual(persona.personas, [[3,'Donald','Trump']])

    def test_load_file(self):
        persona=Persona()
        persona.load_file()
        self.assertEqual(persona.personas,[['44634957', 'Tomas', 'Grau'], ['63548489', 'Juan Pablo', 'Samso']])

if __name__ == '__main__':
    unittest.main()