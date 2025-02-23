from datetime import date, datetime
from pydantic import EmailStr, BaseModel
from typing import List, Optional, Union


class EmailSchema(BaseModel):
    emailAddress: EmailStr
