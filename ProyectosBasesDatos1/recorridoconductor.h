#ifndef RECORRIDOCONDUCTOR_H
#define RECORRIDOCONDUCTOR_H

#include <QWidget>

namespace Ui {
class RecorridoConductor;
}

class RecorridoConductor : public QWidget
{
    Q_OBJECT
    
public:
    explicit RecorridoConductor(QWidget *parent = 0);
    ~RecorridoConductor();
    
private:
    Ui::RecorridoConductor *ui;
};

#endif // RECORRIDOCONDUCTOR_H
