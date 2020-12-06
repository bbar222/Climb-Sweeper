Climb-Sweeper
-----


Controls:
Left click to clear tile, right click to flag tile. Don't click on the mines, numbered tiles show how many mines are nearby in a 3x3 area.


-----
Struggles I encountered during the project: <br>
I have never used pygame before, but have played complex games before that have used pygame and looked very cool, so I decided to try and learn it here. It was simple enough at first, but my first big conflict arose when I was about halfway done. I realized that I built my whole project from a starting point of a ball bouncing around on a screen, since I was following a tutorial on how to display images on the screen. It was not helpful to build the rest of the project from this skeleton, as each tile of the minesweeper board was its own object I had to create manually in a loop.
The biggest drawback to this was it would:
<br><br>
  A: Be impossible to make the board 'truly' infinite, as I can't just put the board creation in a while loop, and I cannot make new rows on-demand because I would need information from the previous and the next rows in order to properly display the number of mines surrounding the tiles, which could potentially make previous rows inaccurately display what the tiles above itself contain.
<br><br>
  B: Due to my inexperience with object-oriented-programming, I do not think it is possible (with how I had designed the board engine) to auto-clear surrounding zeroes, since each tile was stored as an individual object, and I couldn't figure out how to tell another object to reveal itself because a nearby object was clicked. 
<br><br>
  C: Because I started with no knowledge and that beginner tutorial, I thought I could make tiny adjustments to how an objects velocity is changed. It turns out you cannot adjust a rect object in pygame by a float value, so I could only traverse the screen in integer values. 
  Unfortunately, moving at 1 pixel per tick was already much to fast for the climbsweeper board to be going, and this was the slowest option. My only workaround was to slow down the tick speed of the game, so that when the game is moving slower, the actually runs at a lower framerate than if the board was moving fast. This is what made me the most sad. Almost as sad as the quality of the presentation video on youtube, because I am a computer science man and not a video man, so I couldn't make it as good as I wanted to with free software. 
<br><br>
However, I found it funny that my commit history for this project is similar a bell-curve over the course of two weeks because of that big issue I encountered in the middle of the project: each tiny step forward, as well as backward, was a success to me and I found it reasonable to save then.



-----
Video Link

https://youtu.be/y4z7p1e0Ato 



-----





Credits:
All images made by me (Brian) <br>
Sounds are manually altered windows 10 alert sounds <br>


