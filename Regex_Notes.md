# Regex notes in Python

## Matching chars in a sequence with random insertions
**—The `lookahead`** (copied from a great [post](https://stackoverflow.com/questions/10828118/how-to-match-required-characters-in-random-order-using-regular-expression) 
by user [Andreas Wong](https://stackoverflow.com/users/135448/andreas-wong) in response to a question by user [flowfree](https://stackoverflow.com/users/1396314/flowfree))

The questioner asked:
> I need to match text which has `@`, `#`, and any number in it. The characters can be in random position as long as they are in the text. Given this input:
> `abc@#d9`
> `a9b#c@d`
> `@@abc#9`
> `abc9d@@`
> `a#b#c@d`
> The regex should match the first 3 lines....

Andreas Wong responded with the expression `/(?=.*@)(?=.*#)(?=.*[0-9]).*/`. He goes on to explain it thusly:
> The regex is basically using what they call `lookahead`. [http://www.regular-expressions.info/lookaround.html](http://www.regular-expressions.info/lookaround.html)
> A simple case from the link above is trying to match q, followed by u, by doing q(?=u), that's why it's called lookahead, it finds q followed by u ahead.
>
> Let's take one of your valid case: a9b#c@d
>
> The first lookahead is `(?=.*@)`, which states: Match anything, followed by a `@`. So it does, which is the string `a9b#c`, then since the match from the lookahead 
> must be discarded, the engine steps back to the start of the string, which is an a. Then it goes to `(?=.*#)`, which states: Match anything that is followed 
> by `#`, then it finds it at `a9b`. etc. The difference between using lookahead and `(a)(b)(c)` is basically the stepping back.

### My conclusions
Negative lookahead matches something NOT followed by something else, while positive lookahead matches something that IS followed by something else. 

**The biggest advantage to lookaheads is that they can match something followed by something else without returning that something else.**

Consider the strings "quiet," "acquitted," and "quasar" and we'll apply different regex to them to see what happens.

#### The regex `/q(?=t)/`...
This expression is the easiest. It will return any `q` that is immediately followed by a `t`, but will not include the `t`. Unfortunately, none of our 
test strings would match this pattern.

#### The regex `/q(?=.*t)/`
This expression will return:
- `q` in _quiet_
- `q` in _acquitted_
- nothing from _quasar_

#### The regex `/q.*(?=t)/`... 
The expression matches `q` followed by any characters as long as the sequence ends with a `t`. Considering the three test words mentioned, there are matches for:
- `quie` in _quiet_
- `quit in _acquitted_
Notice how the first of the two _t_'s  in _acquitted_ is included in its match. That is because in Python, regex are greedy by default. If, however, 
you add a `?` after the `.*` wildcard (making the expression to be `/q.*?(?=t)/`, Python will try to find the shortest match instead. In this circumstance, the `quie` 
in _quiet_ will still match, but the match in _acquitted_ is now `qui` instead of `quit`. 
