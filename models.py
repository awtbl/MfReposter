from peewee import Model, IntegerField, SqliteDatabase

db = SqliteDatabase('data.db')


class Channel(Model):
    """
    The class for containing channel's metadata like
        Channel's ID,
        Channel's last post ID
    """

    channel_id = IntegerField()
    last_post_id = IntegerField()

    class Meta:
        database = db

        indexes = (
            (("channel_id",), False),
        )
