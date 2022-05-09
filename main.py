import tkinter as tk
from tkinter import  ttk
from translate import  Translator
from PIL import ImageTk, Image

#proframm info
appTitle = "DoubleText"
appVersion = 0.1
author = "Roshchenyuk Vladislav."
devDate = "01/01/2022"
about = "Translator App for Windows."

#main window
win = tk.Tk()
loadtime = 2000

#window settings
win_width = 400
win_height = 550
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_coord = (screen_width/2)-(win_width/2)
y_coord = (screen_height/2)-(win_height/2)
win.geometry("%dx%d+%d+%d"%(win_width, win_height, x_coord, y_coord))
global redirectValue
win.overrideredirect(1)

#font settings
calibriFont = ('Calibri', 12, )
consoleFont = ('Consolas', 12, )
arialFont = ('Arial', 12, )
font1 = ('Calibri (Body)', 14, 'bold')
font2 = ('Calibri (Body)', 18, 'bold')
font5 = ('Calibri (Body)', 28, 'bold')
font6 = ('Calibri (Body)', 20)

#color settings
red = "#cf4444"
white = "#ffffff"
black = "#000000"
blue = "#7cbcff"
green = "#57ff89"
yellow = "#f8ff8f"
orange = "#ffc044"
sahara = "#faeece"
mint = "#3fffd9"
sonder = "#613400"
nardo = "#828282"
magenta = "#cb25b5"

colourList = [red, white, black, blue, green, yellow, orange, sahara, mint, sonder, nardo, magenta]

#lang
languagesList = ["English", "Ukrainian", "Spanish", "Brasilian", "Romanian", "Italian", "Hungarian", "Japaneese", "France","Polish"]

#images
var1 = tk.StringVar()
logo = ImageTk.PhotoImage(Image.open('staticfiles/logo.png'))
YTImage = ImageTk.PhotoImage(Image.open("staticfiles/Yt.png"))
FBImage = ImageTk.PhotoImage(Image.open("staticfiles/Face.png"))
InstImage = ImageTk.PhotoImage(Image.open("staticfiles/inst.png"))
ResizeResult = ImageTk.PhotoImage(Image.open("staticfiles/ResizeRes.png"))

#Console log
logList=["started App","Opened main page"]

#startFrame
def startFrame():
    global frame
    frame = tk.Frame(win, bg=red)
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)
    #startScreen settings

    #title
    title1 = tk.Label(frame, bg=red, fg=white, text="Double", font=font5)
    title1.place(relx=0.25, rely=0.05, relwidth=0.35, relheight=0.1)
    title2 = tk.Label(frame, bg=red, fg=white, text="Text", font=font6, anchor=tk.W)
    title2.place(relx=0.6, rely=0.05, relwidth=0.2, relheight =0.1)

    #logo
    logoFrame = tk.Label(frame, bg=red, image=logo)
    logoFrame.place(relx=0.05, rely=0.15, relheight=0.7, relwidth=0.9)

    #loading bar
    loadText = tk.Label(frame, bg=red,fg=white, text="Loading", font=font5)
    loadText.place(relx=0.3, rely=0.835, relwidth=0.4, relheight=0.08 )

    #loading status
    global statusFrame
    statusFrame = tk.Frame(frame, bg= red)
    statusFrame.place(relx = 0.3, rely = 0.93, relwidth = 0.4, relheight = 0.08)
    indicator1 = tk.Frame(statusFrame, bg = white)
    indicator2 = tk.Frame(statusFrame, bg=white)
    indicator3 = tk.Frame(statusFrame, bg=white)

    indicator1.place(relx = 0.15, rely = 0.3, relwidth = 0.2, relheight = 0.3)
    indicator2.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.3)
    indicator3.place(relx=0.65, rely=0.3, relwidth=0.2, relheight=0.3)
    win.after(30, mainWindow)

#loadcyce



#main window
def mainWindow():
    frame.destroy()
    logList.append("Opened Main Screen")
    global mainFrame
    mainFrame = tk.Frame(win, bg = red)
    mainFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    mainFrame.bind("<Map>", frame_mapped)

    #upper line
    controlFrame = tk.Frame(mainFrame, bg = red)
    controlFrame.place(relx = 0, rely = 0, relwidth  = 1, relheight = 0.08)

    #controls
    global openMenuBtn
    openMenuBtn = ImageTk.PhotoImage(Image.open("staticfiles/showMenu.png"))
    menuBtn = tk.Button(controlFrame, bg = red, image =openMenuBtn ,bd =0, activebackground = red,command = openMenu)
    menuBtn.place(relx = 0.01, rely = 0.1, relwidth = 0.1, relheight = 0.8)

    global hideWinBtn
    hideWinBtn = ImageTk.PhotoImage(Image.open("staticfiles/tray.png"))
    global closeAppBtn
    closeAppBtn = ImageTk.PhotoImage(Image.open("staticfiles/closeApp.png"))

    hideBtn = tk.Button(controlFrame, bg = red,image = hideWinBtn,bd = 0,activebackground = black ,command = hide_window)
    hideBtn.place(relx = 0.8, rely = 0.12, relwidth = 0.09, relheight = 0.75)
    closeBtn = tk.Button(controlFrame, bg=red, image = closeAppBtn,bd = 0,activebackground = black , command=appClose)
    closeBtn.place(relx=0.9, rely=0.12, relwidth=0.09, relheight=0.75)

    def translate():
        InLang = InLangChoise.get()
        InLangFinal  = InLang.lower()
        OutLang = OutLangChoise.get()
        OutLangFinal = OutLang.lower()
        translator = Translator(from_lang = f"{InLangFinal}", to_lang=f'{OutLangFinal}')
        translation = translator.translate(f"{inputvar.get()}")
        print(translation)
        output.insert(0, f"{translation}")
        newline = " \n-"
        #if len(translation) >= 22:
        ##   ''.join([translation[:22] , newline , translation[22:]])

    #main fields
    Title = tk.Label(mainFrame, bg = red, fg = white, text = "DoubleText it!", font= font6)
    Title.place(relx = 0.1, rely=0.12, relheight = 0.09, relwidth = 0.8 )

    #abstract image
    global abstractImage
    abstractImage = ImageTk.PhotoImage(Image.open("staticfiles/abstract.png"))
    abstract = tk.Label(mainFrame, bg = red, fg = white, image = abstractImage)
    abstract.place(relx = 0.1, rely = 0.2, relheight = 0.135, relwidth = 0.8)

    #inputs
    InLangChoise = ttk.Combobox(mainFrame, values = languagesList, font = font1)
    InLangChoise.place(relx=0.1, rely=0.54, relwidth=0.39, relheight=0.09)


    InputFrame = tk.Frame(mainFrame, bg = white)
    InputFrame.place(relx=0.1, rely=0.34, relwidth=0.8, relheight=0.18)
    inputvar = tk.Entry(InputFrame, bg=blue, fg=red, font=font1)
    inputvar.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.4)

    global refreshImage
    refreshImage = ImageTk.PhotoImage(Image.open("staticfiles/refresh.png"))
    #refreshBtn = tk.Button(inputvar, bg=white, fg=white, text="X", font=font6, bd = 0, image = refreshImage, activebackground = white)
    #refreshBtn.place(relx=0.7, rely=0.02, relwidth=0.3, relheight=0.95)

    OutLangChoise = ttk.Combobox(mainFrame, values=languagesList, font=font1)
    OutLangChoise.place(relx=0.51, rely=0.54, relwidth=0.39, relheight=0.09)


    #textarea
    OutputFrame = tk.Frame(mainFrame, bg =white)
    OutputFrame.place(relx = 0.1, rely = 0.65, relwidth = 0.8, relheight = 0.18)
    output = tk.Entry(OutputFrame, bg = blue, fg = red, font = font1)
    output.place(relx = 0.05, rely = 0.1, relwidth = 0.78, relheight = 0.35)

    def resizeOutput():
        global BigOut
        BigOut = tk.Frame(mainFrame, bg = red)
        BigOut.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        buttonsblock = tk.Frame(BigOut, bg = red)
        buttonsblock.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)
        UnresizeBtn = tk.Button(buttonsblock, bg = red, image = ResizeResult, bd = 0, command = unresizeOutput)
        UnresizeBtn.place(relx = 0.85, rely = 0.1, relheight = 0.8, relwidth = 0.12)

        outputVar = output.get()
        try:
            chars_per_line = 20
            for i in range(0, len(outputVar), chars_per_line):
                textVar = outputVar[i: + chars_per_line+ "\n"]
                OutLabel = tk.Label(BigOut, bg=red, fg = white, font = font1, text = f"{textVar}", anchor = tk.NW)
                OutLabel.place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.85)

        except:
            OutLabel = tk.Label(BigOut, bg = red, fg=  white, font = font1, text = "_____________")
            OutLabel.place(relx = 0.05, rely = 0.12, relwidth = 0.9, relheight = 0.85 )

        return BigOut

    def unresizeOutput():
        BigOut.destroy()

    ResizeResultBtn = tk.Button(mainFrame, bg = white, fg = white, image =ResizeResult, bd = 0, command = resizeOutput)
    ResizeResultBtn.place(relx =0.77, rely = 0.66, relwidth = 0.115, relheight= 0.08)



    #translate button
    global translateImage
    translateImage =  ImageTk.PhotoImage(Image.open("staticfiles/TranslateBtn.png"))
    transtaleBtn = tk.Button(mainFrame, bd = 0, bg = red,image = translateImage, font = font6, activebackground = red, command = translate)
    transtaleBtn.place(relx = 0.375, rely = 0.825, relwidth = 0.25, relheight = 0.2)



#menu sidebar
def openMenu():
    logList.append("Opened menu")
    sidebar = tk.Frame(mainFrame, bg = black)
    sidebar.place(relx = 0, rely = 0, relwidth = 0.75, relheight = 1)

    def hideMenu():
        logList.append("Menu Hidden")
        sidebar.destroy()

    global closeimage
    closeimage = ImageTk.PhotoImage(Image.open("staticfiles/close.png"))

    hideSidebarBtn =  tk.Button(sidebar, image = closeimage, command = hideMenu, bd = 0,bg = black , activebackground = black )
    hideSidebarBtn.place(relx = 0.02, rely = 0.01, relheight = 0.06, relwidth = 0.12)

    #effects
    def hover(event):
        settingsbtn.config(bg = red)

    def unhover(event):
        settingsbtn.config(bg=black)


    def hover2(event):
        aboutbtn.config(bg = red)

    def unhover2(event):
        aboutbtn.config(bg=black)


    def hover3(event):
        consolebtn.config(bg = red)

    def unhover3(event):
        consolebtn.config(bg=black)

    def hover4(event):
        feedbackbtn.config(bg = red)

    def unhover4(event):
        feedbackbtn.config(bg=black)

    def hover5(event):
        closebtn.config(bg = red)

    def unhover5(event):
        closebtn.config(bg=black)


    #sidebar buttons
    MenuControls = tk.Frame(sidebar, bg = red)
    MenuControls.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheigh = 0.6)
    #buttons
    settingsbtn = tk.Button(MenuControls, bg = black, fg = white, activebackground = red, activeforeground = white,bd = 0, text = "Settings", font = font2, command = Settings)
    settingsbtn.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
    settingsbtn.bind("<Enter>", hover)
    settingsbtn.bind("<Leave>", unhover)

    aboutbtn = tk.Button(MenuControls, bg=black, fg=white, activebackground=red, activeforeground=white, bd=0,text="About", font=font2, command = About)
    aboutbtn.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)
    aboutbtn.bind("<Enter>", hover2)
    aboutbtn.bind("<Leave>", unhover2)

    consolebtn = tk.Button(MenuControls, bg=black, fg=white, activebackground=red, activeforeground=white, bd=0,text="Console", font=font2, command = Console)
    consolebtn.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)
    consolebtn.bind("<Enter>", hover3)
    consolebtn.bind("<Leave>", unhover3)

    feedbackbtn = tk.Button(MenuControls, bg=black, fg=white, activebackground=red, activeforeground=white, bd=0,text="FeedBack", font=font2, command = FeedBack)
    feedbackbtn.place(relx=0, rely=0.6, relwidth=1, relheight=0.2)
    feedbackbtn.bind("<Enter>", hover4)
    feedbackbtn.bind("<Leave>", unhover4)

    closebtn = tk.Button(MenuControls, bg=black, fg=white, activebackground=red, activeforeground=white, bd=0,text="Close App", font=font2, command = appClose)
    closebtn.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
    closebtn.bind("<Enter>", hover5)
    closebtn.bind("<Leave>", unhover5)




#From menu

#Settings tab
def Settings():
    logList.append("Opened Settings")
    mainFrame.destroy()

    frame = tk.Frame(win, bg = red)
    frame.place(relx = 0, rely = 0, relwidth= 1, relheight = 1)

    controlFrame = tk.Frame(frame, bg=red)
    controlFrame.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    global backImage
    backImage = ImageTk.PhotoImage(Image.open("staticfiles/backToMM.png"))
    backBtn = tk.Button(controlFrame, bg=red,image = backImage, bd=0, activebackground=red, command=mainWindow)
    backBtn.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.8)

    global hideWinBtn
    hideWinBtn = ImageTk.PhotoImage(Image.open("staticfiles/tray.png"))
    global closeAppBtn
    closeAppBtn = ImageTk.PhotoImage(Image.open("staticfiles/closeApp.png"))

    hideBtn = tk.Button(controlFrame, bg=red, image=hideWinBtn, bd=0, activebackground=black, command=hide_window)
    hideBtn.place(relx=0.8, rely=0.12, relwidth=0.09, relheight=0.75)
    closeBtn = tk.Button(controlFrame, bg=red, image=closeAppBtn, bd=0, activebackground=black, command=appClose)
    closeBtn.place(relx=0.9, rely=0.12, relwidth=0.09, relheight=0.75)


    #settings
    settingsFrame = tk.Frame(frame, bg = red)
    settingsFrame.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.75)



    def styling():
        #colour
        colourLabel = tk.Label(settingsFrame, bg = red, fg = white, font = font1, text = "Colour", anchor = tk.W)
        colourLabel.place(relx = 0, rely =0, relwidth = 1, relheight = 0.1)

        choisedColor = tk.Frame(settingsFrame, bg = white)
        choisedColor.place(relx = 0.001, rely = 0.117, relwidth = 0.12, relheight = 0.104)

        currentColour = 0
        colourRelY = 0.125
        colourRelX = 0.01
        for i in range(len(colourList)):
            colorFrame = tk.Button(settingsFrame, bg = colourList[currentColour], bd = 0)
            colorFrame.place(relx = colourRelX, rely = colourRelY, relwidth =0.1,relheight = 0.085)
            currentColour += 1
            colourRelX += 0.15
            if currentColour == 6:
                colourRelY += 0.125
                colourRelX = 0.01

        #background
        backgroundLabel = tk.Label(settingsFrame, bg = red, fg= white, font = font1, text = "Background Image", anchor = tk.W)
        backgroundLabel.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)


        #background change func (not complete)
        def changeBackGround(backgroundImage=None):
            openFile = tk.filedialog.askopenfile(title="Open File")
            var1.set(openFile)
            win.config(image = backgroundImage)
            pass


        chooseBackgroundBtn = tk.Button(settingsFrame, bg = white, fg = black, bd = 0, font=arialFont, text = "Choose Photo", command = changeBackGround)
        chooseBackgroundBtn.place(relx = 0, rely = 0.525, relwidth = 0.35, relheight = 0.1)

        chooseBackgroundBtn = tk.Button(settingsFrame, bg=white, fg=black, bd=0, font=arialFont, text="X",)
        chooseBackgroundBtn.place(relx=0.37, rely=0.525, relwidth=0.115, relheight=0.1)

        #font
        currenfFont = tk.Frame(settingsFrame, bg = white)
        currenfFont.place(relx = 0, rely = 0.84, relwidth = 0.277, relheight = 0.104)

        fontLabel = tk.Label(settingsFrame, bg=red, fg=white, font=font1, text="Font", anchor=tk.W)
        fontLabel.place(relx=0, rely=0.7, relwidth=1, relheight=0.1)
        arialFontBtn = tk.Button(settingsFrame, bg=black, fg=white, text = "Arial", bd = 0, font = arialFont)
        arialFontBtn.place(relx = 0.015, rely = 0.85, relwidth = 0.25, relheight = 0.08)

        consolasFontBtn = tk.Button(settingsFrame, bg=black, fg=white, text="Consolas", bd=0, font=consoleFont)
        consolasFontBtn.place(relx=0.3, rely=0.85, relwidth=0.25, relheight=0.08)

        arialFontBtn = tk.Button(settingsFrame, bg=black, fg=white, text="Calibri", bd=0, font=calibriFont)
        arialFontBtn.place(relx=0.57, rely=0.85, relwidth=0.25, relheight=0.08)



    def otherSettings():
        pass

    styling()
    #buttons
    general = tk.Button(frame, bg = red, fg = white ,font = font1, bd = 0, activebackground = white, text= "Styling", command = styling)
    general.place(relx = 0.05, rely = 0.85, relwidth = 0.45, relheight = 0.1)
    underline1 = tk.Frame(frame, bg = white)
    underline1.place(relx=0.05, rely=0.95, relwidth=0.45, relheight=0.01)

    other = tk.Button(frame, bg=red, fg=white, font=font1, bd=0, activebackground=white, text="Other",command=otherSettings)
    other.place(relx=0.5, rely=0.85, relwidth=0.45, relheight=0.1)
    underline2 = tk.Label(frame, bg=red, text = "▲", fg=  white, font = font6)
    underline2.place(relx=0.5, rely=0.95, relwidth=0.45, relheight=0.03)




def About():
    logList.append("Opened About")
    mainFrame.destroy()

    frame = tk.Frame(win, bg=red)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    controlFrame = tk.Frame(frame, bg=red)
    controlFrame.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    global backImage
    backImage = ImageTk.PhotoImage(Image.open("staticfiles/backToMM.png"))
    backBtn = tk.Button(controlFrame, bg=red, image=backImage, bd=0, activebackground=red, command=mainWindow)
    backBtn.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.8)

    global hideWinBtn
    hideWinBtn = ImageTk.PhotoImage(Image.open("staticfiles/tray.png"))
    global closeAppBtn
    closeAppBtn = ImageTk.PhotoImage(Image.open("staticfiles/closeApp.png"))

    hideBtn = tk.Button(controlFrame, bg=red, image=hideWinBtn, bd=0, activebackground=black, command=hide_window)
    hideBtn.place(relx=0.8, rely=0.12, relwidth=0.09, relheight=0.75)
    closeBtn = tk.Button(controlFrame, bg=red, image=closeAppBtn, bd=0, activebackground=black, command=appClose)
    closeBtn.place(relx=0.9, rely=0.12, relwidth=0.09, relheight=0.75)

    #hover func
    def Info1Hover(event):
        InfoCursor1.config(bg = red , fg = white)
        AppInfoTitle.config(font = font1)

    def Info1Unhover(event):
        InfoCursor1.config(bg = red , fg = red)
        AppInfoTitle.config(font=arialFont)


    def Info2Hover(event):
        InfoCursor2.config(bg = red , fg = white)
        AppVerTitle.config(font=font1)

    def Info2Unhover(event):
        InfoCursor2.config(bg=red, fg=red)
        AppVerTitle.config(font=arialFont)

    def Info3Hover(event):
        InfoCursor3.config(bg = red , fg = white)
        AppAboutTitle.config(font=font1)

    def Info3Unhover(event):
        InfoCursor3.config(bg=red, fg=red)
        AppAboutTitle.config(font=arialFont)

    def Info4Hover(event):
        InfoCursor4.config(bg = red , fg = white)
        DevDateTitle.config(font=font1)

    def Info4Unhover(event):
        InfoCursor4.config(bg=red, fg=red)
        DevDateTitle.config(font=arialFont)

    def Info5Hover(event):
        InfoCursor5.config(bg = red , fg = white)
        TimeSpendTitle.config(font=font1)

    def Info5Unhover(event):
        InfoCursor5.config(bg=red, fg=red)
        TimeSpendTitle.config(font=arialFont)

    def Info6Hover(event):
        InfoCursor6.config(bg = red , fg = white)
        AuthorTitle.config(font=font1)

    def Info6Unhover(event):
        InfoCursor6.config(bg=red, fg=red)
        AuthorTitle.config(font=arialFont)

    #about
    AboutFrame = tk.Frame(frame, bg = red)
    AboutFrame.place(relx = 0.05, rely = 0.1, relwidth =0.9, relheight = 0.85)

    AboutTitle = tk.Label(AboutFrame, bg = red , fg = white, font = font5, text = "About")
    AboutTitle.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.08)

    AppInfoTitle1 = tk.Label(AboutFrame, bg=red, fg=white, font=font2, text="App Info", anchor = tk.W)
    AppInfoTitle1.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)

    AppInfoTitle = tk.Label(AboutFrame, bg=red, fg=white, font=arialFont, text=f"App Title: {appTitle}", anchor=tk.W,)
    AppInfoTitle.place(relx=0, rely=0.16, relwidth=1, relheight=0.08)
    InfoCursor1 = tk.Label(AboutFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    InfoCursor1.place(relx=0.9, rely=0.15, relwidth=0.1, relheight=0.06)
    AppInfoTitle.bind("<Enter>", Info1Hover)
    AppInfoTitle.bind("<Leave>", Info1Unhover)

    AppVerTitle = tk.Label(AboutFrame, bg=red, fg=white, font=arialFont, text=f"App Version: {appVersion}", anchor=tk.W)
    AppVerTitle.place(relx=0, rely=0.24, relwidth=1, relheight=0.08)
    InfoCursor2 = tk.Label(AboutFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    InfoCursor2.place(relx=0.9, rely=0.23, relwidth=0.1, relheight=0.06)
    AppVerTitle.bind("<Enter>", Info2Hover)
    AppVerTitle.bind("<Leave>", Info2Unhover)

    AppAboutTitle = tk.Label(AboutFrame, bg=red, fg=white, font=arialFont, text=f"About this App: {about}", anchor=tk.W)
    AppAboutTitle.place(relx=0, rely=0.32, relwidth=1, relheight=0.08)
    InfoCursor3 = tk.Label(AboutFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    InfoCursor3.place(relx=0.9, rely=0.31, relwidth=0.1, relheight=0.06)
    AppAboutTitle.bind("<Enter>", Info3Hover)
    AppAboutTitle.bind("<Leave>", Info3Unhover)

    MiddleLine = tk.Frame(AboutFrame, bg = white)
    MiddleLine.place(relx=0, rely=0.45, relwidth=1, relheight=0.01)



    AuthorInfoTitle = tk.Label(AboutFrame, bg=red, fg=white, font=font2, text="Dev Info", anchor=tk.W)
    AuthorInfoTitle.place(relx=0, rely=0.5, relwidth=1, relheight=0.08)

    DevDateTitle = tk.Label(AboutFrame, bg=red, fg=white, font=arialFont, text=f"Development Date: {devDate}", anchor=tk.W)
    DevDateTitle.place(relx=0, rely=0.58, relwidth=1, relheight=0.08)
    InfoCursor4 = tk.Label(AboutFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    InfoCursor4.place(relx=0.9, rely=0.57, relwidth=0.1, relheight=0.06)
    DevDateTitle.bind("<Enter>", Info4Hover)
    DevDateTitle.bind("<Leave>", Info4Unhover)

    TimeSpendTitle = tk.Label(AboutFrame, bg=red, fg=white, font=arialFont, text="Spent Days: 4", anchor=tk.W)
    TimeSpendTitle.place(relx=0, rely=0.66, relwidth=1, relheight=0.08)
    InfoCursor5 = tk.Label(AboutFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    InfoCursor5.place(relx=0.9, rely=0.65, relwidth=0.1, relheight=0.06)
    TimeSpendTitle.bind("<Enter>", Info5Hover)
    TimeSpendTitle.bind("<Leave>", Info5Unhover)

    AuthorTitle = tk.Label(AboutFrame, bg=red, fg=white, font=arialFont, text=f"Author: {author}", anchor=tk.W)
    AuthorTitle.place(relx=0, rely=0.74, relwidth=1, relheight=0.08)
    InfoCursor6 = tk.Label(AboutFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    InfoCursor6.place(relx=0.9, rely=0.73, relwidth=0.1, relheight=0.06)
    AuthorTitle.bind("<Enter>", Info6Hover)
    AuthorTitle.bind("<Leave>", Info6Unhover)

def Console():
    logList.append("Opened Console")
    mainFrame.destroy()

    frame = tk.Frame(win, bg=red)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    controlFrame = tk.Frame(frame, bg=red)
    controlFrame.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    global backImage
    backImage = ImageTk.PhotoImage(Image.open("staticfiles/backToMM.png"))
    backBtn = tk.Button(controlFrame, bg=red, image=backImage, bd=0, activebackground=red, command=mainWindow)
    backBtn.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.8)

    global hideWinBtn
    hideWinBtn = ImageTk.PhotoImage(Image.open("staticfiles/tray.png"))
    global closeAppBtn
    closeAppBtn = ImageTk.PhotoImage(Image.open("staticfiles/closeApp.png"))

    hideBtn = tk.Button(controlFrame, bg=red, image=hideWinBtn, bd=0, activebackground=black, command=hide_window)
    hideBtn.place(relx=0.8, rely=0.12, relwidth=0.09, relheight=0.75)
    closeBtn = tk.Button(controlFrame, bg=red, image=closeAppBtn, bd=0, activebackground=black, command=appClose)
    closeBtn.place(relx=0.9, rely=0.12, relwidth=0.09, relheight=0.75)

    #Console
    ConsoleFrame = tk.Frame(frame, bg = black)
    ConsoleFrame.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.75)
    text = ["console", "Clear", "pressed button", "input text - sasasaadsff", "text is translated", "showed results", "opened menu"]
    rely = 0.05
    counter = 0
    for i in range(len(text)):
        consoleRow = tk.Label(ConsoleFrame, bg = black, fg = white,font = consoleFont ,text = f"> {logList[counter]}", anchor = tk.W)
        consoleRow.place(relx = 0.05, rely = rely, relwidth = 0.9, relheight = 0.05 )
        rely +=0.05
        counter +=1



    #clear console
    clearConsole = tk.Button(frame, bg = white, fg = black, text = "Clear", bd = 0, font = font1)
    clearConsole.place(relx = 0.05, rely = 0.86, relwidth = 0.9, relheight = 0.09)

def FeedBack():
    logList.append("Opened Append")
    mainFrame.destroy()

    frame = tk.Frame(win, bg=red)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    controlFrame = tk.Frame(frame, bg=red)
    controlFrame.place(relx=0, rely=0, relwidth=1, relheight=0.08)

    global backImage
    backImage = ImageTk.PhotoImage(Image.open("staticfiles/backToMM.png"))
    backBtn = tk.Button(controlFrame, bg=red, image=backImage, bd=0, activebackground=red, command=mainWindow)
    backBtn.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.8)

    global hideWinBtn
    hideWinBtn = ImageTk.PhotoImage(Image.open("staticfiles/tray.png"))
    global closeAppBtn
    closeAppBtn = ImageTk.PhotoImage(Image.open("staticfiles/closeApp.png"))

    hideBtn = tk.Button(controlFrame, bg=red, image=hideWinBtn, bd=0, activebackground=black, command=hide_window)
    hideBtn.place(relx=0.8, rely=0.12, relwidth=0.09, relheight=0.75)
    closeBtn = tk.Button(controlFrame, bg=red, image=closeAppBtn, bd=0, activebackground=black, command=appClose)
    closeBtn.place(relx=0.9, rely=0.12, relwidth=0.09, relheight=0.75)

    #Hover Effects
    def Title1hover(event):
        Title1.config(bg = black)
        YTButton.config(bg = black, fg = white, font = font1)
        YTCursor.config(bg = black, fg = white)

    def Title1unhover(event):
        Title1.config(bg=red)
        YTButton.config(bg=red, fg=white, font=font1)
        YTCursor.config(bg=red, fg=red)

    def Title2hover(event):
        Title2.config(bg = black)
        InstButton.config(bg=black, fg=white, font=font1)
        InstCursor.config(bg=black, fg=white)

    def Title2unhover(event):
        Title2.config(bg=red)
        InstButton.config(bg=red, fg=white, font=font1)
        InstCursor.config(bg=red, fg=red)

    def Title3hover(event):
        Title3.config(bg = black)
        FBButton.config(bg=black, fg=white, font=font1)
        FBCursor.config(bg=black, fg=white)

    def Title3unhover(event):
        Title3.config(bg=red)
        FBButton.config(bg=red, fg=white, font=font1)
        FBCursor.config(bg=red, fg=red)

    def Title4hover(event):
        Title4.config(bg = black)
        GMButton.config(bg=black, fg=white, font=font1)
        GMCursor.config(bg=black, fg=white)

    def Title4unhover(event):
        Title4.config(bg=red)
        GMButton.config(bg=red, fg=white, font=font1)
        GMCursor.config(bg=red, fg=red)

    def Title5hover(event):
        Title5.config(bg = black)
        TGButton.config(bg=black, fg=white, font=font1)
        TGCursor.config(bg=black, fg=white)

    def Title5unhover(event):
        Title5.config(bg=red)
        TGButton.config(bg=red, fg=white, font=font1)
        TGCursor.config(bg=red, fg=red)

    #feedback
    FeedbackFrame = tk.Frame(frame, bg = red)
    FeedbackFrame.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.85)

    #Media Links
    MediaTitle = tk.Label(FeedbackFrame, bg = red, fg = white, font = font2, text = "Our Media")
    MediaTitle.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)
    #Media Titles
    LinksTitleFrame1 = tk.Frame(FeedbackFrame, bg = red)
    LinksTitleFrame1.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.35)

    Title1 = tk.Label(LinksTitleFrame1, bg = red, fg = white, text = " YouTube",font=font1, anchor=tk.W)
    Title1.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.33)
    Title1.bind("<Enter>", Title1hover)
    Title1.bind("<Leave>", Title1unhover)

    Title2 = tk.Label(LinksTitleFrame1, bg=red, fg=white, text=" Instagramm", font=font1, anchor=tk.W)
    Title2.place(relx=0, rely=0.33, relwidth=1, relheight=0.33)
    Title2.bind("<Enter>", Title2hover)
    Title2.bind("<Leave>", Title2unhover)

    Title3 = tk.Label(LinksTitleFrame1, bg=red, fg=white, text=" Facebook", font=font1, anchor=tk.W)
    Title3.place(relx=0, rely=0.66, relwidth=1, relheight=0.33)
    Title3.bind("<Enter>", Title3hover)
    Title3.bind("<Leave>", Title3unhover)

    #Media Links Buttons
    YTButton = tk.Button(LinksTitleFrame1, bg = red, text = "Open", bd = 0, font = font1, fg = white)
    YTButton.place(relx = 0.5, rely = 0, relwidth = 0.33, relheight = 0.33)
    YTCursor = tk.Label(LinksTitleFrame1, bd = 0, bg = red, fg = red, text = "<", font = ("Consolas",20, 'bold'))
    YTCursor.place(relx = 0.8, rely = 0.07, relwidth= 0.1, relheight = 0.15)
    YTButton.bind("<Enter>", Title1hover)
    YTButton.bind("<Leave>", Title1unhover)

    InstButton = tk.Button(LinksTitleFrame1, bg=red, text = "Open", bd=0, font = font1, fg = white)
    InstButton.place(relx=0.5, rely=0.33, relwidth=0.33, relheight=0.33)
    InstCursor = tk.Label(LinksTitleFrame1, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    InstCursor.place(relx=0.8, rely=0.4, relwidth=0.1, relheight=0.15)
    InstButton.bind("<Enter>", Title2hover)
    InstButton.bind("<Leave>", Title2unhover)

    FBButton = tk.Button(LinksTitleFrame1, bg=red,  text = "Open", bd=0 , font = font1, fg = white)
    FBButton.place(relx=0.5, rely=0.66, relwidth=0.33, relheight=0.33)
    FBCursor = tk.Label(LinksTitleFrame1, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    FBCursor.place(relx=0.8, rely=0.73, relwidth=0.1, relheight=0.15)
    FBButton.bind("<Enter>", Title3hover)
    FBButton.bind("<Leave>", Title3unhover)

    MiddleLine = tk.Frame(FeedbackFrame, bg = white)
    MiddleLine.place(relx = 0, rely = 0.45, relwidth = 1, relheight = 0.01)

    FeedbackTitleFrame = tk.Frame(FeedbackFrame, bg = red)
    FeedbackTitleFrame.place(relx=0, rely=0.5, relwidth=1, relheight=0.35)
    Title4 = tk.Label(FeedbackTitleFrame, bg=red, fg=white, text=" Gmail Support", font=font1, anchor=tk.W)
    Title4.place(relx=0, rely=0, relwidth=1, relheight=0.33)
    Title4.bind("<Enter>", Title4hover)
    Title4.bind("<Leave>", Title4unhover)

    Title5 = tk.Label(FeedbackTitleFrame, bg=red, fg=white, text=" Telegram ", font=font1, anchor=tk.W)
    Title5.place(relx=0, rely=0.33, relwidth=1, relheight=0.33)
    Title5.bind("<Enter>", Title5hover)
    Title5.bind("<Leave>", Title5unhover)

    GMButton = tk.Button(FeedbackTitleFrame, bg=red, text="Open", bd=0, font = font1, fg = white)
    GMButton.place(relx=0.5, rely=0, relwidth=0.33, relheight=0.33)
    GMCursor = tk.Label(FeedbackTitleFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    GMCursor.place(relx=0.8, rely=0.07, relwidth=0.1, relheight=0.15)
    GMButton.bind("<Enter>", Title4hover)
    GMButton.bind("<Leave>", Title4unhover)

    TGButton = tk.Button(FeedbackTitleFrame, bg=red, text="Open", bd=0, font = font1, fg = white)
    TGButton.place(relx=0.5, rely=0.33, relwidth=0.33, relheight=0.33)
    TGCursor = tk.Label(FeedbackTitleFrame, bd=0, bg=red, fg=red, text="<", font=("Consolas", 20, 'bold'))
    TGCursor.place(relx=0.8, rely=0.4, relwidth=0.1, relheight=0.15)
    TGButton.bind("<Enter>", Title5hover)
    TGButton.bind("<Leave>", Title5unhover)


#Clearly Closing app
def appClose():
    win.quit()
    win.destroy()
    exit()

def frame_mapped(e):
        logList.append("Unhidden Window")
        print(e)
        win.update_idletasks()
        win.overrideredirect(True)
        win.state('normal')

#windoe tray func
def hide_window():
    logList.append("Hidden window")
    win.update_idletasks()
    win.overrideredirect(False)
    win.wm_state('iconic')




#window show function
if __name__ == "__main__":
    startFrame()
    win.mainloop()




