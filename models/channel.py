from sqlmodel import SQLModel, Field


class Channel(SQLModel):
    """
    The class for containing channel's metadata like
        Channel's ID,
        Channel's last post ID
    """

    channel_id: int
    last_post_id: int = Field(default=0)
