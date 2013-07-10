#ifndef CONDUCTOR_H
#define CONDUCTOR_H

#include <QWidget>

namespace Ui {
class Conductor;
}

class Conductor : public QWidget
{
    Q_OBJECT
    
public:
    explicit Conductor(QWidget *parent = 0);
    ~Conductor();
    
private:
    Ui::Conductor *ui;
};

#endif // CONDUCTOR_H
