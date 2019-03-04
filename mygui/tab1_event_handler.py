# This file takes care of all the event from tab1

def widgets_init_tab1(main_window=None):
    main_window.tab1_ui.pushButton.clicked.connect(lambda value=True,
                                                   main_window=main_window: button_clicked(value,
                                                                                           main_window))

def button_clicked(clicked, main_window):

    # this ui is in the tab1
    main_window.tab1_ui.textEdit.setText("button clicked")

    # this shows that we can communicate with the widgets of the main window
    main_window.ui.lineEdit.setText("tab1 button clicked")