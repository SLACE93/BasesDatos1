#ifndef CONSULTAS_H
#define CONSULTAS_H

#include <QWidget>

namespace Ui {
class Consultas;
}

class Consultas : public QWidget
{
    Q_OBJECT
    
public:
    explicit Consultas(QWidget *parent = 0);
    ~Consultas();
    
private:
    Ui::Consultas *ui;
};

#endif // CONSULTAS_H
