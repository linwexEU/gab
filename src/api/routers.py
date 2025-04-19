from api.auth import router as auth_router
from api.users import router as users_router 
from api.posts import router as posts_router
from api.followers import router as followers_router
from api.bookmarks import router as bookmarks_router
from api.comments import router as comments_router
from api.notifications import router as notifications_router
from api.reported_user import router as reported_user_router

all_routers = [auth_router, users_router, posts_router, comments_router, bookmarks_router, followers_router, notifications_router, reported_user_router]
