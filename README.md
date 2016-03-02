# tvcs
Tag-Value Comms System - Python driven multithread communicator

## Workshop Instructions
- Go into `modules` folder.
- Make copy of `Template.py`. Rename the copy to `OpenCV.py`.
- Make one more copy of `Template.py`. Name it `Servo.py`.
- Make one more copy of `Template.py`. Name it `Sound.py`.
- Let's add new modules to tvcs. Open `ModuleList.py`. Change its contents to:
```

fromSource = [
    "OpenCV",
    "Servo",
    "Sound"
]

fromClass = [
]

```
- Let's define tags and their default outputs. In `OpenCV.py`, inside `init` function add line `self.registerOutput("facePos", Obj("x", 0, "y", 0))`
- Similarly, in `Servo.py`, add `self.registerOutput("servo", Obj("moving", False))`
- Similarly, in `Sound.py`, add `self.registerOutput("audio", Obj("playing", False))`
- Now, let's define behaviour. In `OpenCV.py` we want to output x and y that switches between (10, 10) and (-10, -10). Take note of `self.output("facePos", Obj("x", xPos, "y", yPos))`.
```
def run (self):
    # put your init and global variables here
    xPos = 10
    yPos = 10

    # main loop
    while 1:
        # put your logic here
        # you can use: output, getInputs, message 
        self.output("facePos", Obj("x", xPos, "y", yPos))
        xPos *= -1
        yPos *= -1

        # if you want to limit framerate, put it at the end
        time.sleep(3)
```
- In `Servo.py` we want to read OpenCV's output. It used `facePos` tag and that's what we are going to use to retrieve the data. Based on that, we are going to output `moving` as True when x > 0 and False when x <= 0. Take note of `facePos = self.getInputs().facePos` and `facePos.x`
```
def run (self):
    # put your init and global variables here
    moving = False

    # main loop
    while 1:
        # put your logic here
        # you can use: output, getInputs, message 
        facePos = self.getInputs().facePos
        if (facePos.x > 0): moving = True
        else: moving = False

        self.output("servo", Obj("moving", moving))

        # if you want to limit framerate, put it at the end
        time.sleep(1)
```
- In `Sound.py` we want to output `playing` as True when servo is moving. In this case code will be similar to Servo code.
```
def run (self):
    # put your init and global variables here
    playing = False

    # main loop
    while 1:
        # put your logic here
        # you can use: output, getInputs, message 
        servo = self.getInputs().servo

        if (servo.moving): playing = True
        else: playing = False

        self.output("audio", Obj("playing", playing))

        # if you want to limit framerate, put it at the end
        time.sleep(0.5)
```
- Let's say we would like to write to the console when face position x < 0. Put this line after `self.output` in `OpenCV.py`
```
if (xPos < 0): self.message("face is in negative x!")
```
- type in `python main.py -debug` to run this setup.