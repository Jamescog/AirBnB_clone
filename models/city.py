"contains the definition of class City"


from base_model import BaseModel


class City(BaseModel):
    """Defines the class City
    
    Attribute:
        state_id:str - State id
        name:str - name of city
    """
    state_id = ""
    name = ""

