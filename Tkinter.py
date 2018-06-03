import tkinter as Tkinter
import base64

top = Tkinter.Tk()
top.geometry("1200x6000")
top.title("Message Encryption and Decryption")

rand = Tkinter.StringVar()
Msg = Tkinter.StringVar()
key = Tkinter.StringVar()
mode = Tkinter.StringVar()
Result = Tkinter.StringVar()

lblReference = Tkinter.Label(top,font=('arial',16,'bold'),text="Name:",bd=16,anchor="w").grid(row=0,column=0)
txtReference = Tkinter.Entry(top,font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4,bg="powder blue", justify='right')
txtReference.grid(row=0, column=1)

lblReference = Tkinter.Label(top, font = ('arial', 16, 'bold'),text = "Message:", bd = 16, anchor = "w").grid(row=1,
                                                                                                              column=0)
txtReference = Tkinter.Entry(top, font=('arial', 16, 'bold'),textvariable=Msg, bd=10, insertwidth=4,bg="powder blue",
                             justify='right')
txtReference.grid(row=1, column=1)

lblReference = Tkinter.Label(top, font = ('arial', 16, 'bold'),text = "Key:", bd = 16, anchor = "w").grid(row=2,column=0)
txtReference = Tkinter.Entry(top, font=('arial', 16, 'bold'),textvariable=key, bd=10, insertwidth=4,bg="powder blue",
                             justify='right')
txtReference.grid(row=2, column=1)

lblReference = Tkinter.Label(top, font = ('arial', 16, 'bold'),text = "Mode:", bd = 16, anchor = "w").grid(row=3,column=0)
txtReference = Tkinter.Entry(top, font=('arial', 16, 'bold'),textvariable=mode, bd=10, insertwidth=4,bg="powder blue",
                             justify='right')
txtReference.grid(row=3, column=1)

lblReference = Tkinter.Label(top, font = ('arial', 16, 'bold'),text = "Result:", bd = 16, anchor = "w").grid(row=3,
                                                                                                             column = 2)
txtReference = Tkinter.Entry(top, font=('arial', 16, 'bold'),textvariable=Result, bd=10, insertwidth=4,bg="powder blue", justify='right')
txtReference.grid(row=3, column=3)


def hellocallback():
    m = mode.get()
    clear = Msg.get()
    k = key.get()
    if m == 'e':
        enc = []
        for i in range(len(clear)):
            key_c = k[i % len(k)]
            enc_c = chr((ord(clear[i]) +
                         ord(key_c)) % 256)

            enc.append(enc_c)

        Result.set(base64.urlsafe_b64encode("".join(enc).encode()).decode())
    elif m == 'd':
        dec = []
        enc = base64.urlsafe_b64decode(clear).decode()
        for i in range(len(enc)):
            key_c = k[i % len(k)]
            dec_c = chr((256 + ord(enc[i]) -
                         ord(key_c)) % 256)

            dec.append(dec_c)
            Result.set("".join(dec))

def reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

def exit():
    top.destroy()

ShowMessage = Tkinter.Button(top, padx = 16, pady = 8, bd = 16, fg = "black",
                        font = ('arial', 16, 'bold'), width = 10, text ="ShowMessage",bg = "powder blue", command=hellocallback).grid(row = 7, column = 1)

Reset = Tkinter.Button(top,padx = 16, pady = 8, bd = 16,
                  fg = "black", font = ('arial', 16, 'bold'),
                    width = 10, bg = "green", text ="Reset", command=reset).grid(row = 7, column = 2)

Exit = Tkinter.Button(top, padx = 16, pady = 8, bd = 16,
                 fg = "black", font = ('arial', 16, 'bold'),
                      width = 10, text = "Exit", bg = "red", command=exit).grid(row = 7, column = 3)

top.mainloop()
