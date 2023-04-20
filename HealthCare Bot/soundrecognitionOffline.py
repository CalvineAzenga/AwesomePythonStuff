# from win32com.client import constants
# import win32com.client
# import pythoncom
# phrase="""Sample code for using the Microsoft Speech SDK 5.1 via COM in Python.
#     Requires that the SDK be installed (it's a free download from
#             http://www.microsoft.com/speech
#     and that MakePy has been used on it (in PythonWin,
#     select Tools | COM MakePy Utility | Microsoft Speech Object Library 5.1).
#     After running this, then saying "One", "Two", "Three" or "Four" should
#     display "You said One" etc on the console. The recognition can be a bit
#     shaky at first until you've trained it (via the Speech entry in the Windows
#     Control Panel."""

# class SpeechRecognition:
#     """ Initialize the speech recognition with the passed in list of words """
#     def __init__(self, wordsToAdd):
#         # For text-to-speech
#         self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         print(self.speaker)
#         # For speech recognition - first create a listener
#         self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
#         # Then a recognition context
#         self.context = self.listener.CreateRecoContext()
#         # which has an associated grammar
#         self.grammar = self.context.CreateGrammar()
#         # Do not allow free word recognition - only command and control
#         # recognizing the words in the grammar only
#         self.grammar.DictationSetState(0)
#         # Create a new rule for the grammar, that is top level (so it begins
#         # a recognition) and dynamic (ie we can change it at runtime)
#         self.wordsRule = self.grammar.Rules.Add("wordsRule",constants.SRATopLevel + constants.SRADynamic, 0)
#         # Clear the rule (not necessary first time, but if we're changing it
#         # dynamically then it's useful)
#         self.wordsRule.Clear()
#         # And go through the list of words, adding each to the rule
#         [ self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd ]
#         # Set the wordsRule to be active
#         self.grammar.Rules.Commit()
#         self.grammar.CmdSetRuleState("wordsRule", 1)
#         # Commit the changes to the grammar
#         self.grammar.Rules.Commit()
#         # And add an event handler that's called back when recognition occurs
#         self.eventHandler = ContextEvents(self.context)
#         # Announce we've started
#         self.say("Started successfully")
#         """Speak a word or phrase"""
#     def say(self, phrase):
#         self.speaker.Speak(phrase)
# """The callback class that handles the events raised by the speech object.
#     See "Automation | SpSharedRecoContext (Events)" in the MS Speech SDK
#     online help for documentation of the other events supported. """
# class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
# # """Called when a word/phrase is successfully recognized  -
# # ie it is found in a currently open grammar with a sufficiently high
# # confidence"""
#     def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
#         newResult = win32com.client.Dispatch(Result)
#         print("You said: ",newResult.PhraseInfo.GetText())
# if __name__=='__main__':
#     wordsToAdd = [ "One", "Two", "Three", "Four" ]
#     speechReco = SpeechRecognition(wordsToAdd)
#     while 1:
#         pythoncom.PumpWaitingMessages()

# Press CTRL + ENTER to run a single line in the console
print('Welcome to Rodeo!')

# Press CTRL + ENTER with text selected to run multiple lines
# For example, select the following lines
x = 7
x**2
# and remember to press CTRL + ENTER

# Here is an example of using Rodeo:

# Install packages

# ! pip install pandas
# ! pip install numpy

# Import packages

import numpy as np
import pandas as pd

N = 100
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })
df.head()

# Another example of making a plot:

from matplotlib import pyplot as plt
x=df.x
with plt.style.context('fivethirtyeight'):
    plt.plot(x, np.sin(x*5) + x + np.random.randn(N)*15)
    plt.plot(x, np.sin(x*5) + 0.5 * x + np.random.randn(N)*5)
    plt.plot(x, np.sin(x) + 2 * x + np.random.randn(N)*20)

plt.title('Random lines')
plt.show()


