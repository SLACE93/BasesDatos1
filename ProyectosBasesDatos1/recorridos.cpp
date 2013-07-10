#include "recorridos.h"
#include "ui_recorridos.h"

Recorridos::Recorridos(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Recorridos)
{
    ui->setupUi(this);
}

Recorridos::~Recorridos()
{
    delete ui;
}
