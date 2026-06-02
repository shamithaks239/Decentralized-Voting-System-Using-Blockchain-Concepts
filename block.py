import hashlib
import json


class Block:
    def __init__(
        self,
        index,
        timestamp,
        vote_data,
        previous_hash,
        nonce=0,
        hash_value=None
    ):
        self.index = index
        self.timestamp = timestamp
        self.vote_data = vote_data
        self.previous_hash = previous_hash
        self.nonce = nonce

        if hash_value:
            self.hash = hash_value
        else:
            self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + json.dumps(self.vote_data, sort_keys=True)
            + str(self.previous_hash)
            + str(self.nonce)
        )

        return hashlib.sha256(
            block_string.encode()
        ).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "vote_data": self.vote_data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }