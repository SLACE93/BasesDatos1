#include "recorridohoras.h"
#include "ui_recorridohoras.h"

RecorridoHoras::RecorridoHoras(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::RecorridoHoras)
{
    ui->setupUi(this);
}

RecorridoHoras::~RecorridoHoras()
{
    delete ui;
}
