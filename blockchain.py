import json
from datetime import datetime

from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []

        self.registered_voters = [
            "VOTER101",
            "VOTER102",
            "VOTER103",
            "VOTER104",
            "VOTER105"
        ]

        self.candidates = [
            "Alice",
            "Bob",
            "Charlie"
        ]

        # Dynamic difficulty settings
        self.difficulty = 2
        self.target_block_time = 5  # seconds

        self.voting_deadline = None

        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(
            index=0,
            timestamp=str(datetime.now()),
            vote_data={
                "voter_id": "GENESIS",
                "candidate": "NONE"
            },
            previous_hash="0"
        )

        genesis.mine_block(self.difficulty)
        self.chain.append(genesis)

    def get_latest_block(self):
        return self.chain[-1]

    def has_voted(self, voter_id):
        for block in self.chain[1:]:
            if block.vote_data["voter_id"] == voter_id:
                return True
        return False

    def validate_vote(self, voter_id, candidate):
        if voter_id not in self.registered_voters:
            return False, "Voter not registered"

        if candidate not in self.candidates:
            return False, "Invalid candidate"

        if self.has_voted(voter_id):
            return False, "Voter already voted"

        if self.voting_deadline:
            if datetime.now() > self.voting_deadline:
                return False, "Voting deadline passed"

        return True, "Vote valid"

    def adjust_difficulty(self, block_creation_time):
        if block_creation_time < self.target_block_time / 2:
            self.difficulty += 1

        elif (
            block_creation_time > self.target_block_time * 2
            and self.difficulty > 1
        ):
            self.difficulty -= 1

    def add_vote(self, voter_id, candidate):
        valid, message = self.validate_vote(
            voter_id,
            candidate
        )

        if not valid:
            print(message)
            return

        vote_data = {
            "voter_id": voter_id,
            "candidate": candidate
        }

        previous_block = self.get_latest_block()

        start_time = datetime.now()

        new_block = Block(
            index=len(self.chain),
            timestamp=str(datetime.now()),
            vote_data=vote_data,
            previous_hash=previous_block.hash
        )

        new_block.mine_block(self.difficulty)

        end_time = datetime.now()

        elapsed = (
            end_time - start_time
        ).total_seconds()

        self.adjust_difficulty(elapsed)

        self.chain.append(new_block)

        print("Vote added successfully")
        print(f"Block mined with difficulty {self.difficulty}")

    def count_votes(self):
        result = {
            candidate: 0
            for candidate in self.candidates
        }

        for block in self.chain[1:]:
            candidate = block.vote_data["candidate"]
            result[candidate] += 1

        return result

    def declare_winner(self):
        votes = self.count_votes()

        highest = max(votes.values())

        winners = [
            candidate
            for candidate, count in votes.items()
            if count == highest
        ]

        if highest == 0:
            print("No votes cast")
            return

        if len(winners) > 1:
            print("Election tied between:")
            for winner in winners:
                print(winner)

        else:
            print(f"Winner: {winners[0]}")

    def is_valid(self):
        voters_seen = set()

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

            if (
                not current.hash.startswith(
                    "0" * self.difficulty
                )
            ):
                pass

            voter = current.vote_data["voter_id"]

            if voter in voters_seen:
                return False

            voters_seen.add(voter)

        return True

    def display_chain(self):
        for block in self.chain:
            print(json.dumps(
                block.to_dict(),
                indent=4
            ))
            print("-" * 50)

    def save_chain(
        self,
        filename="blockchain_data.json"
    ):
        data = [
            block.to_dict()
            for block in self.chain
        ]

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Blockchain saved")

    def load_chain(
        self,
        filename="blockchain_data.json"
    ):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.chain = []

            for item in data:
                block = Block(
                    index=item["index"],
                    timestamp=item["timestamp"],
                    vote_data=item["vote_data"],
                    previous_hash=item["previous_hash"],
                    nonce=item["nonce"],
                    hash_value=item["hash"]
                )

                self.chain.append(block)

            print("Blockchain loaded")

        except FileNotFoundError:
            print("No saved blockchain found")


