from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel.
    
    Public attributes:
    - state_id: string, empty string, refers to the State.id
    - name: string, empty string
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes City instance.
        
        Args:
            args: Not used.
            kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
