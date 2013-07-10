#ifndef RECORRIDOUNIDAD_H
#define RECORRIDOUNIDAD_H

#include <QWidget>

namespace Ui {
class RecorridoUnidad;
}

class RecorridoUnidad : public QWidget
{
    Q_OBJECT
    
public:
    explicit RecorridoUnidad(QWidget *parent = 0);
    ~RecorridoUnidad();
    
private:
    Ui::RecorridoUnidad *ui;
};

#endif // RECORRIDOUNIDAD_H
