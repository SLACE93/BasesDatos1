#include "recorridofecha.h"
#include "ui_recorridofecha.h"

RecorridoFecha::RecorridoFecha(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::RecorridoFecha)
{
    ui->setupUi(this);
}

RecorridoFecha::~RecorridoFecha()
{
    delete ui;
}
