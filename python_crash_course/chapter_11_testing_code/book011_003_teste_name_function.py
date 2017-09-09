import unittest
from book011_001_name_function import get_nome_completo

class NamesTestCase(unittest.TestCase):
    """Testando a função criada no arquivo 'book011_001_name_function.py'"""

    # a função vai ser rodada automaticamente mas deve iniciar com 'test_'
    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""

        nome = get_nome_completo('janis', 'joplin')
        self.assertEqual(nome, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""

        nome = get_nome_completo('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(nome, 'Wolfgang Amadeus Mozart')

unittest.main()
