"""contains the definition of class Place"""


from base_model import BaseModel


class Place(BaseModel):
    """Defines the class Place
    Attributes:
        city_id:str - city.id
        user_id:str - User.id
        name:str -
        description:str -
        number_rooms :int
        number_bathrooms:int
        max_guest:int
        price_by_night:int
        latitude:float
        longitude:float
        amenity_ids:list - Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

