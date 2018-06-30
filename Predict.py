from Tkinter import *
import pandas as pd
import datetime
import folium
from folium.map import *
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import FloatImage
import sys
from browser import BrowserDialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

url = ('https://media.licdn.com/mpr/mpr/shrinknp_100_100/AAEAAQAAAAAAAAlgAAAAJGE3OTA4YTdlLTkzZjUtNDFjYy1iZThlLWQ5OTNkYzlhNzM4OQ.jpg')



def quit3():

    master3.destroy()

def ShowChoice():
    print(v.get())


def predict():
    F_date = f1.get()
    F_crimeclass = v.get()
    F_predmodel = s.get()
    f1.delete(0,END)
    master3.destroy()
    
    #Split the date
    day_list = [7,1,2,3,4,5,6]
    split_date = F_date.split('-')
    day = int(split_date[0])
    month = int(split_date[1])
    year = int(split_date[2])
    date = datetime.date(year,month,day)



    #Previous day
    prev_date = date + datetime.timedelta(days=-1)
    prev_day = prev_date.day
    prev_date_month = prev_date.month
    prev_date_year = prev_date.year
    
    SF_COORDINATES = (37.76, -122.45)
    #crimedata = pd.read_csv('new_train(kaggledata).csv')
    crimedata = pd.read_csv('demo.csv')
    state_geo = 'SFPD.json'
    crime_count = open('crime_countdata.csv','w')
    # for speed purposes
    MAX_RECORDS = 878050
    list_of_crimes = ["WARRANTS","OTHER OFFENSES","LARCENY/THEFT","VEHICLE THEFT","VANDALISM","NON-CRIMINAL","ROBBERY","ASSAULT","WEAPON LAWS","BURGLARY","SUSPICIOUS OCC","DRUNKENNESS","FORGERY/COUNTERFEITING","DRUG/NARCOTIC","STOLEN PROPERTY","SECONDARY CODES","TRESPASS","MISSING PERSON","FRAUD","KIDNAPPING","RUNAWAY","DRIVING UNDER THE INFLUENCE","SEX OFFENSES FORCIBLE","PROSTITUTION","DISORDERLY CONDUCT","ARSON","FAMILY OFFENSES","LIQUOR LAWS","BRIBERY","EMBEZZLEMENT","SUICIDE","LOITERING","SEX OFFENSES NON FORCIBLE","EXTORTION","GAMBLING","BAD CHECKS","TREA","RECOVERED VEHICLE","PORNOGRAPHY/OBSCENE MAT"]
    list_of_pdistrict = ["NORTHERN","PARK","INGLESIDE","BAYVIEW","RICHMOND","CENTRAL","TARAVAL","TENDERLOIN","MISSION","SOUTHERN"] 
    count_of_pdistrict = {"NORTHERN":0,"PARK":0,"INGLESIDE":0,"BAYVIEW":0,"RICHMOND":0,"CENTRAL":0,"TARAVAL":0,"TENDERLOIN":0,"MISSION":0,"SOUTHERN":0}
    # create empty map zoomed in on San Francisco
    m = folium.Map(location=SF_COORDINATES, zoom_start=13,tiles='CartoDBPositron')
    cluster = folium.plugins.MarkerCluster(name="Previous Crimes").add_to(m)

    # add a marker for every record in the filtered data, use a clustered view
    for each in crimedata[0:MAX_RECORDS].iterrows():
        if ((int(each[1]['Day'])==prev_day) and (int(each[1]['Month'])==prev_date_month) and (int(each[1]['Year'])==prev_date_year)):
            crime_name = list_of_crimes[int(each[1]['Category'])-1]
            occ_date = "%s-%s-%s"%(str(prev_day),str(prev_date_month),str(prev_date_year))
            pdistrict = list_of_pdistrict[int(each[1]['PdDistrict'])-1]
            count_of_pdistrict[pdistrict]=(count_of_pdistrict[pdistrict])+1
            location = "%s,%s"%(each[1]['Y'],each[1]['X'])
            folium.Marker(location = [each[1]['Y'],each[1]['X']], popup='<b>Occured date: </b>%s<br></br><b>Crime Type: </b>%s<br></br><b>Police District: </b>%s<br></br><b>Location: </b>%s'%(occ_date,crime_name,pdistrict,location),).add_to(cluster)


    crime_count.write('PD,Crime_Count\n')
    for key in count_of_pdistrict:
        crime_count.write("%s,%s\n"%(key,str(count_of_pdistrict[key])))
    crime_count.close()
    state_data = pd.read_csv('crime_countdata.csv')
    m.choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=state_data,
        columns=['PD', 'Crime_Count'],
        key_on='feature.id',
        fill_color='Reds',
        fill_opacity=0.7,
        line_opacity=0.9,
        legend_name='Crime Rate'
    )


    non_violent_loc =[[ 37.783003799999996,-122.4124143],[37.77436883,-122.5058834],[37.74491907,-122.47577350000002],[37.71083265,-122.43244650000001],[37.72513804,-122.423327],[37.73015769,-122.37598919999999],[37.75999239,-122.3977468],[37.80087263,-122.4269953],[37.77739182,-122.3976156],[37.77539248,-122.4156581],[37.79149808,-122.40574479999998],[37.79750489,-122.4020426]]
    violent_loc=[[37.72156474,-122.47318200000001],[37.73511269,-122.4845457],[ 37.73449811,-122.4448541],[37.76978409,-122.449123],[37.77753219,-122.4408795],[37.7299736,-122.3920652],[37.80427189,-122.44827839999999],[37.774598600000004,-122.42589170000001],[37.79243096,-122.3957716],[37.75942275,-122.41905890000001],[37.80618612,-122.41625959999999]]

    for loc in non_violent_loc:
        folium.CircleMarker(location=loc, radius=30,
                popup='<b>Prediction Type: </b>Non-Violent Crime<br></br><b>Location: </b>%s'%(loc), line_color='#3186cc',
                fill_color='#FFFFFF',fill_opacity=0.7, fill=True).add_to(m)


    for loc in violent_loc:
        folium.CircleMarker(location=loc, radius=30,
                popup='<b>Prediction Type: </b>Violent Crime<br></br><b>Location: </b>%s'%(loc), line_color='#3186cc',
                fill_color='#000000',fill_opacity=0.7, fill=True).add_to(m)


    
    folium.TileLayer(tiles='Stamen Toner',name="Stamen Toner").add_to(m)
    folium.TileLayer(tiles='Stamen Terrain',name="Stamen Terrain").add_to(m)
    folium.LayerControl().add_to(m)
    m.add_child(MeasureControl())
    FloatImage(url, bottom=5, left=85).add_to(m)
    m.save('index.html')
    print "Saving the webpage for map...."
    class MyBrowser(QtGui.QDialog):
        def __init__(self, parent=None):
            QtGui.QWidget.__init__(self, parent)
            QWebView.__init__(self)
            self.ui = BrowserDialog()
            self.ui.setupUi(self)
            self.ui.lineEdit.returnPressed.connect(self.loadURL)
     
        def loadURL(self):
            url = self.ui.lineEdit.text()
            self.ui.qwebview.load(QUrl(url))
            self.show()  
            #self.ui.lineEdit.setText("")
     
    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = MyBrowser()
        myapp.ui.qwebview.load(QUrl("D:\My Programs + Projects\Crime2Vec - QCRI Internship '18\Main Files\GUI\index.html"))
        myapp.show()
        sys.exit(app.exec_())




#Create the add to database window
master3 = Tk() #form window
v = IntVar()
v.set(0)
s = IntVar()
s.set(0)
crime_desc = ["Exact crime type","Violent vs. Non-Violent crime"]
pred_models = ["Crime2Vec","Random Forest","Naive Bayes","SVM","Logistic Regression"]
master3.title("Crime Prediction")  #Title of the form
master3.configure(background = '#656565')
master3.resizable(False, False) 
Label(master3, text="Predict Crimes",fg='#FFFFFF',font=("Segoe UI Light", 30),bg='#656565').grid(row=0,columnspan=1,sticky=W,padx=10,pady=10)
Label(master3, text="*indicates mandatory fields",fg='#FFFFFF',font=("Segoe UI Light", 12),bg='#656565').grid(row=1,columnspan=1,sticky=W,padx=10,pady=10)


#Label box in each row
var = IntVar()
Radiobutton(master3, text="Administrator",fg='#000000', variable=var,font=("Segoe UI Light", 15),bg='#494949', value=1).grid(sticky=W,row=2,columnspan=1,pady=10,padx=50)
Radiobutton(master3, text="Verified User",fg='#000000', variable=var,font=("Segoe UI Light", 15),bg='#494949', value=2).grid(sticky=E,row=2,columnspan=2,pady=10,padx=50)
Label(master3, text="Date(dd-mm-yyyy)*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=3,sticky=W,pady=10)
Label(master3, text="Choose the type of classification*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=4,sticky=W,pady=10)
Label(master3, text="Choose the type of prediction model*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=6,sticky=W,pady=10)
for val, language in enumerate(crime_desc):
    Radiobutton(master3, 
                  text=language,
                  fg='#000000',
                  font=("Segoe UI Light", 15),
                  bg='#494949',
                  variable=v,
                  value=val).grid(row=5,column=val,sticky=W)


for val, language in enumerate(pred_models):
    if val==0 or val==1:
        Radiobutton(master3, 
                      text=language,
                      fg='#000000',
                      font=("Segoe UI Light", 15),
                      bg='#494949',
                      variable=s,
                      value=val).grid(row=7,column=val,sticky=W)
    elif val==2 or val==3:
        Radiobutton(master3, 
                      text=language,
                      fg='#000000',
                      font=("Segoe UI Light", 15),
                      bg='#494949',
                      variable=s,
                      value=val).grid(row=8,column=val-2,sticky=W)
    else:
        Radiobutton(master3, 
                      text=language,
                      fg='#000000',
                      font=("Segoe UI Light", 15),
                      bg='#494949',
                      variable=s,
                      value=val).grid(row=9,column=val-4,sticky=W)
        


#Text entry/box for each label
f1=Entry(master3,width=30)

#Text box in each row
f1.grid(row=3, column=1,sticky=E,padx=10)


Button(master3, text='Predict now',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#2C2827', command=predict,height = 1, width = 15).grid(row=10,column=0,sticky=W,pady=30,padx=10)
Button(master3, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#2C2827', command=quit3,height = 1, width = 15).grid(row=10,column=1,sticky=W,pady=30,padx=10)
mainloop()


