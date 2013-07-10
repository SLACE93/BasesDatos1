#include "conductor.h"
#include "ui_conductor.h"

Conductor::Conductor(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Conductor)
{
    ui->setupUi(this);
}

Conductor::~Conductor()
{
    delete ui;
}
