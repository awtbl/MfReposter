from peewee import Model, IntegerField


class Channel(Model):
    """
    The class for containing channel's metadata like
        Channel's ID,
        Channel's last post ID
    """

    channel_id = IntegerField(unique=True)
    last_post_id = IntegerField()
