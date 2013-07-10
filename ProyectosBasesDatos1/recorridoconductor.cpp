#include "recorridoconductor.h"
#include "ui_recorridoconductor.h"

RecorridoConductor::RecorridoConductor(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::RecorridoConductor)
{
    ui->setupUi(this);
}

RecorridoConductor::~RecorridoConductor()
{
    delete ui;
}
