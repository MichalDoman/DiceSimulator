# DiceSimulator (workshop exercise)

This app works in a terminal. The program takes a dice-code as an input. The dice code should be given in a form of e.g.
5D6 or 10D12-10, where the first code would mean: 5 throws of a 6-sided die, and the second: 10 throws with a 12-sided
die, and from the total score, 10 would be subtracted (modifier = -10).

After the user inputs their code, the program interprets it the way as explained above. Next, all the throws are
conducted and displayed, as well as the total score, including the modifier if such was given.

```
Type in the code and the system will generate the moves: 5D6-10
Throw number 1: 3
Throw number 2: 6
Throw number 3: 3
Throw number 4: 4
Throw number 5: 5
Your score was: 11!
```
The program allows any type of dice, even if were impossible in real life:
```
Type in the code and the system will generate the moves: 5D13
Throw number 1: 3
Throw number 2: 11
Throw number 3: 2
Throw number 4: 13
Throw number 5: 11
Your score was: 40!
```
