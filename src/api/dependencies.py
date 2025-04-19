from repositories.users import UsersRepository 
from services.users import UsersService 

from services.ip_defender import IpDefenderService 
from repositories.ip_defender import IpDefenderRepository

from services.posts import PostsService 
from repositories.posts import PostsRepository

from services.liked_posts import LikedPostsService 
from repositories.liked_posts import LikedPostsRepository

from services.comments import CommentsService
from repositories.comments import CommentsRepository

from services.followers import FollowersService 
from repositories.followers import FollowersRepository

from services.password_reset import PasswordResetService 
from repositories.password_reset import PasswordResetRepository

from services.bookmarks import BookmarksService 
from repositories.bookmarks import BookmarksRepository

from services.liked_comments import LikedCommentsService 
from repositories.liked_comments import LikedCommentsRepository

from services.notifications import NotificationsService 
from repositories.notifications import NotificationsRepository

from services.reported_user import ReportedUserService 
from repositories.reported_user import ReportedUserRepository


def users_service(): 
    return UsersService(UsersRepository)


def ip_defender_service(): 
    return IpDefenderService(IpDefenderRepository)


def posts_service(): 
    return PostsService(PostsRepository)


def liked_post_service(): 
    return LikedPostsService(LikedPostsRepository)


def comments_service(): 
    return CommentsService(CommentsRepository)


def followers_service(): 
    return FollowersService(FollowersRepository)


def password_reset_service(): 
    return PasswordResetService(PasswordResetRepository)


def bookmarks_service(): 
    return BookmarksService(BookmarksRepository)


def liked_comments_service(): 
    return LikedCommentsService(LikedCommentsRepository)


def notifications_service(): 
    return NotificationsService(NotificationsRepository)


def reported_user_service(): 
    return ReportedUserService(ReportedUserRepository)
