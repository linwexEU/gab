from utils.repository import SQLAlchemyRepository 
from models.models import ReportedUser 


class ReportedUserRepository(SQLAlchemyRepository): 
    model = ReportedUser 
