from uuid import UUID

class InvalidChatType(Exception):
    ...

class InvalidNumberOfParticipants(Exception):
    ...

class DuplicateIdempotencyKey(Exception):
    def __init__(self, key: UUID):
        self.duplicate_key = key