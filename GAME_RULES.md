# Game Rules

Very simple game, yet so much fun.

In the beginning, program generates a 3x3 square with 9 cards.

Also, the card on top (obviously hidden) is generated. Your goal is very simple:

> To guess is the card on top higher/lower than one of the cards from the square.

Let's say you have this situation:

```txt
A ◆     Q ♣     6 ♣

10 ♣     2 ♠     K ❤

10 ❤     6 ♠     3 ♣
```

You'd like to check the card on top against a **Q ♣**.

You decided that the card on top is going to be smaller.

You can do so by inputting **Q j** (or however you did bind the `config.key_below`).

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

Now you guess like usually, but:

> [!NOTE]
> If you guess the card on the square, you are entitled to open a new pile.

Doesn't matter, whether the guess was with `config.key_above` or `config.key_below`.

If all of them were already opened, new, (n+1)th tile is being created.
If one of them is closed, that's the one that is automatically being opened.
If two or more, you can choose from the list by typing the pile number.

But there's a catch!

We have this situation:

```txt
A ◆     4 ♣     6 ♣

10 ♣     2 ♠     2 ❤

10 ❤     6 ♠     3 ♣

Guess: 10 j
```

I decided to guess lower than 10. However:

```txt
A ◆     4 ♣     6 ♣

10 ♣     2 ♠     2 ❤

10 ❤     6 ♠     3 ♣

Guess: 10 j
You lost!
The card was J ❤

40 left in the deck

A ◆     4 ♣     6 ♣

XX     2 ♠     2 ❤

10 ❤     6 ♠     3 ♣
```

As you see, the pile with 10 was closed with J on top.

> [!CAUTION]
> Incorrect guess closes the pile. Play carefully!

So, the goal is simple: **to survive to the end with at least one pile open**.

## Good luck and have fun!
