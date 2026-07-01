import json

from app.core.redis import redis_client


class RedisMemory:

    def __init__(
        self,
        session_id: str = "default"
    ):
        self.key = f"chat:{session_id}"

    def add_user_message(
        self,
        message: str
    ):
        redis_client.rpush(
            self.key,
            json.dumps(
                {
                    "role": "user",
                    "content": message
                }
            )
        )

    def add_assistant_message(
        self,
        message: str
    ):
        redis_client.rpush(
            self.key,
            json.dumps(
                {
                    "role": "assistant",
                    "content": message
                }
            )
        )

    def get_history(self):
        messages = redis_client.lrange(
            self.key,
            0,
            -1
        )

        return [
            json.loads(message)
            for message in messages
        ]

    def clear(self):
        redis_client.delete(self.key)