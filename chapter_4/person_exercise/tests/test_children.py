import datetime
import unittest

from ..person.person import Person


class ChildrenTestCase(unittest.TestCase):
    """
    Test the security checks and result of the Person.procreate method.
    """
    def test_have_child_no_params(self):
        """
        Test that persons can have children.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        child = person_1.procreate(person_2, "Alex")
        assert child.first_name == "Alex"
        assert child.last_name == "Smith"
        assert child.parents == [person_1, person_2]
        assert child in person_1.children
        assert child in person_2.children
        assert child.biological_gender in ["M", "F"]
    
    def test_have_child_with_last_name(self):
        """
        Test that persons can have children.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        child = person_1.procreate(person_2, "Alex", last_name="Smithyant")
        assert child.first_name == "Alex"
        assert child.last_name == "Smithyant"
        assert child.parents == [person_1, person_2]
        assert child in person_1.children
        assert child in person_2.children
        assert child.biological_gender in ["M", "F"]
    
    def test_have_child_with_country(self):
        """
        Test that persons can have children.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        child = person_1.procreate(person_2, "Alex", country="USA")
        assert child.first_name == "Alex"
        assert child.last_name == "Smith"
        assert child.country == "USA"
        assert child.parents == [person_1, person_2]
        assert child in person_1.children
        assert child in person_2.children
        assert child.biological_gender in ["M", "F"]

    def test_have_child_with_dead_person(self):
        """
        Test that a dead person can't have children.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        person_1.unalive()
        with self.assertRaises(ValueError) as exception_context:
            person_1.procreate(person_2, "Alex")
            assert str(exception_context.exception) == "John Smith is dead, they can't have children."

    def test_have_child_with_dead_person_reverse(self):
        """
        Test that a dead person can't have children.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        person_2.unalive()
        
        with self.assertRaises(ValueError) as exception_context:
            person_1.procreate(person_2, "Alex")
            assert str(exception_context.exception) == "John Bryant is dead, they can't have children."
    
    def test_have_child_with_self(self):
        """
        Test that a person can't have children with themselves.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        with self.assertRaises(ValueError) as exception_context:
            person_1.procreate(person_1, "Alex")
            assert str(exception_context.exception) == "You can't have children with yourself."

    def test_have_child_with_non_person(self):
        """
        Test that a person can't have children with a non-person.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2000, 2, 2))
        with self.assertRaises(TypeError) as exception_context:
            person_1.procreate("John Bryant", "Alex")
            assert str(exception_context.exception) == "It's impossible to have children with a <class 'str'>."

    def test_have_child_with_someone_too_young(self):
        """
        Test that a person can't have children with someone too young.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(2022, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(1999, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_1.procreate(person_2, "Alex")
            assert str(exception_context.exception) == "John Smith is too young to have children."

    def test_have_child_with_someone_too_young_reverse(self):
        """
        Test that a person can't have children with someone too young.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(1999, 2, 2))
        person_2 = Person("John", "Bryant", "M", [], date_of_birth=datetime.date(2022, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_1.procreate(person_2, "Alex")
            assert str(exception_context.exception) == "John Bryant is too young to have children."

    def test_have_child_with_parent(self):
        """
        Test that a person can't have children with their parent.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(1999, 2, 2))
        person_2 = Person("John", "Bryant", "M", [person_1], date_of_birth=datetime.date(1979, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_1.procreate(person_2, "Alex")
            assert str(exception_context.exception) == "Please don't have children with your own family members."

    def test_have_child_with_parent_reverse(self):
        """
        Test that a person can't have children with their parent.
        """
        person_1 = Person("John", "Smith", "M", [], date_of_birth=datetime.date(1999, 2, 2))
        person_2 = Person("John", "Bryant", "M", [person_1], date_of_birth=datetime.date(1979, 2, 7))
        with self.assertRaises(ValueError) as exception_context:
            person_2.procreate(person_1, "Alex")
            assert str(exception_context.exception) == "Please don't have children with your own family members."


if __name__ == '__main__':
    unittest.main()
