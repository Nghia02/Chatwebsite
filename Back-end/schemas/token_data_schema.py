# -*- coding: utf-8 -*-
from pydantic import BaseModel


class TokenData(BaseModel):
    username: str
