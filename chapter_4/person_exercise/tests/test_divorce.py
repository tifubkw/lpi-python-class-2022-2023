import datetime
import unittest

from ..person.person import Person


class DivorceTestCase(unittest.TestCase):
    """
    Test the security checks and result of the Person.divorce method.
    """

    def test_divorce(self):
        """
        Test that persons can get divorced.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        person_1.mary(person_2, "compose")
        person_1.divorce()
        assert person_1.last_name == "Smith"
        assert person_2.last_name == "Bryant"
        assert person_1.spouse is None
        assert person_2.spouse is None
    
    def test_divorce_not_married(self):
        """
        Test that persons can't get divorced if they are not married.
        """
        person = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        with self.assertRaises(ValueError) as exception_context:
            person.divorce()
            assert str(exception_context.exception) == "John Smith is not married, they can't get divorced."


if __name__ == '__main__':
    unittest.main()
