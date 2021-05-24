import os
# import easygui as g
import streamlit as st
import wx


currdir = os.getcwd()
title = 'Choose your image'
# class ImageFile:
#     def __init__(self):
#         super().__init__()
#         self.fname = None
    
def get_path():
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.STAY_ON_TOP
    wildcard =  "pictures (*.jpg;*.bmp)|*.jpg; *.bmp | png files (*.png)| *.png"
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path
    
def load_file():
    # obj = ImageFile()
    # obj.fname = obj.get_path()
    image_file = get_path()
    if image_file == None:
        return
    else:
        return image_file
    
x = None

