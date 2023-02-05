import datetime


class Person:
    DEFAULT_COUNTRY = "France"
    instances = []

    def __init__(
        self,
        first_name: str,
        last_name: str,
        biological_gender,
        parents,
        spouse=None,
        children=[],
        country=DEFAULT_COUNTRY,
        date_of_birth=datetime.date.today(),
        date_of_death=None
    ):
        self.instances.append(self)
        self.first_name = first_name
        self.maiden_name = last_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.biological_gender = biological_gender
        self.spouse = spouse
        self.children = children
        self.parents = parents
        self.country = country
        self.date_of_death = date_of_death
    
    @property
    def is_alive(self):
        return self.date_of_death is None
    
    @property
    def age(self):
        today = datetime.date.today()
        born = self.date_of_birth
        return today.year - born.year - (0 if today.month >= born.month and today.day >= born.day else 1)
    
    @classmethod
    def _check_if_person(cls, instance, action):
        if not isinstance(instance, cls):
            raise TypeError(f"It's impossible to {action} with a {type(instance)}.")

    def _check_if_alive(self, action):
        if not self.is_alive:
            raise ValueError(f"{self} is dead, they can't {action}.")
            
    def _check_if_old_enough(self, action, age):
        if not self.age >= age:
            raise ValueError(f"{self} is too young to {action}.")
    
    def _check_if_self(self, instance, action):
        if self == instance:
            raise ValueError(f"You can't {action} with yourself.")
    
    def _check_if_parents(self, instance, action):
        if instance in self.parents or self in instance.parents:
            raise ValueError(f"Please don't {action} with your own family members.")
            
    def _make_marriage_checks(self, someone):
        action = "get married"
        age = 18
        self._check_if_person(someone, action)
        self._check_if_self(someone, action)
        self._check_if_parents(someone, action)
        someone._check_if_parents(self, action)
        self._check_if_alive(action)
        someone._check_if_alive(action)
        self._check_if_old_enough(action, age)
        someone._check_if_old_enough(action, age)
        
        
    def unalive(self, new_date_of_death=datetime.date.today()):
        self.date_of_death = new_date_of_death
        
    def mary(self, someone, what_to_do_with_name = "pass"):
        """
        This method marries someone with instance it is called on
        
        Arguments
        ---------
        someone : Person
            person the instance is marrying
        what_to_do_with_name : string["pass", "own", "compose"]
            what to do with last name
        """
        self._make_marriage_checks(someone)
        
        self.spouse = someone
        someone.spouse = self
        
        match what_to_do_with_name:
            case "own":
                someone.last_name = self.last_name
            case "compose":
                someone.last_name = f"{someone.maiden_name}-{self.maiden_name}"
                self.last_name = f"{self.maiden_name}-{someone.maiden_name}"
            case "pass":
                pass
            case _:
                pass
        return (self, someone,)
    
    def __repr__(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
        return self.first_name + " " + self.last_name
