from utils.repository import SQLAlchemyRepository 
from db.db import async_session_maker 
from sqlalchemy import delete
from models.models import LikedComments 


class LikedCommentsRepository(SQLAlchemyRepository): 
    model = LikedComments 

    async def delete_liked_comment(self, user_id: int, comment_id: int): 
        async with async_session_maker() as session: 
            query = delete(self.model).where(self.model.comment_id == comment_id, self.model.user_id == user_id).returning(self.model.id)
            result = await session.execute(query) 

            await session.commit() 

            return result.scalar() 
