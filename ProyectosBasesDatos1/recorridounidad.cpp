#include "recorridounidad.h"
#include "ui_recorridounidad.h"

RecorridoUnidad::RecorridoUnidad(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::RecorridoUnidad)
{
    ui->setupUi(this);
}

RecorridoUnidad::~RecorridoUnidad()
{
    delete ui;
}
