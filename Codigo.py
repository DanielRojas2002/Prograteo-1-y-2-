import sys
class Prograteo:
    
    def __init__(self,materiaPrimaIndirecta,manoDeobraIndirecta,renta,energiaElectrica,agua,telefono,seguroDeEdificio,depreciacionDeMaquinaria,seguroDeMaquinaria):
        self.__materiaPrimaIndirecta=materiaPrimaIndirecta
        self.__manoDeobraIndirecta=manoDeobraIndirecta
        self.__renta=renta
        self.__energiaElectrica=energiaElectrica
        self.__agua=agua
        self.__telefono=telefono
        self.__seguroDeEdificio=seguroDeEdificio
        self.__depreciacionDeMaquinaria=depreciacionDeMaquinaria
        self.__seguroDeMaquinaria=seguroDeMaquinaria

    
    def CalcularPrograteo1(self):
#         PREGUNTAS DEL PRODUCTIVO 1
        print("-"*100)
        print("Dime todos los datos de el productivo 1")
        MPDP1=float(input("Dime tu M.P.D del productivo1 :"))
        MODP1=float(input("Dime tu M.O.D del productivo 1 : "))
        M2P1=float(input("Dime tu M2 del productivo 1 : "))
        M3P1=float(input("Dime tu M3 del productivo 1 : "))
        ATP1=float(input("Dime tus aparatos telefonicos del productivo 1 : "))
        VMP1=float(input("Dime tu valor de maquinaria del productivo 1 : "))
        NRDMP1=float(input("Dime tu numero de requerimientos de materiales  del productivo 1 : "))
        KWP1=float(input("Dime tus KW/Hora  del productivo 1 : "))
        HMP1=float(input("Dime tus Horas Maquinaria  del productivo 1 : "))
        print("-"*100)
        
#         PREGUNTAS DEL PRODUCTIVO 2
        print("Dime todos los datos de el productivo 2")
        MPDP2=float(input("Dime tu M.P.D del productivo 2 :"))
        MODP2=float(input("Dime tu M.O.D del productivo 2 : "))
        M2P2=float(input("Dime tu M2 del productivo 2 : "))
        M3P2=float(input("Dime tu M3 del productivo 2 : "))
        ATP2=float(input("Dime tus aparatos telefonicos del productivo 2 : "))
        VMP2=float(input("Dime tu valor de maquinaria del productivo 2 : "))
        NRDMP2=float(input("Dime tu numero de requerimientos de materiales  del productivo 2 : "))
        KWP2=float(input("Dime tus KW/Hora  del productivo 2 : "))
        HMP2=float(input("Dime tus Horas Maquinaria  del productivo 2 : "))
        print("-"*100)
        
#         PREGUNTAS DEL PRODUCTIVO 3
        print("Dime todos los datos de el productivo 3")
        MPDP3=float(input("Dime tu M.P.D del productivo 3 :"))
        MODP3=float(input("Dime tu M.O.D del productivo 3 : "))
        M2P3=float(input("Dime tu M2 del productivo 3 : "))
        M3P3=float(input("Dime tu M3 del productivo 3 : "))
        ATP3=float(input("Dime tus aparatos telefonicos del productivo 3 : "))
        VMP3=float(input("Dime tu valor de maquinaria del productivo 3 : "))
        NRDMP3=float(input("Dime tu numero de requerimientos de materiales  del productivo 3 : "))
        KWP3=float(input("Dime tus KW/Hora  del productivo 3 : "))
        HMP3=float(input("Dime tus Horas Maquinaria  del productivo 3 : "))
        print("-"*100)
        
#         PREGUNTAS DEL PRODUCTIVO 4
        print("Dime todos los datos de el productivo 4")
        MPDP4=float(input("Dime tu M.P.D del productivo 4 :"))
        MODP4=float(input("Dime tu M.O.D del productivo 4 : "))
        M2P4=float(input("Dime tu M2 del productivo 4 : "))
        M3P4=float(input("Dime tu M3 del productivo 4 : "))
        ATP4=float(input("Dime tus aparatos telefonicos del productivo 4 : "))
        VMP4=float(input("Dime tu valor de maquinaria del productivo 4 : "))
        NRDMP4=float(input("Dime tu numero de requerimientos de materiales  del productivo 4 : "))
        KWP4=float(input("Dime tus KW/Hora  del productivo 4 : "))
        HMP4=float(input("Dime tus Horas Maquinaria  del productivo 4 : "))
        print("-"*100)
        
#         PREGUNTAS DEL ALAMCEN DE MATERIALES
        print("Dime todos los datos del Almacen de materiales ")
        MPDAM=float(input("Dime tu M.P.D del almacen de materiales:"))
        MODAM=float(input("Dime tu M.O.D del almacen de materiales : "))
        M2AM=float(input("Dime tu M2 del almacen de materiales : "))
        M3AM=float(input("Dime tu M3 del almacen de materiales : "))
        ATAM=float(input("Dime tus aparatos telefonicos del almacen de materiales : "))
        VMAM=float(input("Dime tu valor de maquinaria del almacen de materiales : "))
        NRDMAM=float(input("Dime tu numero de requerimientos de materiales  del almacen de materiales : "))
        KWAM=float(input("Dime tus KW/Hora  del almacen de materiales : "))
        HMAM=float(input("Dime tus Horas Maquinaria  del almacen de materiales : "))
        print("-"*100)
        
#         PREGUNTAS DEL ASEO Y LIMPIEZA
        print("Dime todos los datos de Aseo y Limpieza ")
        MPDAL=float(input("Dime tu M.P.D del aseo y limpieza:"))
        MODAL=float(input("Dime tu M.O.D del aseo y limpieza : "))
        M2AL=float(input("Dime tu M2 del aseo y limpieza : "))
        M3AL=float(input("Dime tu M3 del aseo y limpieza: "))
        ATAL=float(input("Dime tus aparatos telefonicos del aseo y limpieza : "))
        VMAL=float(input("Dime tu valor de maquinaria del aseo y limpieza : "))
        NRDMAL=float(input("Dime tu numero de requerimientos de materiales  del aseo y limpieza : "))
        KWAL=float(input("Dime tus KW/Hora  del aseo y limpieza : "))
        HMAL=float(input("Dime tus Horas Maquinaria  del aseo y limpieza : "))
        print("-"*100)
        
#         PREGUNTAS DEL MANTENIMIENTO
        print("Dime todos los datos del Mantenimiento")
        MPDM=float(input("Dime tu M.P.D del Mantenimiento:"))
        MODM=float(input("Dime tu M.O.D del Mantenimiento : "))
        M2M=float(input("Dime tu M2 del Mantenimiento: "))
        M3M=float(input("Dime tu M3 del Mantenimiento: "))
        ATM=float(input("Dime tus aparatos telefonicos del Mantenimiento : "))
        VMM=float(input("Dime tu valor de maquinaria del Mantenimiento: "))
        NRDMM=float(input("Dime tu numero de requerimientos de materiales  del Mantenimiento : "))
        KWM=float(input("Dime tus KW/Hora  del Mantenimiento: "))
        HMM=float(input("Dime tus Horas Maquinaria  del Mantenimiento : "))
        print("-"*100)

        #Estos son la variables donde se guarda las sumas de todos los campos
        SumaMPD=(MPDP1+MPDP2+MPDP3+MPDP4+MPDAM+MPDAL+MPDM)
        SumaMOD=(MODP1+MODP2+MODP3+MODP4+MODAM+MODAL+MODM)
        SumaM2=(M2P1+M2P2+M2P3+M2P4+M2AM+M2AL+M2M)
        SumaM3=(M3P1+M3P2+M3P3+M3P4+M3AM+M3AL+M3M)
        SumaAT=(ATP1+ATP2+ATP3+ATP4+ATAM+ATAL+ATM)
        SumaVM=(VMP1+VMP2+VMP3+VMP4+VMAM+VMAL+VMM)
        SumaNRDM=(NRDMP1+NRDMP2+NRDMP3+NRDMP4+NRDMAM+NRDMAL+NRDMM)
        SumaKW=(KWP1+KWP2+KWP3+KWP4+KWAM+KWAL+KWM)
        SumaHM=(HMP1+HMP2+HMP3+HMP4+HMAM+HMAL+HMM)
        
        #Estos son las variables donde se  guarda los factores
        FactorMPD=(self.__materiaPrimaIndirecta/SumaMPD)
        FactorMOD=(self.__manoDeobraIndirecta/SumaMOD)
        FactorRenta=(self.__renta/SumaM2)
        FactorEnergia=(self.__energiaElectrica/SumaKW)
        FactorAgua=(self.__agua/SumaM3)
        FactorTelefono=(self.__telefono/ SumaAT)
        FactorSeguroE=(self.__seguroDeEdificio/SumaM2)
        FactorDepreciacionM=(self.__depreciacionDeMaquinaria/SumaVM)
        FactorSeguroM=(self.__seguroDeMaquinaria/SumaVM)
        
#         Estos son tus factores
        print("ESTOS SON TUS FACTORES : ")
        print(f"Este es tu factor del MPD :{FactorMPD}")
        print(f"Este es tu factor del MOD :{FactorMOD}")
        print(f"Este es tu factor del Renta :{FactorRenta}")
        print(f"Este es tu factor del Energia Electrica :{FactorEnergia}")
        print(f"Este es tu factor del Agua :{FactorAgua}")
        print(f"Este es tu factor del Telefono :{FactorTelefono}")
        print(f"Este es tu factor del Seguro de Edificio :{FactorSeguroE}")
        print(f"Este es tu factor del Depreciacion de Maquinaria :{FactorDepreciacionM}")
        print(f"Este es tu factor del Seguro de Maquinaria :{FactorSeguroM}")
        print("-"*100)
        
        #Estas son las variables donde se guardan las respuestas del productivo 1
        RespuestaP1PI=(FactorMPD*MPDP1)
        RespuestaP1OI=(FactorMOD*MODP1)
        RespuestaP1R=(FactorRenta*M2P1)
        RespuestaP1EE=(FactorEnergia*KWP1)
        RespuestaP1A=(FactorAgua*M3P1)
        RespuestaP1T=(FactorTelefono*ATP1)
        RespuestaP1SE=(FactorSeguroE*M2P1)
        RespuestaP1DM=(FactorDepreciacionM*VMP1)
        RespuestaP1SM=(FactorSeguroM*VMP1)
        
        #Estas son las variables donde se guardan las respuestas del productivo 2
        RespuestaP2PI=(FactorMPD*MPDP2)
        RespuestaP2OI=(FactorMOD*MODP2)
        RespuestaP2R=(FactorRenta*M2P2)
        RespuestaP2EE=(FactorEnergia*KWP2)
        RespuestaP2A=(FactorAgua*M3P2)
        RespuestaP2T=(FactorTelefono*ATP2)
        RespuestaP2SE=(FactorSeguroE*M2P2)
        RespuestaP2DM=(FactorDepreciacionM*VMP2)
        RespuestaP2SM=(FactorSeguroM*VMP2)
        
        
        
        #Estas son las variables donde se guardan las respuestas del productivo 3
        RespuestaP3PI=(FactorMPD*MPDP3)
        RespuestaP3OI=(FactorMOD*MODP3)
        RespuestaP3R=(FactorRenta*M2P3)
        RespuestaP3EE=(FactorEnergia*KWP3)
        RespuestaP3A=(FactorAgua*M3P3)
        RespuestaP3T=(FactorTelefono*ATP3)
        RespuestaP3SE=(FactorSeguroE*M2P3)
        RespuestaP3DM=(FactorDepreciacionM*VMP3)
        RespuestaP3SM=(FactorSeguroM*VMP3)
        
        #Estas son las variables donde se guardan las respuestas del productivo 4
        RespuestaP4PI=(FactorMPD*MPDP4)
        RespuestaP4OI=(FactorMOD*MODP4)
        RespuestaP4R=(FactorRenta*M2P4)
        RespuestaP4EE=(FactorEnergia*KWP4)
        RespuestaP4A=(FactorAgua*M3P4)
        RespuestaP4T=(FactorTelefono*ATP4)
        RespuestaP4SE=(FactorSeguroE*M2P4)
        RespuestaP4DM=(FactorDepreciacionM*VMP4)
        RespuestaP4SM=(FactorSeguroM*VMP4)
        
        #Estas son las variables donde se guardan las respuestas del Alamacen de materiales
        RespuestaAMPI=(FactorMPD*MPDAM)
        RespuestaAMOI=(FactorMOD*MODAM)
        RespuestaAMR=(FactorRenta*M2AM)
        RespuestaAMEE=(FactorEnergia*KWAM)
        RespuestaAMA=(FactorAgua*M3AM)
        RespuestaAMT=(FactorTelefono*ATAM)
        RespuestaAMSE=(FactorSeguroE*M2AM)
        RespuestaAMDM=(FactorDepreciacionM*VMAM)
        RespuestaAMSM=(FactorSeguroM*VMAM)
        
        #Estas son las variables donde se guardan las respuestas del Aseo y Limpieza
        RespuestaALPI=(FactorMPD*MPDAL)
        RespuestaALOI=(FactorMOD*MODAL)
        RespuestaALR=(FactorRenta*M2AL)
        RespuestaALEE=(FactorEnergia*KWAL)
        RespuestaALA=(FactorAgua*M3AL)
        RespuestaALT=(FactorTelefono*ATAL)
        RespuestaALSE=(FactorSeguroE*M2AL)
        RespuestaALDM=(FactorDepreciacionM*VMAL)
        RespuestaALSM=(FactorSeguroM*VMAL)
        
        #Estas son las variables donde se guardan las respuestas del Mantenimineto
        RespuestaMPI=(FactorMPD*MPDM)
        RespuestaMOI=(FactorMOD*MODM)
        RespuestaMR=(FactorRenta*M2M)
        RespuestaMEE=(FactorEnergia*KWM)
        RespuestaMA=(FactorAgua*M3M)
        RespuestaMT=(FactorTelefono*ATM)
        RespuestaMSE=(FactorSeguroE*M2M)
        RespuestaMDM=(FactorDepreciacionM*VMM)
        RespuestaMSM=(FactorSeguroM*VMM)
        
        #Valores regresados del productivo 1
        print("Respuestas del productivo 1 ")
        print(f"Este es tu Materia Prima Indirecta : {RespuestaP1PI} ")
        print(f"Este es tu Mano de Obra Indirecta : {RespuestaP1OI} " )
        print(f"Este es tu Renta  : { RespuestaP1R} " )
        print(f"Este es tu Energia Electrica : {RespuestaP1EE} " )
        print(f"Este es tu Agua  : {RespuestaP1A} " )
        print(f"Este es tu Telefono : {RespuestaP1T} " )
        print(f"Este es tu Seguro de Edificio : {RespuestaP1SE} " )
        print(f"Este es tu Depreciacion de Maquinaria  : {RespuestaP1DM} " )
        print(f"Este es tu Seguro de Maquinaria   : {RespuestaP1SM} " )
        print("-"*30)
        
#         VALORES REGRESADOS DEL PRODUCTIVO 2
        print("Respuestas del productivo 2 ")
        print(f"Este es tu Materia Prima Indirecta : {RespuestaP2PI} ")
        print(f"Este es tu Mano de Obra Indirecta : {RespuestaP2OI} " )
        print(f"Este es tu Renta  : { RespuestaP2R} " )
        print(f"Este es tu Energia Electrica : {RespuestaP2EE} " )
        print(f"Este es tu Agua  : {RespuestaP2A} " )
        print(f"Este es tu Telefono : {RespuestaP2T} " )
        print(f"Este es tu Seguro de Edificio : {RespuestaP2SE} " )
        print(f"Este es tu Depreciacion de Maquinaria  : {RespuestaP2DM} " )
        print(f"Este es tu Seguro de Maquinaria   : {RespuestaP2SM} " )
        print("-"*30)
        
#         VALORES REGRESADOS DEL PRODUCTIVO 3
        print("Respuestas del productivo 3")
        print(f"Este es tu Materia Prima Indirecta : {RespuestaP3PI} ")
        print(f"Este es tu Mano de Obra Indirecta : {RespuestaP3OI} " )
        print(f"Este es tu Renta  : { RespuestaP3R} " )
        print(f"Este es tu Energia Electrica : {RespuestaP3EE} " )
        print(f"Este es tu Agua  : {RespuestaP3A} " )
        print(f"Este es tu Telefono : {RespuestaP3T} " )
        print(f"Este es tu Seguro de Edificio : {RespuestaP3SE} " )
        print(f"Este es tu Depreciacion de Maquinaria  : {RespuestaP3DM} " )
        print(f"Este es tu Seguro de Maquinaria   : {RespuestaP3SM} " )
        print("-"*30)
        
#         VALORES REGRESADOS DEL PRODUCTIVO 4
        print("Respuestas del productivo 4 ")
        print(f"Este es tu Materia Prima Indirecta : {RespuestaP4PI} ")
        print(f"Este es tu Mano de Obra Indirecta : {RespuestaP4OI} " )
        print(f"Este es tu Renta  : { RespuestaP4R} " )
        print(f"Este es tu Energia Electrica : {RespuestaP4EE} " )
        print(f"Este es tu Agua  : {RespuestaP4A} " )
        print(f"Este es tu Telefono : {RespuestaP4T} " )
        print(f"Este es tu Seguro de Edificio : {RespuestaP4SE} " )
        print(f"Este es tu Depreciacion de Maquinaria  : {RespuestaP4DM} " )
        print(f"Este es tu Seguro de Maquinaria   : {RespuestaP4SM} " )
        print("-"*30)
        
#         VALORES REGRESADOS DEL ALMACEN DE MATERIALES
        print("Respuestas del Almacen de Materiales ")
        print(f"Este es tu Materia Prima Indirecta : {RespuestaAMPI} ")
        print(f"Este es tu Mano de Obra Indirecta : {RespuestaAMOI} " )
        print(f"Este es tu Renta  : { RespuestaAMR} " )
        print(f"Este es tu Energia Electrica : {RespuestaAMEE} " )
        print(f"Este es tu Agua  : {RespuestaAMA} " )
        print(f"Este es tu Telefono : {RespuestaAMT} " )
        print(f"Este es tu Seguro de Edificio : {RespuestaAMSE} " )
        print(f"Este es tu Depreciacion de Maquinaria  : {RespuestaAMDM} " )
        print(f"Este es tu Seguro de Maquinaria   : {RespuestaAMSM} " )
        print("-"*30)
        
#         VALORES REGRESADOS DEL ASEO Y LIMPIEZA
        print("Respuestas del Aseo y Limpieza ")
        print(f"Este es tu Materia Prima Indirecta : {RespuestaALPI} ")
        print(f"Este es tu Mano de Obra Indirecta : {RespuestaALOI} " )
        print(f"Este es tu Renta  : { RespuestaALR} " )
        print(f"Este es tu Energia Electrica : {RespuestaALEE} " )
        print(f"Este es tu Agua  : {RespuestaALA} " )
        print(f"Este es tu Telefono : {RespuestaALT} " )
        print(f"Este es tu Seguro de Edificio : {RespuestaALSE} " )
        print(f"Este es tu Depreciacion de Maquinaria  : {RespuestaALDM} " )
        print(f"Este es tu Seguro de Maquinaria   : {RespuestaALSM} " )
        print("-"*30)
        
#         VALORES REGRESADOS DEL MANTENIMIENTO
        print("Respuestas del Mantenimiento")
        print(f"Este es tu Materia Prima Indirecta : {RespuestaMPI} ")
        print(f"Este es tu Mano de Obra Indirecta : {RespuestaMOI} " )
        print(f"Este es tu Renta  : { RespuestaMR} " )
        print(f"Este es tu Energia Electrica : {RespuestaMEE} " )
        print(f"Este es tu Agua  : {RespuestaMA} " )
        print(f"Este es tu Telefono : {RespuestaMT} " )
        print(f"Este es tu Seguro de Edificio : {RespuestaMSE} " )
        print(f"Este es tu Depreciacion de Maquinaria  : {RespuestaMDM} " )
        print(f"Este es tu Seguro de Maquinaria   : {RespuestaMSM} " )
        
#         COMPROBACION LA SUMA DE TODOS LOS CAMPOS  DEBE SER IGUAL A LA SUMATORIA DE TODOS LOS MONTOS
        VariableSumatoria=(self.__materiaPrimaIndirecta+self.__manoDeobraIndirecta+self.__renta+self.__energiaElectrica+self.__agua+self.__telefono+self.__seguroDeEdificio+self.__depreciacionDeMaquinaria+self.__seguroDeMaquinaria)
        correcto=(RespuestaP1PI+RespuestaP1OI+RespuestaP1R+RespuestaP1EE+RespuestaP1A+RespuestaP1T+RespuestaP1SE+RespuestaP1DM+RespuestaP1SM+RespuestaP2PI+RespuestaP2OI+RespuestaP2R+RespuestaP2EE+RespuestaP2A+RespuestaP2T+RespuestaP2SE+RespuestaP2DM+RespuestaP2SM)
        correcto1=(RespuestaP3PI+RespuestaP3OI+RespuestaP3R+RespuestaP3EE+RespuestaP3A+RespuestaP3T+RespuestaP3SE+RespuestaP3DM+RespuestaP3SM+RespuestaP4PI+RespuestaP4OI+RespuestaP4R+RespuestaP4EE+RespuestaP4A+RespuestaP4T+RespuestaP4SE+RespuestaP4DM+RespuestaP4SM)
        correcto2=(RespuestaAMPI+RespuestaAMOI+RespuestaAMR+RespuestaAMEE+RespuestaAMA+RespuestaAMT+RespuestaAMSE+RespuestaAMDM+RespuestaAMSM+RespuestaALPI+RespuestaALOI+RespuestaALR+RespuestaALEE+RespuestaALA+RespuestaALT+RespuestaALSE+RespuestaALDM+RespuestaALSM)
        correcto3=(RespuestaMPI+RespuestaMOI+RespuestaMR+RespuestaMEE+RespuestaMA+RespuestaMT+RespuestaMSE+RespuestaMDM+RespuestaMSM)
        variable=(correcto+correcto1+correcto2+correcto3)
        print("-"*100)
        print("Hay una regla que si la suma de todos tus montos es igual a la sumatoria de todas las variantes de todos tus departamentos si este es igual esta bien hecho el prograteo")
        print(f"Esta es la sumatoria de todos tus montos  : {VariableSumatoria}")
        print(f"Esta es la sumatoria de todos tus departamentos :{variable}")
        
        
#         Estas variables son donde se guarda la sumatoria de todos los departamentos 
        sumatoriaP1=(RespuestaP1PI+RespuestaP1OI+RespuestaP1R+RespuestaP1EE+RespuestaP1A+RespuestaP1T+RespuestaP1SE+RespuestaP1DM+RespuestaP1SM)
        sumatoriaP2=(RespuestaP2PI+RespuestaP2OI+RespuestaP2R+RespuestaP2EE+RespuestaP2A+RespuestaP2T+RespuestaP2SE+RespuestaP2DM+RespuestaP2SM)
        sumatoriaP3=(RespuestaP3PI+RespuestaP3OI+RespuestaP3R+RespuestaP3EE+RespuestaP3A+RespuestaP3T+RespuestaP3SE+RespuestaP3DM+RespuestaP3SM)
        sumatoriaP4=(RespuestaP4PI+RespuestaP4OI+RespuestaP4R+RespuestaP4EE+RespuestaP4A+RespuestaP4T+RespuestaP4SE+RespuestaP4DM+RespuestaP4SM)
        sumatoriaAM=(RespuestaAMPI+RespuestaAMOI+RespuestaAMR+RespuestaAMEE+RespuestaAMA+RespuestaAMT+RespuestaAMSE+RespuestaAMDM+RespuestaAMSM)
        sumatoriaAL=(RespuestaALPI+RespuestaALOI+RespuestaALR+RespuestaALEE+RespuestaALA+RespuestaALT+RespuestaALSE+RespuestaALDM+RespuestaALSM)
        sumatoriaM=(RespuestaMPI+RespuestaMOI+RespuestaMR+RespuestaMEE+RespuestaMA+RespuestaMT+RespuestaMSE+RespuestaMDM+RespuestaMSM)
        sumatoriaTotal=(sumatoriaP1+sumatoriaP2+sumatoriaP3+sumatoriaP4+sumatoriaAM+sumatoriaAL+sumatoriaM)
        
        
        
#         Sumatorias para los prograteos
        sumatoriaDeM2=(M2P1+M2P2+M2P3+M2P4+M2AM+M2M+M2AL-M2AL)
        sumatoriaDeNRM=(NRDMP1+NRDMP2+NRDMP3+NRDMP4+NRDMAM+NRDMAL+NRDMM-NRDMAM-NRDMAL)
        sumatoriaDeHM=(HMP1+HMP2+HMP3+HMP4+HMAM+HMAL+HMM-HMAM-HMAL-HMM)
        
#         If de comprobacion si son iguales ambos esta bien 
        if VariableSumatoria==variable:
            print ("Tu prograteo es correcto ")
        else:
            print("Anotaste mal un dato ")
            
#         Inicializador para poder hacer el PROGRATEO 2
        print("-"*100)
        opcion=int(input("¿Deseas sacar el PROGRATEO 2 ? 1=SI 2=NO : "))
        if opcion==1:
            print("-"*20,"DEPARTAMENTOS","-"*20)
            print(f"PRODUCTIVO 1 : {sumatoriaP1}")
            print(f"PRODUCTIVO 2 :{sumatoriaP2}")
            print(f"PRODUCTIVO 3 :{sumatoriaP3}")
            print(f"PRODUCTIVO 4 :{sumatoriaP4}")
            print(f"ALMACEN DE MATERIALES:{sumatoriaAM}")
            print(f"ASEO Y LIMPIEZA:{sumatoriaAL}")
            print(f"MANTENIMIENTO:{sumatoriaM}")
            print(f"TOTAL : {sumatoriaTotal}")
            print("-"*100)
            
#             FACTORES DEL PROGRATEO 2 DEL ASEO Y LIMPIEZA
            factorAL=(sumatoriaAL/sumatoriaDeM2)
        
            
#             VARIABLES QUE GUARDAN LA APLICACION DEL ASEO Y LIMPIEZA
            AL1=(factorAL*M2P1)
            AL2=(factorAL*M2P2)
            AL3=(factorAL*M2P3)
            AL4=(factorAL*M2P4)
            AM=(factorAL*M2AM)
            AL=(sumatoriaAL)
            M=(factorAL*M2M)
            TOTAL=(AL1+AL2+AL3+AL4+AM+M-AL)
            
#           VARIABLES QUE GUARDAN EL SUBTOTAL DEL ASEO Y LIMPIEZA
            SUBP1=(sumatoriaP1+AL1)
            SUBP2=(sumatoriaP2+AL2)
            SUBP3=(sumatoriaP3+AL3)
            SUBP4=(sumatoriaP4+AL4)
            SUBAM=(sumatoriaAM+AM)
            SUBAL=0
            SUBM=(sumatoriaM+M)
            TOTAL1=(SUBP1+SUBP2+SUBP3+SUBP4+SUBAM+SUBAL+SUBM)
            
#            Factor de almacen del prograteo 2 
            factorAlmacen=(SUBAM/sumatoriaDeNRM)
            
            
#             VARIABLES QUE GUARDAN LA APLICACION DEL ALMACEN
            AM1=(factorAlmacen*NRDMP1)
            AM2=(factorAlmacen*NRDMP2)
            AM3=(factorAlmacen*NRDMP3)
            AM4=(factorAlmacen*NRDMP4)
            AM=(SUBAM)
            AMAL=0
            AMM=(factorAlmacen*NRDMM)
            TOTAL2=(AM1+AM2+AM3+AM4+AMAL+AMM-AM)
            
#             VARIABLES QUE GUARDAN EL SUBTOTAL DEL ALMACEN
            SUBAP1=(SUBP1+AM1)
            SUBAP2=(SUBP2+AM2)
            SUBAP3=(SUBP3+AM3)
            SUBAP4=(SUBP4+AM4)
            SUBAA=0
            SUBAAL=0
            SUBAM=(SUBM+AMM)
            TOTAL3=(SUBAP1+SUBAP2+SUBAP3+SUBAP4+SUBAA+SUBAAL+SUBAM)
            
            
#             FACTOR DE MANTENIMINETO DEL PROGRATEO 2
            factorMantenimiento=(SUBAM/sumatoriaDeHM)
            
#             VARIABLES QUE GUARDAN LA APLICACION DEL MANTENIMIENTO
            MAP1=(factorMantenimiento*HMP1)
            MAP2=(factorMantenimiento*HMP2)
            MAP3=(factorMantenimiento*HMP3)
            MAP4=(factorMantenimiento*HMP4)
            MAA=0
            MAAL=0
            MAM=(SUBAM)
            TOTAL4=(MAP1+MAP2+MAP3+MAP4-MAA-MAAL-MAM)
            
#             VARIABLES QUE GUARDAN EL TOTAL DEL MANTENIMIENTO
            TOTALFINALP1=(SUBAP1+MAP1)
            TOTALFINALP2=(SUBAP2+MAP2)
            TOTALFINALP3=(SUBAP3+MAP3)
            TOTALFINALP4=(SUBAP4+MAP4)
            X=0
            Y=0
            Z=0
            SUMATORIAFINAL=(TOTALFINALP1+TOTALFINALP2+TOTALFINALP3+TOTALFINALP4)
            
            
            print("-"*20,"ASEO Y LIMPIEZA","-"*20)
            print("-"*20,"APLICACION :","-"*20)
            print(f"Productivo 1 : {AL1}") 
            print(f"Productivo 2 :{AL2}")  
            print(f"Productivo 3 :{AL3}")  
            print(f"Productivo 4 :{AL4}")  
            print(f"Alamacen de Mercancia :{AM}") 
            print(f"Aseo y Limpieza :{-AL}")  
            print(f"Mantenimiento :{M}") 
            print(f"TOTAL : {TOTAL}")
            
            print("-"*20,"SUBTOTAL :","-"*20)
            print(f"Productivo 1 : {SUBP1}")
            print(f"Productivo 2 : {SUBP2}")
            print(f"Productivo 3 : {SUBP3}")
            print(f"Productivo 4 : {SUBP4}")
            print(f"Almacen de Mercancias : {SUBAM}")
            print(f"Aseo y Limpieza : {SUBAL}")
            print(f"Mantenimineto : {SUBM}")
            print(f"TOTAL : {TOTAL1}")
            
            
            
            
            print("-"*20,"ALMACEN","-"*20)
            print("-"*20,"APLICACION :","-"*20)
            print(f"Productivo 1 : {AM1}") 
            print(f"Productivo 2 :{AM2}")  
            print(f"Productivo 3 :{AM3}")  
            print(f"Productivo 4 :{AM4}")  
            print(f"Alamacen de Mercancia :{-AM}") 
            print(f"Aseo y Limpieza :{AMAL}") 
            print(f"Mantenimiento :{AMM}") 
            print(f"TOTAL : {TOTAL2}")
            
            print("-"*20,"SUBTOTAL :","-"*20)
            print(f"Productivo 1 : {SUBAP1}")
            print(f"Productivo 2 : {SUBAP2}")
            print(f"Productivo 3 : {SUBAP3}")
            print(f"Productivo 4 : {SUBAP4}")
            print(f"Almacen de Mercancias : {SUBAA}")
            print(f"Aseo y Limpieza : {SUBAAL}")
            print(f"Mantenimineto : {SUBAM}")
            print(f"TOTAL : {TOTAL3}")
            
            
            print("-"*20,"MANTENIMIENTO","-"*20)
            print("-"*20,"APLICACION :","-"*20)
            print(f"Productivo 1 : {MAP1}") 
            print(f"Productivo 2 :{MAP2}")  
            print(f"Productivo 3 :{MAP3}")  
            print(f"Productivo 4 :{MAP4}")  
            print(f"Alamacen de Mercancia :{MAA}") 
            print(f"Aseo y Limpieza :{MAAL}") 
            print(f"Mantenimiento :{-MAM}") 
            print(f"TOTAL : {TOTAL4}")
            
            print("$"*30,"TOTAL::","$"*30)
            print(f"Productivo 1 : {TOTALFINALP1}")
            print(f"Productivo 2 : {TOTALFINALP2}")
            print(f"Productivo 3 : {TOTALFINALP3}")
            print(f"Productivo 4 : {TOTALFINALP4}")
            print(f"Almacen de Mercancias : {X}")
            print(f"Aseo y Limpieza : {Y}")
            print(f"Mantenimineto : {Z}")
            print(f"TOTAL : {SUMATORIAFINAL}")


contador=0        
opcion=1
try:
        while opcion==1:
                contador=contador+1
                materiaPrimaIndirecta=float(input("Dime el monto de la Materia prima Indirecta : "))
                manoDeobraIndirecta=float(input("Dime el monto de la Mano de obra indirecta : "))
                renta=float(input("Dime tu monto de la renta : "))
                energiaElectrica=float(input("Dime tu monto de la Energia Electrica : "))
                agua=float(input("Dime tu monto del agua : "))
                telefono=float(input("Dime tu monto del telefono : "))
                seguroDeEdificio=float(input("Dime tu monto del Seguro de Edificio : "))
                depreciacionDeMaquinaria=float(input("Dime tu monto de la Depreciacion de Maquinaria : "))
                seguroDeMaquinaria=float(input("Dime tu monto del Seguro de Maquinaria : "))
    
        a=Prograteo(materiaPrimaIndirecta,manoDeobraIndirecta,renta,energiaElectrica,agua,telefono,seguroDeEdificio,depreciacionDeMaquinaria,seguroDeMaquinaria)
        a.CalcularPrograteo1()
        print(f"Numeros de personas Registradas:{contador}")
        print("-"*100)
        opcion=int(input("Deseas seguir sacando Prograteos 1=SI 2=NO  : "))

except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[0]}")
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("*"*30,"Fin del Programa","*"*30)