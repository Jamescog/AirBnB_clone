"""contains the definition of class Review"""


from base_model import BaseModel


class Review(BaseModel):
    """Define Review
    Attributes:
        place_id:str -Place.id
        user_id:str - User.id
        text:str
    """

    place_id = ""
    user_id = ""
    text = ""

