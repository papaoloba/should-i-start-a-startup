from Failure import Failure

class Student:

    failure_definition=None
    need_a_salary_in_the_next_year=None
    have_cofounder=None
    have_an_idea=None

    def __init__(self, failure_definition,need_a_salary_in_the_next_year,have_cofounder,have_an_idea):
        self.failure_definition = failure_definition
        self.need_a_salary_in_the_next_year = need_a_salary_in_the_next_year
        self.have_cofounder = have_cofounder
        self.have_an_idea=self.have_an_idea

    def should_i_be_entrepreneur(self):

        if self.failure_definition == Failure.mistakes:
            return True
        elif self.failure_definition == Failure.goals:
            return False

    def should_i_start_a_startup(self):

        if self.should_i_be_entrepreneur():
            if self.need_a_salary_in_the_next_year:
                if self.have_cofounder:
                    if self.have_an_idea:
                        print("Go for it!")
                    else:
                        print("'Steal' a cool problem from an US startup and check if in Europe we have the same problem.\nIf no one (or very few) is working on it, go for it build your solution!")
                else:
                    print("Find a cofounder before leaving university and go for it!")
            else:
                print("Apply for a job in a startup you like and work there for a year or so. Then leave and start your own!")
        else: 
            print("No")
            
        

    
    
    