#ifndef RECORRIDOS_H
#define RECORRIDOS_H

#include <QWidget>

namespace Ui {
class Recorridos;
}

class Recorridos : public QWidget
{
    Q_OBJECT
    
public:
    explicit Recorridos(QWidget *parent = 0);
    ~Recorridos();
    
private:
    Ui::Recorridos *ui;
};

#endif // RECORRIDOS_H
