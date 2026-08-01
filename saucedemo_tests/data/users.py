from dataclasses import dataclass

PASSWORD = "secret_sauce"

@dataclass(frozen=True)
class User:
    username: str
    password: str = PASSWORD


STANDARD_USER = User("standard_user")
LOCKED_OUT_USER = User("locked_out_user")
PROBLEM_USER = User("problem_user")
PERFORMANCE_GLITCH_USER = User("performance_glitch_user")
ERROR_USER = User("error_user")
VISUAL_USER = User("visual_user")