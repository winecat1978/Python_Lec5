#from isOdd import isOdd
#print(isOdd(1)) 
#print(isOdd(4))

#from progress.bar import Bar
#import time
#bar = Bar('Processing', max=10)
#for i in range(10):
#    time.sleep(2)
#    bar.next()
#bar.finish() 

#import emoji
#print(emoji.emojize('Python is :thumbs_up:'))

#import matplotlib.pyplot as plt
#import numpy as np
#list = [1,2,3,2,7]
#plt.plot(list)
#plt.show()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token('5552127770:AAHt_ib8rm6AjOqcErAxZdjBqr57jJaegLU').build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print("server start")
app.run_polling()