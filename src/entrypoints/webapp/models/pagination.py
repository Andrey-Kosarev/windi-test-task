from typing import Optional

from pydantic import BaseModel, NonNegativeInt

class Pagination(BaseModel):
    limit: Optional[NonNegativeInt] = 20
    offset: Optional[NonNegativeInt] = 0