import public.plot_colton_graphs as pcg
import public.read_colton_files as rcf
import matplotlib.pyplot as plt
import numpy as np



def absorption_temerature_series_template():
    # Dictionary that holds all of the data with input trans
    data = {}
    data['trans'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    data['blank1'] = rcf.read_trans_data(642)

    data['trans'][15] = rcf.read_trans_data(651) # voltage_file
    data['trans'][50] = rcf.read_trans_data(650) # voltage_file
    data['trans'][100] = rcf.read_trans_data(649) #voltage_file
    data['trans'][150] = rcf.read_trans_data(648) # voltage_file
    fig, ax = plt.subplots()
    # pcg.plot_ABS_temp_series(data, ax=ax, color_map_name='rainbow', smooth=True, colorbar=False)   


    # data['trans'] = {}

    # trans and blank will have strings as their voltage value, but each voltage will be an integer
    # data['blank2'] = rcf.read_trans_data(627)

    data['trans'][200] = rcf.read_trans_data(647) # voltage_file
    data['trans'][250] = rcf.read_trans_data(646) # voltage_file
    data['trans'][300] = rcf.read_trans_data(652) # voltage_file
    
    pcg.plot_ABS_temp_series(data, ax=ax, color_map_name='rainbow', smooth=True, colorbar=True)


    # plt.savefig(fig_name, format='png', dpi=300)

    plt.show()
# absorption_temerature_series_template()

def absorption_template():
    fig, ax = plt.subplots()
    data = {} 

    # data
    data['blank'] = rcf.read_trans_data(1314)
    data['trans'] = rcf.read_trans_data(1315)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # # # data 2
    # data['blank'] = rcf.read_trans_data(1253)
    # data['trans'] = rcf.read_trans_data(1252)

    # # # plot data 2
    # pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)


    plt.show()
# absorption_template()



def absorption_reflection_template():
    fig, ax = plt.subplots()
    data_T = {}
    data_R = {}

    # data
    data_T['blank'], data_R['blank'] = rcf.read_double_lockin_data(1116)
    
    
    data_T['trans'], data_R['trans'] = rcf.read_double_lockin_data(1117)

    # plot data
    pcg.plot_absorption(data_T, ax=ax, smooth=False,energy=False)
    pcg.plot_absorption(data_R, ax=ax, smooth=False,energy=False)


    plt.show()
# absorption_reflection_template()



def Nilave50_50_abs():
    fig, ax = plt.subplots()
    data = {} 

    # data
    data['blank'] = rcf.read_trans_data(1375)
    data['trans'] = rcf.read_trans_data(1374)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # # # data 2
    # data['blank'] = rcf.read_trans_data(1253)
    # data['trans'] = rcf.read_trans_data(1252)

    # # # plot data 2
    # pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)


    plt.show()
# Nilave50_50_abs()

def CHDA():
    fig, ax = plt.subplots()
    data_T = {}
    data_R = {}

    # data
    data_T['blank'], data_R['blank'] = rcf.read_double_lockin_data(1119)
    
    
    data_T['trans'], data_R['trans'] = rcf.read_double_lockin_data(1120)

    # plot data
    pcg.plot_absorption(data_T, ax=ax, smooth=False,energy=False,legend='Abs')
    pcg.plot_absorption(data_R, ax=ax, smooth=False,energy=False,legend='Ref',color='red')


    plt.show()
# CHDA()


def CHDA2():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1134)
    
    
    data['trans'] = rcf.read_trans_data(1135)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,legend='Abs')


    plt.show()
# CHDA2()

def CHDMA_295K():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1167)
    data['trans'] = rcf.read_trans_data(1168)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # # # data 2
    data['blank'] = rcf.read_trans_data(1175)
    data['trans'] = rcf.read_trans_data(1176)

    # plot data 2
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')


    plt.show()
# CHDMA_295K()


def CHDMA_16K():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1167)
    data['trans'] = rcf.read_trans_data(1169)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # # # # data 2
    # data['blank'] = rcf.read_trans_data(1161)
    # data['trans'] = rcf.read_trans_data(1162)

    # # plot data 2
    # pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')


    plt.show()
# CHDMA_16K()


def AMP4_295K():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1199)
    data['trans'] = rcf.read_trans_data(1198)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # # # # data 2
    # data['blank'] = rcf.read_trans_data(1161)
    # data['trans'] = rcf.read_trans_data(1162)

    # # plot data 2
    # pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')


    plt.show()
# AMP4_295K()


def AMP4_16K():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1196)
    data['trans'] = rcf.read_trans_data(1202)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False, energy=True)

    plt.show()
# AMP4_16K()


def AMP4_295K_2():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1196)
    data['trans'] = rcf.read_trans_data(1197)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # # # # data 2
    data['blank'] = rcf.read_trans_data(1217)
    data['trans'] = rcf.read_trans_data(1219)

    # plot data 2
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')

    data['blank'] = rcf.read_trans_data(1217)
    data['trans'] = rcf.read_trans_data(1218)

    # plot data 2
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='black')


    plt.show()
# AMP4_295K_2()


def AMPY4_295K():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1221)
    data['trans'] = rcf.read_trans_data(1222)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)


    plt.show()
# AMPY4_295K()

def AMPY4_17K():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1221)
    data['trans'] = rcf.read_trans_data(1227)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # room temp data
    data['blank'] = rcf.read_trans_data(1221)
    data['trans'] = rcf.read_trans_data(1222)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')

    plt.show()
# AMPY4_17K()

def absorption_2mPESI():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1243)
    data['trans'] = rcf.read_trans_data(1244)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # # data 2
    # data['blank'] = rcf.read_trans_data(1094)
    # data['trans'] = rcf.read_trans_data(1097)

    # # plot data 2
    # pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)


    plt.show()
# absorption_2mPESI()


# plots made for Alice
def Alice_PM6Y6():
    fig, ax = plt.subplots()
    def PM6():
        # fig, ax = plt.subplots()
        data = {}

        # """Absorbance"""
        # # data
        # data['blank'] = rcf.read_trans_data(1016)
        # data['trans'] = rcf.read_trans_data(1014)
        # # plot data
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='blue',energy=True,legend="PM6")
        # # data 2
        # data['blank'] = rcf.read_trans_data(1015)
        # data['trans'] = rcf.read_trans_data(1013)
        # # plot data 2
        # pcg.plot_absorption(data, ax=ax, smooth=False,color="blue",energy=True)

        """Reflectance"""
        color_reflectance = 'blue'
        # data
        data['blank'] = rcf.read_trans_data(1021)
        data['trans'] = rcf.read_trans_data(1022)
        # plot data
        pcg.plot_absorption(data, ax=ax, smooth=False,energy=True, color=color_reflectance,legend="PM6")
        # data 2
        data['blank'] = rcf.read_trans_data(1024)
        data['trans'] = rcf.read_trans_data(1023)
        # plot data 2
        pcg.plot_absorption(data, ax=ax, smooth=False,energy=True, color=color_reflectance)

        # plt.show()
    PM6()

    def PM6Y6_21():
        # fig, ax = plt.subplots()
        data = {}

        # """Absorbance"""
        # # data
        # data['blank'] = rcf.read_trans_data(1065)
        # data['trans'] = rcf.read_trans_data(1066)
        # # plot data
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='black',energy=True,legend="2:1 PM6Y6")
        # # data 2
        # data['blank'] = rcf.read_trans_data(1064)
        # data['trans'] = rcf.read_trans_data(1067)
        # # plot data 2
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='black',energy=True)


        """Reflectance"""
        ax2 = ax#.twinx()
        color_reflectance = 'black'
        # data
        data['blank'] = rcf.read_trans_data(1057)
        data['trans'] = rcf.read_trans_data(1058)
        # plot data
        pcg.plot_absorption(data, ax=ax2, smooth=False,energy=True, color=color_reflectance,legend='2:1 PM6Y6')
        # data 2
        data['blank'] = rcf.read_trans_data(1056)
        data['trans'] = rcf.read_trans_data(1060)
        # plot data 2
        pcg.plot_absorption(data, ax=ax2, smooth=False,energy=True, color=color_reflectance)

        # plt.show()
    PM6Y6_21()

    def PM6Y6_112():
        # fig, ax = plt.subplots()
        data = {}

        # """Absorbance"""
        # # data
        # data['blank'] = rcf.read_trans_data(1081)
        # data['trans'] = rcf.read_trans_data(1082)
        # # plot data
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='cyan',energy=True,legend="1:1.2 PM6Y6")
        # # data 2
        # data['blank'] = rcf.read_trans_data(1080)
        # data['trans'] = rcf.read_trans_data(1083)
        # # plot data 2
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='cyan',energy=True)


        """Reflectance"""
        color_reflectance = 'cyan'
        # data
        data['blank'] = rcf.read_trans_data(1074)
        data['trans'] = rcf.read_trans_data(1076)
        # plot data
        pcg.plot_absorption(data, ax=ax, smooth=False,energy=True, color=color_reflectance,legend='1:1.2 PM6Y6')
        # data 2
        data['blank'] = rcf.read_trans_data(1073)
        data['trans'] = rcf.read_trans_data(1075)
        # plot data 2
        pcg.plot_absorption(data, ax=ax, smooth=False,energy=True, color=color_reflectance)

        # plt.show()
    PM6Y6_112()

    def PM6Y6_12():
        # fig, ax = plt.subplots()
        data = {}

        # """Absorbance"""
        # # data
        # data['blank'] = rcf.read_trans_data(1041)
        # data['trans'] = rcf.read_trans_data(1044)
        # # plot data
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='magenta',energy=True,legend="1:2 PM6Y6",value=1.5757268466362409)
        # # data 2
        # data['blank'] = rcf.read_trans_data(1042)
        # data['trans'] = rcf.read_trans_data(1043)
        # # plot data 2
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='magenta',energy=True,value=1.5757268466362409)


        """Reflectance"""
        color_reflectance = 'magenta'
        # data
        data['blank'] = rcf.read_trans_data(1034)
        data['trans'] = rcf.read_trans_data(1037)
        # plot data
        pcg.plot_absorption(data, ax=ax, smooth=False,energy=True, color=color_reflectance,legend='1:2 PM6Y6')
        # data 2
        data['blank'] = rcf.read_trans_data(1035)
        data['trans'] = rcf.read_trans_data(1036)
        # plot data 2
        pcg.plot_absorption(data, ax=ax, smooth=False,energy=True, color=color_reflectance)

        # plt.show()
    PM6Y6_12()

    def Y6():
        # fig, ax = plt.subplots()
        data = {}

        # """Absorbance"""
        # # data
        # data['blank'] = rcf.read_trans_data(1095)
        # data['trans'] = rcf.read_trans_data(1096)
        # # plot data
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='red',energy=True,legend="Y6")
        # # data 2
        # data['blank'] = rcf.read_trans_data(1094)
        # data['trans'] = rcf.read_trans_data(1097)
        # # plot data 2
        # pcg.plot_absorption(data, ax=ax, smooth=False,color='red',energy=True)


        """Reflectance"""
        ax2 = ax#.twinx()
        color_reflectance = 'red'
        # data
        data['blank'] = rcf.read_trans_data(1088)
        data['trans'] = rcf.read_trans_data(1089)
        # plot data
        pcg.plot_absorption(data, ax=ax2, smooth=False,energy=True, color=color_reflectance,legend="Y6")
        # data 2
        data['blank'] = rcf.read_trans_data(1087)
        data['trans'] = rcf.read_trans_data(1090)
        # plot data 2
        pcg.plot_absorption(data, ax=ax2, smooth=False,energy=True, color=color_reflectance)

        plt.title('Reflection Spectra')
        ax2.set_ylabel('Reflection (OD)')
        plt.legend()
        plt.show()
    Y6()



def VB12():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1221)
    data['trans'] = rcf.read_trans_data(138)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # room temp data
    data['blank'] = rcf.read_trans_data(1221)
    data['trans'] = rcf.read_trans_data(1222)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')

    plt.show()
# VB12()

def PESI2F():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1414)
    data['trans'] = rcf.read_trans_data(1415)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=True)

    # room temp data
    # data['blank'] = rcf.read_trans_data(1221)
    # data['trans'] = rcf.read_trans_data(1222)

    # # plot data
    # pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')

    plt.show()
# PESI2F()



def FMBA():
    fig, ax = plt.subplots()
    data = {}

    # data
    data['blank'] = rcf.read_trans_data(1553)
    data['trans'] = rcf.read_trans_data(1554)

    # plot data
    pcg.plot_absorption(data, ax=ax, smooth=False,energy=False)

    # room temp data
    # data['blank'] = rcf.read_trans_data(1221)
    # data['trans'] = rcf.read_trans_data(1222)

    # # plot data
    # pcg.plot_absorption(data, ax=ax, smooth=False,energy=False,color='red')

    plt.show()
FMBA()














