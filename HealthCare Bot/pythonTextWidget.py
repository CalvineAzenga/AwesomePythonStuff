# File: textstyles.py
# References:
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//text.html
#    http://www.tcl.tk/man/tcl8.5/TkCmd/text.htm
#    http://manning.com/grayson/
from tkinter import *
from tkinter import ttk
# from demopanels import SeeDismissPanel
class StyledTextDemo(ttk.Frame):
    def __init__(self, isapp=True, name='textstylesdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Styled Text Demo')
        self.isapp = isapp
        self._create_widgets()
    def _create_widgets(self):
        if self.isapp:
            pass
            # don't need message panel
            # SeeDismissPanel(self)
        self._create_demo_panel()
    def _create_demo_panel(self):
        # create scrolled text widget
        txtFrame = ttk.Frame(self)
        txtFrame.pack(side=TOP, fill=BOTH, expand=Y)
        text = Text(txtFrame, height=30, setgrid=True, wrap=WORD,
                    undo=True, pady=2, padx=3)
        xscroll = ttk.Scrollbar(txtFrame, command=text.xview, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(txtFrame, command=text.yview, orient=VERTICAL)
        text.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        # position in frame and set resize constraints
        text.grid(row=0, column=0, sticky=NSEW)
        yscroll.grid(row=0, column=1, sticky=NSEW)
        txtFrame.rowconfigure(0, weight=1)
        txtFrame.columnconfigure(0, weight=1)
        # configure styles
        self._config_styles(text)
        # add text to scrolled text widget
        self._insert_txt(text)
    def _config_styles(self, twid):
        # font styles
        family = 'Courier'      # font family
        twid.tag_configure('bold', font=(family, 12, 'bold', 'italic'))
        twid.tag_configure('big', font=(family, 14, 'bold'))
        twid.tag_configure('verybig', font=('Helvetica', 24, 'bold'))
        twid.tag_configure('tiny', font=('Times', 8, 'bold'))
        twid.tag_configure('underline', underline='on')
        twid.tag_configure('overstrike', overstrike='on')
        twid.tag_configure('super', offset='4p', font=(family, 10))
        twid.tag_configure('sub', offset='-2p', font=(family, 10))
        # foreground/background styles
        twid.tag_configure('bgstipple', background='black',
                           borderwidth=0, bgstipple='gray12')
        twid.tag_configure('fgstipple', foreground='blue', fgstipple='gray50')
        twid.tag_configure('color1', background='#a0b7ce')
        twid.tag_configure('color2', foreground='red')
        twid.tag_configure('raised', relief=RAISED, borderwidth=1)
        twid.tag_configure('sunken', relief=SUNKEN, borderwidth=1)
        # margins, spacing, and alignment
        twid.tag_configure('right', justify='right')
        twid.tag_configure('center', justify='center')
        twid.tag_configure('margins', lmargin1='12m', lmargin2='6m',
                           rmargin='10m')
        twid.tag_configure('spacing', spacing1='10p', spacing2='2p',
                           lmargin1='12m', lmargin2='6m', rmargin='10m')
    def _insert_txt(self, twid):
        # Intro
        txt = ["Text widgets like this one allow you to display ",
               "information in a variety of styles.  Display ",
               "styles are controlled using a mechanism called "]
        twid.insert(END, ''.join(txt))
        twid.insert(END, 'tags. ', 'bold')
        txt = ["\n\nTags are just textual names that you can apply to one ",
               "or more ranges of characters within a text widget.  ",
               "You can configure tags with various display styles. ",
               "If you do this, then the tagged characters will be ",
               "displayed with the styles you choose.  The available ",
               "display styles are:\n"]
        twid.insert(END, ''.join(txt))
        #1. Font
        twid.insert(END, '\n1. Font - ', 'big')
        twid.insert(END, 'You can choose any system font, ')
        twid.insert(END, 'large ', 'verybig')
        twid.insert(END, 'or ')
        twid.insert(END, 'small.', 'tiny')
        #2. Color
        twid.insert(END, '\n2. Color - ', 'big')
        twid.insert(END, 'You can change either the ')
        twid.insert(END, 'background', 'color1')
        twid.insert(END, ', or ')
        twid.insert(END, 'foreground ', 'color2')
        twid.insert(END, 'color, or ')
        twid.insert(END, 'both.', ('color1', 'color2'))
        #3. Stippling
        twid.insert(END, '\n3. Stippling - ', 'big')
        twid.insert(END, 'You can cause either the ')
        twid.insert(END, 'background', 'bgstipple')
        twid.insert(END, ' or ')
        twid.insert(END, 'foreground ', 'fgstipple')
        twid.insert(END, 'text to be drawn with a stipple fill ')
        twid.insert(END, 'instead of a solid fill.')
        #4. Underlining
        twid.insert(END, '\n4. Underlining - ', 'big')
        twid.insert(END, 'You can ')
        twid.insert(END, 'underline', 'underline')
        twid.insert(END, ' a range of text.')
        #5. Overstrikes
        twid.insert(END, '\n5. Overstrikes - ', 'big')
        twid.insert(END, 'You can ')
        twid.insert(END, 'draw a line through', 'overstrike')
        twid.insert(END, ' a range of text.')
        #6. 3D Effects
        twid.insert(END, '\n6. 3D Effects - ', 'big')
        twid.insert(END, 'You can arrange for the background ')
        twid.insert(END, 'to be drawn with a border that makes ')
        twid.insert(END, 'the characters appear either ')
        twid.insert(END, 'raised', 'raised')
        twid.insert(END, ' or ')
        twid.insert(END, 'sunken.', 'sunken')
        #7. Justification
        twid.insert(END, '\n7. Justification - ', 'big')
        twid.insert(END, 'You can arrange for lines to be ')
        twid.insert(END, 'displayed left-justified\n')
        twid.insert(END, 'right-justified, or\n', 'right')
        twid.insert(END, 'centered.', 'center')
        #8. Superscripts and subscripts
        twid.insert(END, '\n8. Superscripts and subscripts - ', 'big')
        twid.insert(END, 'You can control the vertical position of text ')
        twid.insert(END, 'to display superscript effects like 10')
        twid.insert(END, 'n', 'super')
        twid. insert(END, ' or subscript effects like x')
        twid.insert(END, 'i', 'sub')
        twid.insert(END, '.')
        #9. Margins
        twid.insert(END, '\n9. Margins - ', 'big')
        twid.insert(END, 'You can control the amount of space ')
        twid.insert(END, 'on each side of the displayed text:\n')
        twid.insert(END, "This paragraph is an example of the use of ", 'margins')
        twid.insert(END, "margins.  It consists of a single line of text ", 'margins')
        twid.insert(END, "that wraps around on the screen.  There are two ", 'margins')
        twid.insert(END, "separate left margin values, one for the first ", 'margins')
        twid.insert(END, "display line associated with the text line, ", 'margins')
        twid.insert(END, "and one for the subsequent display lines, which ", 'margins')
        twid.insert(END, "occur because of wrapping.  There is also a ", 'margins')
        twid.insert(END, "separate specification for the right margin, ", 'margins')
        twid.insert(END, "which is used to choose wrap points for lines.\n", 'margins')
        #10. Spacing
        twid.insert(END, '\n10. Spacing - ', 'big')
        twid.insert(END, " You can control the spacing of lines with three\n")
        twid.insert(END, "separate parameters.  \"Spacing1\" tells how much ")
        twid.insert(END, "extra space to leave\nabove a line, \"spacing3\" ")
        twid.insert(END, "tells how much space to leave below a line,\nand ")
        twid.insert(END, "if a text line wraps, \"spacing2\" tells how much ")
        twid.insert(END, "space to leave\nbetween the display lines that ")
        twid.insert(END, "make up the text line.\n")
        twid.insert(END, "These indented paragraphs illustrate how spacing ", 'spacing')
        twid.insert(END, "can be used.  Each paragraph is actually a ", 'spacing')
        twid.insert(END, "single line in the text widget, which is ", 'spacing')
        twid.insert(END, "word-wrapped by the widget.\n", 'spacing')
        twid.insert(END, "Spacing1 is set to 10 points for this text, ", 'spacing')
        twid.insert(END, "which results in relatively large gaps between ", 'spacing')
        twid.insert(END, "the paragraphs.  Spacing2 is set to 2 points, ", 'spacing')
        twid.insert(END, "which results in just a bit of extra space ", 'spacing')
        twid.insert(END, "within a pararaph.  Spacing3 isn't used ", 'spacing')
        twid.insert(END, "in this example.\n", 'spacing')
        twid.insert(END, "To see where the space is, select ranges of ", 'spacing')
        twid.insert(END, "text within these paragraphs.  The selection ", 'spacing')
        twid.insert(END, "highlight will cover the extra space.", 'spacing')
if __name__ == '__main__':
    StyledTextDemo().mainloop()
