#ifndef UNIDADES_H
#define UNIDADES_H

#include <QWidget>

namespace Ui {
class Unidades;
}

class Unidades : public QWidget
{
    Q_OBJECT
    
public:
    explicit Unidades(QWidget *parent = 0);
    ~Unidades();
    
private:
    Ui::Unidades *ui;
};

#endif // UNIDADES_H
