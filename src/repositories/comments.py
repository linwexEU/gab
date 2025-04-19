from utils.repository import SQLAlchemyRepository 
from db.db import async_session_maker 
from sqlalchemy import update
from models.models import Comments 


class CommentsRepository(SQLAlchemyRepository): 
    model = Comments 
    
    async def like_comment(self, comment_id: int): 
        async with async_session_maker() as session: 
            query = update(self.model).where(self.model.id == comment_id).values(likes=self.model.likes + 1).returning(self.model.id)
            result = await session.execute(query) 

            await session.commit()

            return result.scalar() 
        
    async def unlike_comment(self, comment_id: int): 
        async with async_session_maker() as session: 
            query = update(self.model).where(self.model.id == comment_id).values(likes=self.model.likes - 1).returning(self.model.id) 
            result = await session.execute(query) 

            await session.commit()

            return result.scalar() 
