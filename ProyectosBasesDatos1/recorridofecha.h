#ifndef RECORRIDOFECHA_H
#define RECORRIDOFECHA_H

#include <QWidget>

namespace Ui {
class RecorridoFecha;
}

class RecorridoFecha : public QWidget
{
    Q_OBJECT
    
public:
    explicit RecorridoFecha(QWidget *parent = 0);
    ~RecorridoFecha();
    
private:
    Ui::RecorridoFecha *ui;
};

#endif // RECORRIDOFECHA_H
