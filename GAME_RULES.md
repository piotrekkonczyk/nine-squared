# Game Rules

Very simple game, yet so much fun.

In the beginning, program generates a 3x3 square with 9 cards.

Also, the card on top (obviously hidden) is generated. Your goal is very simple:

> To point out is the card on top higher/lower than one of the cards from the square.

Let's say you have this situation:

```txt
A ◆     Q ♣     6 ♣

10 ♣     2 ♠     K ❤

10 ❤     6 ♠     3 ♣
```

You'd like to check the card on top against a **Q ♣**.

You decided that the card on top is going to be smaller.

You can do so by inputting *Q j* (or however you did bind the `config.key_below`).

```txt
Guess: Q j
You won!
The card was 4 ♣

42 left in the deck

A ◆     4 ♣     6 ♣

10 ♣     2 ♠     K ❤

10 ❤     6 ♠     3 ♣
```

We won! Now, as you see, Queen was replaced with 4.
And we can guess again.

```txt
42 left in the deck

A ◆     4 ♣     6 ♣

10 ♣     2 ♠     K ❤

10 ❤     6 ♠     3 ♣

NOTE: card is on the table
Guess:
```

But this time the value of card on top is already on the square.

> [!NOTE]
> Now you guess like usually, but:
> If you guess the card on the square, you are entitled to open a new pile.
> Doesn't matter, whether the guess was with `config.key_above` or `config.key_below`.
