from quiz.models.rank import PlayerRank, Point 

#get actual rank of user 
def get_rank(player_rank):
   
    rank = PlayerRank.objects.order_by("-total_points").filter(total_points__lte=player_rank.total_points).count()

    return rank

# update list of points after realized quiz
def update_rank(player_rank,point :Point):
    player_rank.points.add(point)

    player_rank.set_total_points()