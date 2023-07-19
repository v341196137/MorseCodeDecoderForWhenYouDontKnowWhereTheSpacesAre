# MapMaker
Script to make CS 246 a little bit easier.  
## Installation
Run `pip -r requirements.txt` or `pip3 -r requirements.txt`
## Usage
There are key bindings for drawing each aspect of the room. Use the mouse to draw stuff.
|Key|Feature|
|-|-|
|R|Draws a room (supports dragging and dropping a rectangle)|
|P|Draws a passage `#` (must click each individual part)|
|D|Draws a door `+` (must click each individual part)|
|E|Draws empty space ` ` (supports dragging and dropping a rectangle)|
|V|Draws a vertical wall `|` (must click each individual part)|
|H|Draws a horizontal wall `-` (must click each individual part)|
|I|Draws an inside the room character `.` (must click each individual part)|
Upon quitting the program, the program will output the map to a file called `world.txt`.

Here are some examples:
![](https://media.discordapp.net/attachments/1106008270302359643/1131287705129603142/image.png)
![](https://media.discordapp.net/attachments/1106008270302359643/1131289551772586104/image.png)
