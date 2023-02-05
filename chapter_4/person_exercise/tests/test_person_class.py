import datetime
import unittest

from ..person.person import Person


class MarriageTestCase(unittest.TestCase):
    """
    Test the security checks and result of the Person.mary method.
    """

    def test_name_option_compose(self):
        """
        Test that persons can get married and compose their last name.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        result = person_1.mary(person_2, "compose")
        assert person_1.last_name == "Smith-Bryant"
        assert person_2.last_name == "Bryant-Smith"
        assert person_1.spouse == person_2
        assert person_2.spouse == person_1

    def test_name_option_pass(self):
        """
        Test that persons can get married and both keep their last name.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        result = person_1.mary(person_2, "pass")
        assert person_1.last_name == "Smith"
        assert person_2.last_name == "Bryant"
        assert person_1.spouse == person_2
        assert person_2.spouse == person_1

    def test_name_option_own(self):
        """
        Test that persons can get married and keep one of their last name.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        result = person_1.mary(person_2, "own")
        assert person_1.last_name == "Smith"
        assert person_2.last_name == "Smith"
        assert person_1.spouse == person_2
        assert person_2.spouse == person_1

    def test_marry_dead_person(self):
        """
        Test that a dead person can't get married.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        person_1.unalive()
        with self.assertRaises(ValueError) as exception_context:
            person_1.mary(person_2, "compose")
            assert str(exception_context.exception) == "John Smith is dead, they can't get married."

    def test_marry_dead_person_reverse(self):
        """
        Test that a dead person can't get married.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        person_2.unalive()
        
        with self.assertRaises(ValueError) as exception_context:
            person_1.mary(person_2, "compose")
            assert str(exception_context.exception) == "John Bryant is dead, they can't get married."
    
    def test_marriage_with_self(self):
        """
        Test that a person can't get married with themselves.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        with self.assertRaises(ValueError) as exception_context:
            person_1.mary(person_1, "compose")
            assert str(exception_context.exception) == "You can't get married with yourself."

    def test_mary_with_non_person(self):
        """
        Test that a person can't get married with a non-person.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        with self.assertRaises(TypeError) as exception_context:
            person_1.mary("John Bryant", "compose")
            assert str(exception_context.exception) == "It's impossible to get married with a <class 'str'>."

    def test_marry_someone_too_young(self):
        """
        Test that a person can't get married with someone too young.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2010, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_1.mary(person_2, "compose")
            assert str(exception_context.exception) == "John Smith is too young to get married."

    def test_marry_someone_too_young_reverse(self):
        """
        Test that a person can't get married with someone too young.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(1999, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(2010, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_1.mary(person_2, "compose")
            assert str(exception_context.exception) == "John Bryant is too young to get married."

    def test_marry_parent(self):
        """
        Test that a person can't get married with their parent.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(1999, 2, 2))
        person_2 = Person("John", "Bryant", "M", [person_1], date_of_birth=datetime.date(1979, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_1.mary(person_2, "compose")
            assert str(exception_context.exception) == "Please don't get married with your own family members."

    def test_marry_parent_reverse(self):
        """
        Test that a person can't get married with their parent.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(1999, 2, 2))
        person_2 = Person("John", "Bryant", "M", [person_1], date_of_birth=datetime.date(1979, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_2.mary(person_1, "compose")
            assert str(exception_context.exception) == "Please don't get married with your own family members."


if __name__ == '__main__':
    unittest.main()
