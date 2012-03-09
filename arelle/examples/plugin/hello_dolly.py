'''
Hello dolly is a simple "Hello world" to demonstrate how plugins
are written for Arelle

(c) Copyright 2012 Mark V Systems Limited, All rights reserved.
'''
from random import randint


LYRICS =  ["I said hello, dolly,......well, hello, dolly", \
            "It's so nice to have you back where you belong ", \
            "You're lookin' swell, dolly.......i can tell, dolly ", \
            "You're still glowin'...you're still crowin'...you're still goin' strong ", \
            "I feel that room swayin'......while the band's playin' ", \
            "One of your old favourite songs from way back when ", \
            "So..... take her wrap, fellas.......find her an empty lap, fellas ", \
            "Dolly'll never go away again" 
            ]

def randomLyric():
    ''' A random lyrics.'''
    return LYRICS[randint(0, len(LYRICS) - 1)]
        
def helloMenuEntender(cntlr, menu):
    menu.add_cascade(label="Hello Dolly", underline=0, command=lambda: helloMenuCommand(cntlr, "Hello Dolly") )

def helloMenuCommand(cntlr, label):
    hello_dolly = randomLyric();
    cntlr.addToLog(hello_dolly)
    import tkinter
    tkinter.messagebox.showinfo(label, hello_dolly, parent=cntlr.parent)            

def helloCommandLineOptionExtender(parser):
    parser.add_option("--hello_dolly", 
                      action="store_true", 
                      dest="hello_dolly", 
                      help=_('Print a random lyric from "Hello, Dolly"'))

def helloCommandLineXbrlRun(cntlr, options, modelXbrl):
    if options.hello_dolly:
        hello_dolly = randomLyric();
        try:
            modelXbrl.info("info", hello_dolly)
        except:
            print(hello_dolly)


__pluginInfo__ = {
    'name': 'Hello Dolly',
    'version': '0.9',
    'description': "This is not just a plugin, it symbolizes the hope and enthusiasm "
					"of an entire generation summed up in two words sung most famously "
					"by Louis Armstrong: Hello, Dolly. When activated you will randomly "
					"see a lyric from Hello, Dolly.",
    'license': 'Apache-2',
    'author': 'R\u00e9gis D\u00e9camps',
    'copyright': '(c) Copyright 2012 Mark V Systems Limited, All rights reserved.',
    # classes of mount points (required)
    'CntlrWinMain.Menu.Tools': helloMenuEntender,
    'CntlrCmdLine.Options': helloCommandLineOptionExtender,
    'CntlrCmdLine.Xbrl.Run': helloCommandLineXbrlRun,
}
