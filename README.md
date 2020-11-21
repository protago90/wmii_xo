## The Tictactoe case study for UŁ WMII's AI lecture


#### #PRESENTATION AGENDA:
 1. &nbsp; about titactoe:&nbsp; *zero-sum game, 19683 states, 255168 gameplays (=solved)*
 2. &nbsp; board state epresentation:&nbsp; *9 elem table with numeric keyboard api*
 3. &nbsp; implemented bots:&nbsp; *minmax, random, human and custom<sup>TM</sup>*
 4. &nbsp; (?) code & baseline algorithms inspection&nbsp;
 5. &nbsp; presenting own rule-based bot idea
 6. &nbsp; gaming session:&nbsp; *single & tournament modes*


#### #N=1000 SUMULATIONS:
  <pre>
  time       X-player      win  draw  loss    O-player
# -----------------------------------------------------
  (--:59) &#8594;  Minmax bot --   0 : 100 :   0 -- Minmax bot
  (--:-0) &#8594;  Random bot --  63 :  14 :  23 -- Random bot
  (--:-0) &#8594;  Debuts bot --  10 :  87 :   3 -- Debuts bot
  (--:58) &#8594;  Custom bot --  38 :  51 :  11 -- Custom bot
# -----------------------------------------------------
  (-1:02) &#8594;  Custom bot --   0 :  82 :  18 -- Minmax bot
  (--:59) &#8594;  Minmax bot --  77 :  23 :   0 -- Custom bot
  (--:09) &#8594;  Custom bot --  88 :  10 :   2 -- Random bot
  (--:52) &#8594;  Random bot --   7 :  18 :  75 -- Minmax bot
  (--:08) &#8594;  Custom bot --  17 :  77 :   6 -- Debuts bot
  (--:52) &#8594;  Debuts bot --  25 :  46 :  29 -- Custom bot</pre>


#### #TICTACTOE TREE DEPTH:
<img src="./xkcd_xo.png" alt="XKCD" width="550">

[*source XKCD*](https://xkcd.com/832/)


#### #RESOURCES:
  - https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
  - https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/