#include "unidades.h"
#include "ui_unidades.h"

Unidades::Unidades(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Unidades)
{
    ui->setupUi(this);
}

Unidades::~Unidades()
{
    delete ui;
}
