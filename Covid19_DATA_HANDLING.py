from covid import *             #pip install covid
import datetime
import matplotlib.pyplot as plt #pip install matplotlib
from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import messagebox  
import os

lst = os.listdir()

if 'data' not in lst:
    os.mkdir('data')
    
print('Created By Shivank Dubey')

window = Tk()
window.title('COVID19_DATA_HANDLING')
window.resizable(0,0)
window.geometry('800x600')
covid = Covid()

corona = ImageTk.PhotoImage(file='corona.png')
bg = Label(window, image=corona)
bg.pack(fill=BOTH, expand=True)

title = Label(bg, text='COVID19_DATA_HANDLING', font=('Calibari', 26, 'bold'), bg='pink')
title.pack()

gap1 = Label(bg, text='                       ', font=('Calibari', 18, 'bold'), bg='light blue', width=800)
gap1.pack()

frame = Frame(bg, bg='yellow')
frame.pack()

label = Label(frame, text='Enter Country name', font=('Calibari', 24, 'bold'), bg='yellow')
label.grid(row=0, column=0)

gap = Label(frame, text='          ', font=('Calibari', 24, 'bold'), bg='yellow')
gap.grid(row=0, column=1)

entry = Entry(frame, font=('Calibari', 24))
entry.grid(row=0, column=2)

def main():
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    curtime = hour+minute+second
    
    country = str(entry.get())

    try:
        result = covid.get_status_by_country_name(country)
        print()
       
        '''{'id': '137', 'country': 'Pakistan', 'confirmed': 45898, 'active': 31812, 'deaths': 985, 'recovered': 13101, 'latitude': 30.3753,
        'longitude': 69.3451, 'last_update': 1589970736000}'''

        ID = list(result.values())[0]
        country = list(result.values())[1]
        confirmed = list(result.values())[2]
        active = list(result.values())[3]
        deaths = list(result.values())[4]
        recovered = list(result.values())[5]
        dp = float(deaths/confirmed*100)
        rp = float(recovered/confirmed*100)
        
        lb.delete(0, END)
        lb.insert(END, 'Country ID: '+str(ID))
        lb.insert(END, 'Country Name: '+str(country))
        lb.insert(END, 'Confirmed Cases: '+str(confirmed))
        lb.insert(END, 'Active Cases: '+str(active))
        lb.insert(END, 'Deaths: '+str(deaths))
        lb.insert(END, 'Recovered: '+str(recovered))
        lb.insert(END, 'Deaths percentage: '+str(dp)+str('% (Per 100 Conirmed Cases)'))
        lb.insert(END, 'Recovery percentage: '+str(rp)+str('% (Per 100 Confirmed Cases)'))
        
        
        
        list1 = [confirmed, active, deaths, recovered]
        #plt.bar(['Confirmed', 'Active', 'Deaths', 'Recovered'], [confirmed,active,deaths,recovered],
        #        color=['orange', 'yellow', 'red', 'green'], label=list1)
        plt.bar('Confirmed', confirmed, color='orange', label=confirmed)
        plt.bar('Active', active, color='yellow', label=active)
        plt.bar('Deaths', deaths, color='red', label=deaths)
        plt.bar('Recovered', recovered, color='green', label=recovered)
        plt.legend()
        plt.ylabel('Counts')
        plt.xlabel('Parameters')
        plt.title('COVID-19 STATS IN '+str(country).upper()+' ON '+str(datetime.datetime.now().date()))
        #plt.axis([0,4,0,100])
        plt.savefig('data\\'+country+'_time'+curtime)
        plt.show()
    except:
        messagebox.showerror('ERROR', 'COUNTRY NAME IS NOT RECOGNIZABLE OR CHECK THE INTERNET CONNECTION')

gap1 = Label(bg, text='                       ', font=('Calibari', 18, 'bold'), bg='light blue', width=800)
gap1.pack()

button = Button(bg, text='GET DATA', command = main, width=800, height=2, font=('Calibari', 10, 'bold'), bg='light green')
button.pack()

gap1 = Label(bg, text='RESULT WILL BE DISLAYED BELOW', font=('Calibari', 18, 'bold'), bg='light blue', width=800)
gap1.pack()

lb = Listbox(bg, width=600, bg='yellow', font=('Calibari', 16, 'bold'))
lb.pack()
window.mainloop()
