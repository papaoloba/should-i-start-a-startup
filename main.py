from Student import Student
from Failure import Failure

me = Student(
    failure_definition = Failure.mistakes,
    need_a_salary_in_the_next_year = False,
    have_cofounder=True,
    have_an_idea=False
    )

me.should_i_start_a_startup()