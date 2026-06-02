
from blockchain import Blockchain


def main():
    blockchain = Blockchain()

    while True:

        print("\n===== Voting System =====")
        print("1. Register Vote")
        print("2. View Blockchain")
        print("3. Count Votes")
        print("4. Check Chain Validity")
        print("5. Declare Winner")
        print("6. Save Chain")
        print("7. Load Chain")
        print("8. Tamper Test")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            voter_id = input(
                "Enter voter id: "
            )

            candidate = input(
                "Enter candidate: "
            )

            blockchain.add_vote(
                voter_id,
                candidate
            )

        elif choice == "2":
            blockchain.display_chain()

        elif choice == "3":
            votes = blockchain.count_votes()

            print("\nVote Count")
            for candidate, count in votes.items():
                print(
                    f"{candidate}: {count}"
                )

        elif choice == "4":
            if blockchain.is_valid():
                print(
                    "Blockchain is valid"
                )
            else:
                print(
                    "Blockchain is INVALID"
                )

        elif choice == "5":
            blockchain.declare_winner()

        elif choice == "6":
            blockchain.save_chain()

        elif choice == "7":
            blockchain.load_chain()

        elif choice == "8":
            if len(blockchain.chain) > 1:
                blockchain.chain[1].vote_data[
                    "candidate"
                ] = "Bob"

                print(
                    "Tampering completed"
                )

            else:
                print(
                    "Need at least one vote"
                )

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

