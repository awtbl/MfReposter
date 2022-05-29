from tortoise.models import Model, IntField


class Channel(Model):
    """
    The class for containing channel's metadata like
        Channel's ID,
        Channel's last post ID
    """

    identifier = IntField()
    last_post_id = IntField(default=0)
