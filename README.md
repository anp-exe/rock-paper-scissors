# Rock Paper Scissors

A Python implementation of the classic Rock Paper Scissors game (and its extended variant, Rock Paper Scissors Lizard Spock), built as part of a [Codedex](https://www.codedex.io) project.

## Game Rules

The player competes against the computer in a single round.

**Classic version:**
- Rock beats Scissors
- Scissors beat Paper
- Paper beats Rock

**Bonus: Rock Paper Scissors Lizard Spock**

An extended variant popularized by *The Big Bang Theory*, invented by Sam Kass to reduce the frequency of ties:

- Scissors cut Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors beat Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock breaks Scissors

## How to Play

Run the program and pick a number when prompted:

**Classic (1–3):**
```
1) ✊  Rock
2) ✋  Paper
3) ✌️  Scissors
```

**Lizard Spock (1–5):**
```
1) ✊  Rock
2) ✋  Paper
3) ✌️  Scissors
4) 🦎  Lizard
5) 🖖  Spock
```

The computer picks randomly, and the winner is announced.

## Example Output

```
===================
Rock Paper Scissors
===================

1) ✊
2) ✋
3) ✌️
Pick a number: 2

You chose: ✋
CPU chose: ✊
The player won!
```

## Requirements

- Python 3
