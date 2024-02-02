from typing import List
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from database.config.db import get_session

