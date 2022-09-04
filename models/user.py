"""contains the defination of User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """The user class that define  users
    
    Attributes:
        email: str - email of the user
        password:str - password of the user
        first_name:str - First name of the user
        last_name:str - Last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

