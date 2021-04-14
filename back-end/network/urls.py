from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('Jwitter/api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('Jwitter/api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('Jwitter/api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path("Jwitter/api/logged", views.isLogged, name="isLogged"),
    path("Jwitter/api/login", views.login_view, name="login"),
    path("Jwitter/api/logout", views.logout_view, name="logout"),
    path("Jwitter/api/register", views.register, name="register"),
    path("Jwitter/api/users", views.AllUsers, name="AllUsers"),
    path("Jwitter/api/users/<int:id>", views.OneUser, name="OneUser"),
    path("Jwitter/api/users/name/<str:username>", views.OneUserName, name="OneUserName"),
    path("Jwitter/api/users/<int:id>/mod", views.OneUserMod, name="OneUserMod"),
    path("Jwitter/api/users/<int:id>/posts", views.UserPosts, name="UserPosts"),
    path("Jwitter/api/users/<int:id>/follows", views.UserFollows, name="UserFollows"),
    path("Jwitter/api/users/<int:id>/follows/count", views.UserFollowsCount, name="UserFollowsCount"),
    path("Jwitter/api/users/<int:id>/followers", views.UserFollowers, name="UserFollowers"),
    path("Jwitter/api/users/<int:id>/followers/count", views.UserFollowersCount, name="UserFollowersCount"),
    path("Jwitter/api/users/<int:id>/follows/posts", views.UserFollowsPosts, name="UserFollowsPosts"),
    path("Jwitter/api/users/<int:id>/likes", views.UserLikes, name="UserLikes"),
    path("Jwitter/api/users/<int:id>/likes/posts/<int:id2>", views.UserLikesPost, name="UserLikesPost"),
    path("Jwitter/api/users/<int:id>/likes/comments/<int:id2>", views.UserLikesComment, name="UserLikesComment"),
    path("Jwitter/api/users/<int:id>/liked", views.UserLiked, name="UserLiked"),
    path("Jwitter/api/users/<int:id>/comments", views.UserComments, name="UserComments"),
    path("Jwitter/api/users/<int:id>/commented", views.UserCommented, name="UserCommented"),
    path("Jwitter/api/users/<int:id>/likescomments", views.UserLikesComments, name="UserLikesComments"),
    path("Jwitter/api/users/<int:id>/likedcomments", views.UserLikedComments, name="UserLikedComments"),
    path("Jwitter/api/users/<int:id>/activity", views.UserActivity, name="UserActivity"),
    path("Jwitter/api/users/<int:id>/notifications", views.UserNotifications, name="UserNotifications"),
    path("Jwitter/api/users/<int:id>/allread", views.UserAllAsRead, name="UserAllAsRead"),
    path("Jwitter/api/users/<int:id>/stats/likes/monthly", views.UsersMonthlyLikesStats, name="UsersMonthlyLikesStats"),
    path("Jwitter/api/users/<int:id>/stats/likes/daily", views.UsersDailyLikesStats, name="UsersDailyLikesStats"),
    path("Jwitter/api/users/<int:id>/stats/comments/monthly", views.UsersMonthlyCommentsStats, name="UsersMonthlyCommentsStats"),
    path("Jwitter/api/users/<int:id>/stats/comments/daily", views.UsersDailyCommentsStats, name="UsersDailyCommentsStats"),
    path("Jwitter/api/users/<int:id>/stats/posts/monthly", views.UsersMonthlyPostsStats, name="UsersMonthlyPostsStats"),
    path("Jwitter/api/users/<int:id>/stats/posts/daily", views.UsersDailyPostsStats, name="UsersDailyPostsStats"),
    path("Jwitter/api/users/<int:id>/stats/follows/monthly", views.UsersMonthlyFollowsStats, name="UsersMonthlyFollowsStats"),
    path("Jwitter/api/users/<int:id>/stats/follows/daily", views.UsersDailyFollowsStats, name="UsersDailyFollowsStats"),
    path("Jwitter/api/countries", views.AllCountries, name="AllCountries"),
    path("Jwitter/api/countries/<int:id>", views.OneCountry, name="OneCountry"),
    path("Jwitter/api/posts", views.AllPosts, name="AllPosts"),
    path("Jwitter/api/posts/mod", views.AllPostsMod, name="AllPostsMod"),
    path("Jwitter/api/posts/<int:id>", views.OnePost, name="OnePost"),
    path("Jwitter/api/posts/<int:id>/mod", views.OnePostMod, name="OnePostMod"),
    path("Jwitter/api/posts/<int:id>/likes", views.OnePostLikes, name="OnePostLikes"),
    path("Jwitter/api/posts/<int:id>/likes/sample", views.OnePostLikesSample, name="OnePostLikesSample"),
    path("Jwitter/api/posts/<int:id>/comments", views.OnePostComments, name="OnePostComments"),
    path("Jwitter/api/posts/<int:id>/comments/sample", views.OnePostCommentsSample, name="OnePostCommentsSample"),
    path("Jwitter/api/follows", views.AllFollows, name="AllFollows"),
    path("Jwitter/api/follows/mod", views.AllFollowsMod, name="AllFollowsMod"),
    path("Jwitter/api/follows/<int:id>", views.OneFollow, name="OneFollow"),
    path("Jwitter/api/follows/<int:id>/mod", views.OneFollowMod, name="OneFollowMod"),
    path("Jwitter/api/likes", views.AllLikes, name="AllLikes"),
    path("Jwitter/api/likes/mod", views.AllLikesMod, name="AllLikesMod"),
    path("Jwitter/api/likes/<int:id>", views.OneLike, name="OneLike"),
    path("Jwitter/api/likes/<int:id>/mod", views.OneLikeMod, name="OneLikeMod"),
    path("Jwitter/api/comments", views.AllComments, name="allComments"),
    path("Jwitter/api/comments/mod", views.AllCommentsMod, name="allCommentsMod"),
    path("Jwitter/api/comments/<int:id>", views.OneComment, name="OneComment"),
    path("Jwitter/api/comments/<int:id>/mod", views.OneCommentMod, name="OneCommentMod"),
    path("Jwitter/api/comments/<int:id>/likes", views.OneCommentLikes, name="OneCommentLikes"),
    path("Jwitter/api/comments/<int:id>/likes/sample", views.OneCommentLikesSample, name="OneCommentLikesSample"),
    path("Jwitter/api/likecomments", views.AllLikeComments, name="AllLikeComments"),
    path("Jwitter/api/likecomments/mod", views.AllLikeCommentsMod, name="AllLikeCommentsMod"),
    path("Jwitter/api/likecomments/<int:id>", views.OneLikeComment, name="OneLikeComment"),
    path("Jwitter/api/likecomments/<int:id>/mod", views.OneLikeCommentMod, name="OneLikeCommentMod"),
    path("Jwitter/api/stats/likes/monthly", views.MonthlyLikesStats, name="MonthlyLikesStats"),
    path("Jwitter/api/stats/likes/daily", views.DailyLikesStats, name="DailyLikesStats"),
    path("Jwitter/api/stats/comments/monthly", views.MonthlyCommentsStats, name="MonthlyCommentsStats"),
    path("Jwitter/api/stats/comments/daily", views.DailyCommentsStats, name="DailyCommentsStats"),
    path("Jwitter/api/stats/posts/monthly", views.MonthlyPostsStats, name="MonthlyPostsStats"),
    path("Jwitter/api/stats/posts/daily", views.DailyPostsStats, name="DailyPostsStats"),
    path("Jwitter/api/stats/follows/monthly", views.MonthlyFollowsStats, name="MonthlyFollowsStats"),
    path("Jwitter/api/stats/follows/daily", views.DailyFollowsStats, name="DailyFollowsStats"),
    path("Jwitter/api/stats/likecomments/monthly", views.MonthlyLikeCommentsStats, name="MonthlyLikeCommentsStats"),
    path("Jwitter/api/stats/likecomments/daily", views.DailyLikeCommentsStats, name="DailyLikeCommentsStats"),
    path("Jwitter/api/users/<int:id>/photo/mod", views.UserPostPhoto, name="UserPostPhoto"),
    path("Jwitter/api/posts/<int:id>/photo/mod", views.PostPostPhoto, name="PostPostPhoto"),
    path("Jwitter/api/posts/<int:id>/mentions/add", views.PostPostMentions, name="PostPostMentions"),
    path("Jwitter/api/comments/<int:id>/mentions/add", views.PostCommentMentions, name="PostCommentMentions"),
    path("Jwitter/api/posts/<int:id>/mentions/del", views.DeletePostMentions, name="DeletePostMentions"),
    path("Jwitter/api/comments/<int:id>/mentions/del", views.DeleteCommentMentions, name="DeleteCommentMentions"),
    path("Jwitter/api/posts/mentions/<int:id>/mod", views.PutPostMentions, name="PutPostMentions"),
    path("Jwitter/api/comments/mentions/<int:id>/mod", views.PutCommentMentions, name="PutCommentMentions"),
]