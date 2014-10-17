#! /usr/bin/env python
#coding=utf-8
from Tkinter import *
 
class LabelDemo( Frame ):
   """Demonstrate Labels"""
    
   def __init__( self ):
      """Create three Labels and pack them"""
       
      Frame.__init__( self )   # initializes Frame instance
 
     
def main():
   LabelDemo().mainloop()  # starts event loop
 
if __name__ == "__main__":
   main()