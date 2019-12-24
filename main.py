'''
Created on Mar 21, 2016

@author: Bill Begueradj
'''
try:
    import Tkinter
    import ttk
except ImportError:  # Python 3
    import tkinter as Tkinter
    #import tkinter.ttk as ttk
    #import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
    from tkinter import ttk
    from tkinter import messagebox

    from datetime import datetime
    import pandas as pd


class Window(Tkinter.Frame):



    '''
    classdocs
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()





    def crear_detalle(self, tabcontrol):

        # crear treeview
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 11, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.tree = ttk.Treeview(tabcontrol, style="mystyle.Treeview")
        self.tree.configure(
            height=19,
            columns=('fecha_in', 'fecha_out', 'estacion', 'cliente', 'usuario', 'tiempo', 'bytes', 'consumo', 'conexiones'),
            displaycolumns="#all"
        )

        self.tree.heading('#0', text='Fecha Acceso')
        self.tree.heading('#1', text='Fecha Desconexion')
        self.tree.heading('#2', text='Estacion')
        self.tree.heading('#3', text='Cliente')
        self.tree.heading('#4', text='Usuario')
        self.tree.heading('#5', text='Tiempo (segundos)')
        self.tree.heading('#6', text='Transferencia (bytes)')
        self.tree.heading('#7', text='Consumo (b/s)')
        self.tree.heading('#8', text='Conexiones')

        self.tree.column('#1', stretch=Tkinter.YES, anchor=Tkinter.W)
        self.tree.column('#2', stretch=Tkinter.YES, anchor=Tkinter.W)
        self.tree.column('#3', stretch=Tkinter.YES, anchor=Tkinter.W)
        self.tree.column('#4', stretch=Tkinter.YES, anchor=Tkinter.W)
        self.tree.column('#5', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#6', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#7', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#8', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#0', stretch=Tkinter.YES, anchor=Tkinter.E)

        self.tree.column('#1', width=150)
        self.tree.column('#2', width=80)
        self.tree.column('#3', width=80)
        self.tree.column('#4', width=80)
        self.tree.column('#5', width=200)
        self.tree.column('#6', width=200)
        self.tree.column('#7', width=200)
        self.tree.column('#8', width=100)
        self.tree.column('#0', width=150)

        scrollH = Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        scrollH.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        scrollV = Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollV.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        self.tree.configure(xscrollcommand=scrollH.set)
        self.tree.configure(yscrollcommand=scrollV.set)
        self.tree.config(selectmode='browse')

        self.tree.grid(row=2, column=0, rowspan=150, columnspan=9, sticky='nsew')

        self.tree.tag_configure(tagname='TOT_ESTACION', background='blue')
        self.tree.tag_configure(tagname='TOT_GENERAL', background='red')

        self.treeview = self.tree
        return self.treeview




    def crear_resumenEstacion(self, tabcontrol):
        # crear treeview
        self.tree = ttk.Treeview(tabcontrol)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 11, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.tree = ttk.Treeview(tabcontrol, style="mystyle.Treeview")

        self.tree.configure(
            height=19,
            columns=('estacion','cliente', 'usuario', 'tiempo', 'bytes', 'consumo', 'conexiones'),
            displaycolumns="#all"
        )

        self.tree.heading('#0', text='Estacion')
        self.tree.heading('#1', text='Usuario')
        self.tree.heading('#2', text='Tiempo (segundos)')
        self.tree.heading('#3', text='Transferencia (bytes)')
        self.tree.heading('#4', text='Consumo (b/s)')
        self.tree.heading('#5', text='Conexiones')

        self.tree.column('#1', stretch=Tkinter.YES, anchor=Tkinter.W)
        self.tree.column('#2', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#3', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#4', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#5', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#0', stretch=Tkinter.YES, anchor=Tkinter.E)

        scrollH = Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        scrollH.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        scrollV = Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollV.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        self.tree.configure(xscrollcommand=scrollH.set)
        self.tree.configure(yscrollcommand=scrollV.set)
        self.tree.config(selectmode='browse')

        self.tree.grid(row=2, column=0, rowspan=150, columnspan=6, sticky='nsew')

        self.tree.tag_configure(tagname='TOT_ESTACION', background='blue')
        self.tree.tag_configure(tagname='TOT_GENERAL', background='red')

        self.treeview = self.tree
        return self.treeview




    def crear_resumenUsuario(self, tabcontrol):
        # crear treeview
        self.tree = ttk.Treeview(tabcontrol)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 11, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.tree = ttk.Treeview(tabcontrol, style="mystyle.Treeview")

        self.tree.configure(
            height=19,
            columns=('usuario', 'tiempo', 'bytes', 'consumo', 'conexiones'),
            displaycolumns="#all"
        )

        self.tree.heading('#0', text='Usuario')
        self.tree.heading('#1', text='Tiempo (segundos)')
        self.tree.heading('#2', text='Transferencia (bytes)')
        self.tree.heading('#3', text='Consumo (b/s)')
        self.tree.heading('#4', text='Conexiones')

        self.tree.column('#1', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#2', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#3', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#4', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#0', stretch=Tkinter.YES, anchor=Tkinter.W)

        scrollH = Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        scrollH.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        scrollV = Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollV.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        self.tree.configure(xscrollcommand=scrollH.set)
        self.tree.configure(yscrollcommand=scrollV.set)
        self.tree.config(selectmode='browse')

        self.tree.grid(row=2, column=0, rowspan=150, columnspan=5, sticky='nsew')
        self.tree.tag_configure(tagname='TOT_ESTACION', background='blue')
        self.tree.tag_configure(tagname='TOT_GENERAL', background='red')

        self.treeview = self.tree
        return self.treeview




    def crear_resumenGeneral(self, tabcontrol):
        # crear treeview
        self.tree = ttk.Treeview(tabcontrol)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 11, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.tree = ttk.Treeview(tabcontrol, style="mystyle.Treeview")

        self.tree.configure(
            height=19,
            columns=('factor', 'rtcm_2_3', 'rtcm_3_0', 'total'),
            displaycolumns="#all"
        )

        self.tree.heading('#0', text='Factor')
        self.tree.heading('#1', text='RTCM2.3')
        self.tree.heading('#2', text='RTCM3.0')
        self.tree.heading('#3', text='TOTAL')

        self.tree.column('#1', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#2', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#3', stretch=Tkinter.YES, anchor=Tkinter.E)
        self.tree.column('#0', stretch=Tkinter.YES, anchor=Tkinter.W)

        scrollH = Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        scrollH.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        scrollV = Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        scrollV.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        self.tree.configure(xscrollcommand=scrollH.set)
        self.tree.configure(yscrollcommand=scrollV.set)
        self.tree.config(selectmode='browse')

        self.tree.grid(row=2, column=0, rowspan=150, columnspan=4, sticky='nsew')
        self.tree.tag_configure(tagname='TOT_ESTACION', background='blue')
        self.tree.tag_configure(tagname='TOT_GENERAL', background='red')

        self.treeview = self.tree
        return self.treeview


    def crear_acercaDe(self, tabcontrol):
        message=("Linea 1 \n"
                 "Linea 2 \n"
                 "Linea 3 \n"
                 )
        # label
        self.info = Message(tabcontrol, text=message, anchor='w')


        return self.info



    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Log Server Analisis")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        # ------------------------------ Menu ------------------------------
        menu = Menu(self.parent)
        self.parent.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open...", command=self.insert_data)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.parent.quit)


        # ------------------------------ Workbook ------------------------------
        # Creo el contenedor de paginas
        self.tabcontrol = ttk.Notebook(self.parent)

        # Creo la pagina de detalles
        self.tabDetalle = self.crear_detalle(self.tabcontrol)
        self.tabcontrol.add(self.tabDetalle, text="Detalle de consumo")

        # Creo la pagina de consumo por estacion y usuario
        self.tabResumenEstacion = self.crear_resumenEstacion(self.tabcontrol)
        self.tabcontrol.add(self.tabResumenEstacion, text="Consumo por Estacion/Usuario")

        # Creo la pagina de consumo por usuario
        self.tabResumenUsuario = self.crear_resumenUsuario(self.tabcontrol)
        self.tabcontrol.add(self.tabResumenUsuario, text="Consumo por Usuario")

        # Creo la pagina de consumo general
        self.tabResumenGeneral = self.crear_resumenGeneral(self.tabcontrol)
        self.tabcontrol.add(self.tabResumenGeneral, text="Resumen General")

        # Creo la pagina de acerca de
        self.tabAcercaDe = self.crear_acercaDe(self.tabcontrol)
        self.tabcontrol.add(self.tabAcercaDe, text="Acerca de")


        self.tabcontrol.grid(row=0, sticky='nsew')


        # ------------------------------ Statusbar ------------------------------
        self.status = StringVar()
        self.status.set("Estado: Listo")
        self.statusbar = Label(self.parent, textvariable=self.status, bd=1, relief=FLAT)
        self.statusbar.grid(row=1, sticky='w')



    def about(self):
        messagebox.showinfo("Log Server Analisis", "Log Server Analisis")



    def insert_data(self):
        FILEOPENOPTIONS = dict(defaultextension=".log", initialdir="C:\\", filetypes=[('log file', '*.log')])
        LOGFile = filedialog.askopenfilename(**FILEOPENOPTIONS)
        # print('none' if len(filename)==0 else filename)

        # Array para el contenido del archivo log
        contentList = []
        iLine = 0

        #Creo estylo
        self.treeview.tag_configure(tagname='TOT_ESTACION', background='blue')
        self.treeview.tag_configure(tagname='TOT_GENERAL', background='red')

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 11, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders


        if (len(LOGFile) > 0):
            # Abro archivo ,obtengo lineas de contenido y cierro archivo
            f = open(LOGFile, 'r')
            contentList = f.readlines()
            f.close()

            # Si hay contenido creo un archivo csv y proceso
            if (len(contentList) > 0):

                sEstacion = ''
                sCliente = ''
                sFecha_IN = ''
                sFecha_OUT = ''
                sUsuario = ''

                sSegundos = '0'
                sMinutos = '0'
                sHoras = '0'
                nSegundos = 0
                sBytes = '0'
                nBytes = 0
                sConexiones = '0'
                nConexiones = 0


                iIndex1 = -1
                iIndex2 = -1

                # Creo el diccionario de datos
                log = {}
                iTotalLine=len(contentList)

                for line in contentList:
                    iLine += 1

                    if ((int((iLine/iTotalLine)*100) % 10) == 0) :
                        self.status.set("Estado: procesando " + "{:6,.2f}".format(((iLine/iTotalLine) * 100)) + '%')
                        self.parent.update_idletasks()


                    # Si el cliente es aceptado
                    if (line.find(':Connection Handler] Accepted client') > 0):
                        # print(line)

                        # Busco <fecha y hora>
                        iIndex1 = line.find('[', 0)
                        iIndex2 = line.find(']', iIndex1)
                        sFecha_IN = line[iIndex1 + 1: iIndex2].strip()

                        # Busco <cliente>
                        iIndex1 = iIndex2
                        iIndex1 = line.find(':Connection Handler] Accepted client', iIndex1)
                        iIndex2 = line.find('[', iIndex1 + 36)
                        sCliente = line[iIndex1 + 36:iIndex2].strip()

                        # Busco <usuario>
                        iIndex1 = iIndex2
                        iIndex1 = line.find('[', iIndex1)
                        iIndex2 = line.find(']', iIndex1)
                        sUsuario = line[iIndex1 + 1:iIndex2].strip()

                        # Busco <estacion>
                        iIndex1 = line.find('] on mountpoint [/')
                        iIndex2 = line.find('].', iIndex1)
                        sEstacion = line[iIndex1 + 18:iIndex2].strip()

                        sSegundos = '0'
                        sMinutos = '0'
                        sHoras = '0'
                        nSegundos = 0
                        sBytes = '0'
                        nBytes = 0
                        sConexiones = '0'
                        nConexiones = 0

                        # print('ACCEPTED ==> Fecha: %s, Estacion: %s, Cliente: %s, Usuario: %s, Segundos: %s, Bytes: %s, Conexiones: %s' % (sFecha_IN, sEstacion, sCliente, sUsuario, sSegundos, sBytes, sConexiones))
                        log.setdefault('fecha_in', []).append(datetime.strptime(sFecha_IN, '%d/%b/%Y:%H:%M:%S'))
                        log.setdefault('fecha_out', []).append('')
                        log.setdefault('estacion', []).append(sEstacion)
                        log.setdefault('cliente', []).append(int(sCliente))
                        log.setdefault('usuario', []).append(sUsuario)
                        log.setdefault('tiempo', []).append(nSegundos)
                        log.setdefault('bytes', []).append(nBytes)
                        log.setdefault('consumo', []).append( 0 if nSegundos==0 else  nBytes/nSegundos)
                        log.setdefault('conexiones', []).append(nConexiones)


                    # Si el cliente es desconectado
                    if (line.find(':Source Thread] Kicking client') > 0):
                        nSegundos = 0
                        # Busco <fecha y hora>
                        iIndex1 = line.find('[', 0)
                        iIndex2 = line.find(']', iIndex1)
                        sFecha_OUT = line[iIndex1 + 1: iIndex2].strip()

                        # Busco <cliente>
                        iIndex1 = iIndex2
                        iIndex1 = line.find(':Source Thread] Kicking client', iIndex1)
                        iIndex2 = line.find('[', iIndex1 + 30)
                        sCliente = line[iIndex1 + 30:iIndex2].strip()

                        # Busco <usuario>
                        iIndex1 = iIndex2
                        iIndex1 = line.find('[', iIndex1)
                        iIndex2 = line.find(']', iIndex1)
                        sUsuario = line[iIndex1 + 1:iIndex2].strip()

                        # Busco <segundos>
                        iIndex1 = iIndex2
                        iIndex1 = line.find('[listener], connected for', iIndex1)

                        if (line.find('hours', iIndex1)) > 0:  # convierto hora, minuto a segundos
                            iIndex2 = line.find('hours', iIndex1)
                            sHoras = line[iIndex1 + 25:iIndex2].strip()
                            nSegundos += int(sHoras) * 60 * 60

                            iIndex1 = iIndex2 + 6  # hours,  = 6 chars
                            iIndex2 = line.find('minutes', iIndex1)
                            sMinutos = '0' if iIndex2 < 0 else line[iIndex1:iIndex2].strip()
                            nSegundos += int(sMinutos) * 60

                            if line.find('minutes and') > 0:
                                iIndex1 = iIndex2 + 11  # minutes and = 11 chars
                            elif line.find('minutes,') > 0:
                                iIndex1 = iIndex2 + 8  # minutes, = 8 chars

                            iIndex2 = line.find('seconds', iIndex1)
                            sSegundos = '0' if iIndex2 < 0 else line[
                                                                iIndex1:iIndex2].strip()  # sino encuentro minutos asumo 0 segundos
                            nSegundos += int(sSegundos)

                            iIndex2 = iIndex1 if iIndex2 < 0 else iIndex2


                        elif (line.find('minutes', iIndex1)) > 0:  # convierto minutos a segundos
                            iIndex2 = line.find('minutes', iIndex1)
                            sMinutos = line[iIndex1 + 25:iIndex2].strip()
                            nSegundos += int(sMinutos) * 60

                            if line.find('minutes and') > 0:
                                iIndex1 = iIndex2 + 11  # minutes and = 11 chars
                            elif line.find('minutes,') > 0:
                                iIndex1 = iIndex2 + 8  # minutes, = 8 chars

                            iIndex2 = line.find('seconds', iIndex1)
                            sSegundos = '0' if iIndex2 < 0 else line[
                                                                iIndex1:iIndex2].strip()  # sino encuentro minutos asumo 0 segundos
                            nSegundos += int(sSegundos)

                            iIndex2 = iIndex1 if iIndex2 < 0 else iIndex2

                        elif (line.find('seconds', iIndex1)) > 0:
                            iIndex2 = line.find('seconds', iIndex1)
                            sSegundos = line[iIndex1 + 25:iIndex2].strip()
                            nSegundos += int(sSegundos)

                        iIndex2 = iIndex1 if iIndex2 < 0 else iIndex2

                        iIndex1 = iIndex2 - 2
                        iIndex2 = line.find(', ', iIndex1)

                        # Busco <bytes>
                        iIndex1 = iIndex2
                        iIndex2 = line.find('bytes transfered.', iIndex1)
                        sBytes = line[iIndex1 + 1:iIndex2].strip()
                        nBytes = int(sBytes)

                        # Busco <conexiones>
                        iIndex1 = iIndex2
                        iIndex2 = line.find('clients connected', iIndex1)
                        sConexiones = line[iIndex1 + 17:iIndex2].strip()
                        nConexiones = int(sConexiones) + 1

                        # print('KICKING ==> Fecha: %s, Estacion: %s, Cliente: %s, Usuario: %s, Segundos: %i, Bytes: %s, Conexiones: %s' % (sFecha_IN, sEstacion, sCliente, sUsuario, nSegundos, sBytes, sConexiones))

                        log.setdefault('fecha_in', []).append(datetime.strptime(sFecha_IN, '%d/%b/%Y:%H:%M:%S'))
                        log.setdefault('fecha_out', []).append(datetime.strptime(sFecha_OUT, '%d/%b/%Y:%H:%M:%S'))
                        log.setdefault('estacion', []).append(sEstacion)
                        log.setdefault('cliente', []).append(int(sCliente))
                        log.setdefault('usuario', []).append(sUsuario)
                        log.setdefault('tiempo', []).append(nSegundos)
                        log.setdefault('bytes', []).append(nBytes)
                        log.setdefault('consumo', []).append( 0 if nSegundos==0 else  nBytes/nSegundos)
                        log.setdefault('conexiones', []).append(nConexiones)

            # Creo un data-frame
            df = pd.DataFrame(log, columns=('fecha_in', 'fecha_out', 'estacion', 'cliente', 'usuario', 'tiempo', 'bytes', 'consumo', 'conexiones'))

            # Ordeno por fecha de conexion
            df2 = df.sort_values(by=['cliente', 'usuario', 'fecha_in'], ascending=True)
            df2.shape
            #print(df2)

            # Actualiza la fecha de conexion
            isNaT=True
            fechaConexion = pd.NaT
            for index, row in df2.iterrows():
                if isNaT:
                    fechaConexion=row['fecha_in']
                    isNaT= False #if row['fecha_out'] == pd.NaT else True
                else:
                    df2.loc[row.name, 'fecha_in'] = fechaConexion
                    fechaConexion=''
                    isNaT = True




            #------------------------------------------------------ PROCESO DETALLE ------------------------------------------------------
            #Contadores para usarios y estaciones
            usuarios_2_3 = 0
            usuarios_3_0 = 0
            #Ordeno por fecha de conexion y excluyo los que tengan fecha de desconexion en nulo
            df3 = df2[df2['fecha_out'].notnull()].sort_values(by=['fecha_in'], ascending=True)
            df3.shape
            #print(df3)


            #Relleno el TreeView
            for index, row in df3.iterrows():

                #Contar usuarios segun estacion
                if row['estacion'][len(row['estacion'])-1:len(row['estacion'])]=='0':
                    usuarios_2_3 += 1
                elif row['estacion'][len(row['estacion'])-1:len(row['estacion'])]=='1':
                    usuarios_3_0 += 1


                #Inserto cada linea de detalle
                self.tabDetalle.insert('', 'end', text=row['fecha_in'], values=(
                                                                        row['fecha_out'],
                                                                        row['estacion'],
                                                                        row['cliente'],
                                                                        row['usuario'],
                                                                        "{:6,.0f}".format(row['tiempo']),
                                                                        "{:6,.0f}".format(row['bytes']),
                                                                        "{:8,.4f}".format(row['consumo']),
                                                                        "{:6,.0f}".format(row['conexiones'])
                                                                        )
                                    )

            #------------------------------------------------------ PROCESO RESUMEN POR ESTACION/USUARIO------------------------------------------------------
            # Agrupo el dataframe
            grouped = df.groupby(['estacion', 'usuario']).sum()
            #print(grouped)

            nTiempoGeneral = 0
            nBytesGeneral = 0
            nConexionesGeneral = 0

            nTiempoEstacion = 0
            nBytesEstacion = 0
            nConexionesEstacion = 0

            estacionCTRL=''

            estaciones_2_3 = 0
            estaciones_3_0 = 0

            usuarios_2_3 = {}
            usuarios_3_0 = {}

            conexiones_2_3 = 0
            conexiones_3_0 = 0

            nTiempo_2_3 = 0
            nTiempo_3_0 = 0

            nBytes_2_3 = 0
            nBytes_3_0 = 0


            for index, row in grouped.iterrows():

                #Quiebre de control para cada estacion
                if (estacionCTRL != row.name[0]):

                    #Acumulo los totales de cada estacion en el total general
                    nTiempoGeneral += nTiempoEstacion
                    nBytesGeneral += nBytesEstacion
                    nConexionesGeneral += nConexionesEstacion

                    #Inserto el total de cada estacion
                    if len(estacionCTRL) > 0:

                        # Contador de estaciones
                        if estacionCTRL[len(estacionCTRL) - 1:len(estacionCTRL)] == '0':
                            estaciones_2_3 += 1
                        elif estacionCTRL[len(estacionCTRL) - 1:len(estacionCTRL)] == '1':
                            estaciones_3_0 += 1


                        self.tabResumenEstacion.insert('', 'end', text='', values=(
                                                                                ('TOTAL '+estacionCTRL+' --->'),
                                                                                "{:6,.0f}".format(nTiempoEstacion),
                                                                                "{:6,.0f}".format(nBytesEstacion),
                                                                                "{:8.4f}".format(0 if nTiempoEstacion==0 else nBytesEstacion/nTiempoEstacion),
                                                                                "{:6,.0f}".format(nConexionesEstacion)
                                                                            ),
                                                tags=('TOT_ESTACION',)
                                               )

                    #Actualizo la estacion actual
                    estacionCTRL = row.name[0]

                    #Limpio acumuladores de Estacion
                    nTiempoEstacion = 0
                    nBytesEstacion = 0
                    nConexionesEstacion = 0
                    nConsumoEstacion = 0


                # Contador de estaciones, conexiones, tiempo y bytes
                if estacionCTRL[len(estacionCTRL) - 1:len(estacionCTRL)] == '0':
                    conexiones_2_3 += row['conexiones'] #Cuento las conexiones segun estacion
                    nTiempo_2_3 += row['tiempo']
                    nBytes_2_3 += row['bytes']

                    if row.name[1] in usuarios_2_3:
                        pass
                    else:
                        usuarios_2_3.setdefault('usuario_2_3', []).append(row.name[1])

                elif estacionCTRL[len(estacionCTRL) - 1:len(estacionCTRL)] == '1':
                    conexiones_3_0 += row['conexiones'] #Cuento las conexiones segun estacion
                    nTiempo_3_0 += row['tiempo']
                    nBytes_3_0 += row['bytes']

                    if row.name[1] in usuarios_3_0:
                        pass
                    else:
                        usuarios_3_0.setdefault('usuario_3_0', []).append(row.name[1])


                #Inserto usuario
                self.tabResumenEstacion.insert('', 'end', text=row.name[0], values=(
                                                                                row.name[1],
                                                                                "{:6,.0f}".format(row['tiempo']),
                                                                                "{:6,.0f}".format(row['bytes']),
                                                                                "{:8.4f}".format(0 if row['tiempo']==0 else row['bytes']/row['tiempo']) ,
                                                                                "{:6,.0f}".format(row['conexiones'])
                                                                           )
                                       )


                #Acumulo valores de usario en los totales de estacion
                nTiempoEstacion += row['tiempo']
                nBytesEstacion += row['bytes']
                nConexionesEstacion += row['conexiones']



            #Elimino usuarios duplicados terminada la iteracion de los grupos
            new_usuarios_2_3 = {a: list(set(b)) for a, b in usuarios_2_3.items()}
            new_usuarios_3_0 = {a: list(set(b)) for a, b in usuarios_3_0.items()}
            print(new_usuarios_2_3)
            print(new_usuarios_3_0)


            #Inserto ultimo registro
            if len(estacionCTRL) > 0:

                #Contador de estaciones
                if estacionCTRL[len(estacionCTRL) - 1:len(estacionCTRL)] == '0':
                    estaciones_2_3 += 1
                elif estacionCTRL[len(estacionCTRL) - 1:len(estacionCTRL)] == '1':
                    estaciones_3_0 += 1

                self.tabResumenEstacion.insert('', 'end', text='', values=(
                                                                        ('TOTAL ' + estacionCTRL + ' --->'),
                                                                        "{:6,.0f}".format(nTiempoEstacion),
                                                                        "{:6,.0f}".format(nBytesEstacion),
                                                                        "{:8.4f}".format(0 if nTiempoEstacion == 0 else nBytesEstacion / nTiempoEstacion),
                                                                        "{:6,.0f}".format(nConexionesEstacion)
                                                                  ),
                                       tags=('TOT_ESTACION',)
                                       )


            # Acumulo los totales de cada estacion en el total general al procesar ultimo registro
            nTiempoGeneral += nTiempoEstacion
            nBytesGeneral += nBytesEstacion
            nConexionesGeneral += nConexionesEstacion

            #Inserto el totales general
            if len(estacionCTRL) > 0:
                self.tabResumenEstacion.insert('', 'end', text='TOTAL GENERAL --->', values=(
                                                                                        '',
                                                                                        "{:6,.0f}".format(nTiempoGeneral),
                                                                                        "{:6,.0f}".format(nBytesGeneral),
                                                                                        "{:8.4f}".format(0 if nTiempoGeneral == 0 else nBytesGeneral / nTiempoGeneral),
                                                                                        "{:6,.0f}".format(nConexionesGeneral)
                                                                                    ),
                                       tags=('TOT_GENERAL',)
                                       )




            #------------------------------------------------------ PROCESO RESUMEN POR USUARIO------------------------------------------------------
            # Agrupo el dataframe
            grouped2 = df.groupby(['usuario']).sum()
            #print(grouped2)

            #Inicializo totales
            nTiempoGeneral = 0
            nBytesGeneral = 0
            nConexionesGeneral = 0


            for index, row in grouped2.iterrows():
                # Inserto usuario
                self.tabResumenUsuario.insert('', 'end', text=row.name, values=(
                                                                                    "{:6,.0f}".format(row['tiempo']),
                                                                                    "{:6,.0f}".format(row['bytes']),
                                                                                    "{:8.4f}".format(0 if row['tiempo'] == 0 else row['bytes'] / row['tiempo']),
                                                                                    "{:6,.0f}".format(row['conexiones'])
                                                                                    )
                                               )

                #Acumulo en totales
                nTiempoGeneral += row['tiempo']
                nBytesGeneral += row['bytes']
                nConexionesGeneral += row['conexiones']



            # Inserto total general
            self.tabResumenUsuario.insert('', 'end', text='TOTAL GENERAL --->', values=(
                                                                                    "{:6,.0f}".format(nTiempoGeneral),
                                                                                    "{:6,.0f}".format(nBytesGeneral),
                                                                                    "{:8.4f}".format(0 if nTiempoGeneral == 0 else nBytesGeneral / nTiempoGeneral),
                                                                                    "{:6,.0f}".format(nConexionesGeneral)
                                                                                ),
                                   tags=('TOT_GENERAL',)
                                   )

            # Inserto total general de usuarios
            self.tabResumenUsuario.insert('', 'end', text='TOTAL USUARIOS ---> ' + "{:6,.0f}".format(len(grouped2) ),
                                   tags=('TOT_GENERAL',)
                                   )

            #------------------------------------------------------ PROCESO RESUMEN GENERAL------------------------------------------------------
            bytes = {}
            tiempo = {}
            consumo = {}
            usuarios = {}
            conexiones = {}
            estaciones = {}


            # USUARIOS
            if 'usuario_2_3' in new_usuarios_2_3:
                usuarios.setdefault('factor', []).append('Usuarios')
                usuarios.setdefault('rtcm_2_3', []).append(len(new_usuarios_2_3['usuario_2_3']))
                usuarios.setdefault('rtcm_3_0', []).append(0)


            if 'usuario_3_0' in new_usuarios_3_0:
                usuarios.setdefault('factor', []).append('Usuarios')
                usuarios.setdefault('rtcm_2_3', []).append(0)
                usuarios.setdefault('rtcm_3_0', []).append(len(new_usuarios_3_0['usuario_3_0']))


            # ESTACIONES
            estaciones.setdefault('factor', []).append('Estaciones')
            estaciones.setdefault('rtcm_2_3', []).append(estaciones_2_3)
            estaciones.setdefault('rtcm_3_0', []).append(0)

            estaciones.setdefault('factor', []).append('Estaciones')
            estaciones.setdefault('rtcm_2_3', []).append(0)
            estaciones.setdefault('rtcm_3_0', []).append(estaciones_3_0)


           # TIEMPO
            tiempo.setdefault('factor', []).append('Tiempo (segundos)')
            tiempo.setdefault('rtcm_2_3', []).append(nTiempo_2_3)
            tiempo.setdefault('rtcm_3_0', []).append(0)

            tiempo.setdefault('factor', []).append('Tiempo (segundos)')
            tiempo.setdefault('rtcm_2_3', []).append(0)
            tiempo.setdefault('rtcm_3_0', []).append(nTiempo_3_0)


            # BYTES
            bytes.setdefault('factor', []).append('Transferencia (bytes)')
            bytes.setdefault('rtcm_2_3', []).append(nBytes_2_3)
            bytes.setdefault('rtcm_3_0', []).append(0)

            bytes.setdefault('factor', []).append('Transferencia (bytes)')
            bytes.setdefault('rtcm_2_3', []).append(0)
            bytes.setdefault('rtcm_3_0', []).append(nBytes_3_0)


            # CONSUMO
            consumo.setdefault('factor', []).append('Consumo (b/s)')
            consumo.setdefault('rtcm_2_3', []).append(0 if nTiempo_2_3 == 0 else nBytes_2_3/nTiempo_2_3)
            consumo.setdefault('rtcm_3_0', []).append(0)

            consumo.setdefault('factor', []).append('Consumo (b/s)')
            consumo.setdefault('rtcm_2_3', []).append(0)
            consumo.setdefault('rtcm_3_0', []).append(0 if nTiempo_3_0 == 0 else nBytes_3_0/nTiempo_3_0)


            # CONEXIONES
            conexiones.setdefault('factor', []).append('Conexiones')
            conexiones.setdefault('rtcm_2_3', []).append(conexiones_2_3)
            conexiones.setdefault('rtcm_3_0', []).append(0)

            conexiones.setdefault('factor', []).append('Conexiones')
            conexiones.setdefault('rtcm_2_3', []).append(0)
            conexiones.setdefault('rtcm_3_0', []).append(conexiones_3_0)


            dfBytes = pd.DataFrame(bytes, columns=('factor', 'rtcm_2_3', 'rtcm_3_0'))
            #print(dfBytes)

            dfTiempo = pd.DataFrame(tiempo, columns=('factor', 'rtcm_2_3', 'rtcm_3_0'))
            #print(dfTiempo)

            dfConsumo = pd.DataFrame(consumo, columns=('factor', 'rtcm_2_3', 'rtcm_3_0'))
            #print(dfConsumo)

            dfUsuarios = pd.DataFrame(usuarios, columns=('factor', 'rtcm_2_3', 'rtcm_3_0'))
            #print(dfUsuarios)

            dfEstaciones = pd.DataFrame(estaciones, columns=('factor', 'rtcm_2_3', 'rtcm_3_0'))
            #print(dfEstaciones)

            dfConexiones = pd.DataFrame(conexiones, columns=('factor', 'rtcm_2_3', 'rtcm_3_0'))
            #print(dfConexiones)

            frames = [dfBytes, dfTiempo, dfConsumo, dfUsuarios, dfEstaciones, dfConexiones]
            result = pd.concat(frames)
            #print(result)

            grouped3 = result.groupby(['factor']).sum()
            #print(grouped3)
            for index, row in grouped3.iterrows():
                # Inserto usuario
                #print(row)
                self.tabResumenGeneral.insert('', 'end', text=row.name, values=(
                                                                                    "{:6,.0f}".format(row['rtcm_2_3']),
                                                                                    "{:6,.0f}".format(row['rtcm_3_0']),
                                                                                    "{:6,.0f}".format(0 if (row.name=='Usuarios' or row.name=='Estaciones' or row.name=='Consumo (b/s)') else  row['rtcm_2_3']+row['rtcm_3_0'])
                                                                                    )
                                               )





def main():
    root = Tkinter.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    #root.geometry("640x480")

    d = Window(root)
    root.mainloop()


if __name__=="__main__":
    main()