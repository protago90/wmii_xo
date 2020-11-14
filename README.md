## The Tictactoe case study for UŁ WMII's AI lecture

---
### #Demo program:
 1. &nbsp; about titactoe:&nbsp; *zero-sum game, 19683 states, 255168 gameplays (=solved)*
 2. &nbsp; board state internal representation:&nbsp; *basic 9 elem table with numeric keyboard api*
 3. &nbsp; implemented agents:&nbsp; *'minmax', 'random', 'human' and 'customTM'*
 4. &nbsp; (?) code & baseline algorithms inspection&nbsp;
 5. &nbsp; presenting your own rule-based agent idea
 6. &nbsp; gaming session&nbsp; *single & tournament modes*

---
### #Simulations:
  - n=1000 &nbsp;&nbsp; t=05:47 &#8594; "X" Minmax agent --      0 :   1000 :      0 -- "O" Minmax agent
  - n=million           t=01:02 &#8594; "X" Random agent -- 585302 : 126922 : 287776 -- "O" Random agent
  - n=1000 &nbsp;&nbsp; t=00:36 &#8594; "X" Minmax agent --    954 :     46 :      0 -- "O" Random agent
  - n=1000 &nbsp;&nbsp; t=05:05 &#8594; "X" Random agent --      0 :    216 :    784 -- "O" Minmax agent

---
### #Moves tree:
<img src="./xkcd_xo.png" alt="XKCD" width="500">

[*source XKCD*](https://xkcd.com/832/)

---
### #Resources:
  - https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
  - https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/