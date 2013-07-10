#include "consultas.h"
#include "ui_consultas.h"

Consultas::Consultas(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Consultas)
{
    ui->setupUi(this);
}

Consultas::~Consultas()
{
    delete ui;
}
