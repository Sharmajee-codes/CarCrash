import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\36474\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\36474\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"



executables = [cx_Freeze.Executable("Game.py")]
cx_Freeze.setup(
    name = "Car Crash",
    
    options = {"build_exe":{"packages" :["pygame"],
                             "include_files":["car.png","Resume.png","invResume.png","lambo.png","music.mp3","accel.wav","boom.png","break.wav","crash.wav","Intro.jpg","exitgame.png","invexitgame.png","playgame.png","invplaygame.png","Polcar.png","road.png"]
                             }
                },
    executables = executables
    )
