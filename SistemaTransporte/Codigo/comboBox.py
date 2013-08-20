'''
Created on Aug 10, 2013

@author: slace93
'''

from PyQt4.QtGui import QComboBox, QCompleter, QSortFilterProxyModel
from PyQt4.QtCore import Qt

class ExtendedComboBox( QComboBox ):
    def __init__( self,  parent = None):
        super( ExtendedComboBox, self ).__init__( parent )
        self.setFocusPolicy( Qt.StrongFocus )
        self.setEditable( True )
        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel( self )
        self.pFilterModel.setFilterCaseSensitivity( Qt.CaseInsensitive )
        self.pFilterModel.setSourceModel(self.model())
        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all completions
        self.completer.setCompletionMode( QCompleter.UnfilteredPopupCompletion )
        self.completer.setPopup( self.view() )
        self.setCompleter( self.completer )
        self.lineEdit().textEdited[unicode].connect( self.pFilterModel.setFilterFixedString )
        self.completer.activated.connect(self.on_completer_activated)

    def setModel( self, model ):
        super(ExtendedComboBox, self).setModel( model )
        self.pFilterModel.setSourceModel( model )
        self.completer.setModel(self.pFilterModel)

    def setModelColumn( self, column ):
        self.completer.setCompletionColumn( column )
        self.pFilterModel.setFilterKeyColumn( column )
        super(ExtendedComboBox, self).setModelColumn( column )

    def view( self ):
        return self.completer.popup()

    def index( self ):
        return self.currentIndex()

    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
