#-------------------------------------------------
#
# Project created by QtCreator 2013-07-09T16:46:17
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = ProyectosBasesDatos1
TEMPLATE = app


SOURCES += main.cpp\
        principal.cpp \
    consultas.cpp \
    conductor.cpp \
    unidades.cpp \
    recorridos.cpp \
    recorridofecha.cpp \
    recorridoconductor.cpp \
    recorridounidad.cpp \
    recorridohoras.cpp

HEADERS  += principal.h \
    consultas.h \
    conductor.h \
    unidades.h \
    recorridos.h \
    recorridofecha.h \
    recorridoconductor.h \
    recorridounidad.h \
    recorridohoras.h

FORMS    += principal.ui \
    consultas.ui \
    conductor.ui \
    unidades.ui \
    recorridos.ui \
    recorridofecha.ui \
    recorridoconductor.ui \
    recorridounidad.ui \
    recorridohoras.ui

RESOURCES += \
    imagenes.qrc
