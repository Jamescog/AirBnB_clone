"""contains the defination of class state"""


from models.base_model import BaseModel


class State(BaseModel):
    """Defines the state class

    Attribute:
        name:str - name of the state
    """
    name = ""
