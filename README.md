## The Tictactoe case study for UŁ WMII's AI lecture


#### #PRESENTATION AGENDA:
 1. &nbsp; about titactoe:&nbsp; *zero-sum game, 19683 states, 255168 gameplays (=solved)*
 2. &nbsp; board state epresentation:&nbsp; *9 elem table with numeric keyboard api*
 3. &nbsp; implemented agents:&nbsp; *minmax, random, human and custom<sup>TM</sup>*
 4. &nbsp; (?) code & baseline algorithms inspection&nbsp;
 5. &nbsp; presenting own rule-based agent idea
 6. &nbsp; gaming session:&nbsp; *single & tournament modes*


#### #N=1000 SUMULATIONS:
  <pre>
  time      X-player         win   draw   loss    O-player 
  (05:47) &#8594; Minmax agent --    0 : 1000 :    0 -- Minmax agent
  (01:02) &#8594; Random agent --  563 :  144 :  293 -- Random agent
  (00:37) &#8594; Custom agent --   42 :  951 :    7 -- Custom agent
  (00:37) &#8594; Custom agent --    0 :  978 :   22 -- Minmax agent
  (00:37) &#8594; Minmax agent --  206 :  794 :    0 -- Custom agent
  (00:00) &#8594; Custom agent --  866 :  118 :   16 -- Random agent
  (00:00) &#8594; Random agent --   55 :  197 :  748 -- Custom agent
  (00:36) &#8594; Minmax agent --  954 :   46 :    0 -- Random agent
  (05:05) &#8594; Random agent --    0 :  216 :  784 -- Minmax agent</pre>


#### #TICTACTOE TREE DEPTH:
<img src="./xkcd_xo.png" alt="XKCD" width="500">

[*source XKCD*](https://xkcd.com/832/)


#### #RESOURCES:
  - https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
  - https://en.wikipedia.org/wiki/Tic-tac-toe
  - https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/