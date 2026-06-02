# Decentralized-Voting-System-Using-Blockchain-Concepts
# Blockchain-Based Decentralized Voting System

## Overview

This project is a learning-based implementation of a decentralized voting system using blockchain concepts. The objective is to understand how blockchain technology can be used to create secure, transparent, and tamper-evident applications.

The system stores votes as blocks in a blockchain and uses cryptographic hashing to ensure that vote records cannot be modified without detection.

This implementation is built entirely in Python using Object-Oriented Programming (OOP) principles.

---

## Features

### Core Features

* Blockchain implementation from scratch
* Block creation and chaining
* SHA-256 hashing
* Genesis block creation
* Vote storage as blockchain transactions
* Registered voter verification
* Candidate verification
* Duplicate vote prevention
* Blockchain validation
* Tampering detection
* Vote counting directly from blockchain data

---

## Bonus Features Implemented

### Proof-of-Work (PoW)

Each block is mined using a nonce value.

The hash of every block must satisfy a difficulty requirement:

```text
00ab45f9...
```

The system automatically adjusts mining difficulty based on the block creation rate.

---

### Smart Contract-Like Vote Validation

The system validates votes before adding them to the blockchain:

* Voter must be registered
* Candidate must exist
* Voter can vote only once
* Invalid votes are rejected

---

### Election Result Declaration

The system can:

* Count all votes
* Determine the winner
* Detect tied elections

Example:

```text
Winner: Alice
```

or

```text
Election Tied
Alice
Bob
```

---

### Save and Load Blockchain

Blockchain data can be stored permanently using JSON.

Functions:

```python
save_chain()
load_chain()
```

---

### Command Line Interface (CLI)

Interactive menu-driven system:

```text
===== Voting System =====

1. Register Vote
2. View Blockchain
3. Count Votes
4. Check Chain Validity
5. Declare Winner
6. Save Chain
7. Load Chain
8. Tamper Test
9. Exit
```

---

## Blockchain Structure

Each block contains:

| Field         | Description                |
| ------------- | -------------------------- |
| Index         | Position of block in chain |
| Timestamp     | Block creation time        |
| Vote Data     | Voter ID and candidate     |
| Previous Hash | Hash of previous block     |
| Nonce         | Used for Proof-of-Work     |
| Difficulty    | Mining difficulty          |
| Hash          | SHA-256 block hash         |

Example Vote Data:

```json
{
  "voter_id": "VOTER404",
  "candidate": "Alice"
}
```

---

## Project Structure

```text
Blockchain-Voting-System/
│
├── block.py
├── blockchain.py
├── voting_system.py
├── blockchain_data.json
├── screenshots/
│   ├── valid_vote.png
│   ├── duplicate_vote.png
│   ├── vote_count.png
│   ├── winner.png
│   ├── tampering.png
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
```

Move into the project directory:

```bash
cd Blockchain-Voting-System
```

Run the application:

```bash
python voting_system.py
```

---

## Sample Registered Voters

```python
[
    "VOTER404",
    "VOTER505",
    "VOTER606",
    "VOTER707",
    "VOTER808"
]
```

---

## Sample Candidates

```python
[
    "Alice",
    "Bob",
    "Charlie"
]
```

---

## Example Workflow

### Add a Vote

```text
Enter voter ID: VOTER404
Enter candidate: Alice

Vote added successfully
```

### Duplicate Vote

```text
Enter voter ID: VOTER707
Enter candidate: Bob

Voter already voted
```

### Invalid Candidate

```text
Enter voter ID: VOTER404
Enter candidate: David

Invalid candidate
```

---

## Tampering Detection

If any vote data is modified manually:

Before:

```json
{
  "candidate": "Alice"
}
```

After:

```json
{
  "candidate": "Bob"
}
```

The blockchain becomes invalid.

Output:

```text
Blockchain has been tampered
```

This demonstrates how blockchain ensures data integrity.

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* SHA-256 Hashing
* JSON Storage
* Proof-of-Work (PoW)

---

## Learning Outcomes

This project demonstrates:

* Blockchain fundamentals
* Cryptographic hashing
* Linked block structures
* Tamper-evident record keeping
* Vote validation mechanisms
* Proof-of-Work mining
* Dynamic difficulty adjustment
* Secure data storage using blockchain concepts

---


