#ifndef RECORRIDOHORAS_H
#define RECORRIDOHORAS_H

#include <QWidget>

namespace Ui {
class RecorridoHoras;
}

class RecorridoHoras : public QWidget
{
    Q_OBJECT
    
public:
    explicit RecorridoHoras(QWidget *parent = 0);
    ~RecorridoHoras();
    
private:
    Ui::RecorridoHoras *ui;
};

#endif // RECORRIDOHORAS_H
