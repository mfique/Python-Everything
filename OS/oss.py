import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
    QHBoxLayout, QInputDialog, QMessageBox, QLineEdit, QMenu, QListWidget, QDialog,
    QTextEdit, QFileDialog
)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt, QTimer, QSize, QPropertyAnimation, QRect, QTime


class Windows10UI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("F Windows")
        self.setGeometry(100, 100, 1200, 700)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Add the desktop area with a background
        self.desktop_area = self.create_desktop_area()

        # Taskbar area
        self.taskbar = self.create_taskbar()

        # Add widgets to the main layout
        main_layout.addWidget(self.desktop_area)
        main_layout.addWidget(self.taskbar)

        # Start with the welcome screen
        self.show_welcome_screen()

        # Update the time every second
        self.update_time()

    def create_desktop_area(self):
        # Create a container for the desktop area
        self.desktop_area = QWidget(self)
        self.desktop_area.setFixedSize(1330, 630)
        desktop_layout = QVBoxLayout(self.desktop_area)

        # Set a background image for the desktop area
        background_label = QLabel(self)
        pixmap = QPixmap('DJJ.png')  # Use a local path to an image
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)
        background_label.setFixedSize(1330, 630)

        # Set background to the desktop area
        desktop_layout.addWidget(background_label)

        # Set the layout
        self.desktop_area.setLayout(desktop_layout)

        # Enable right-click context menu
        self.desktop_area.setContextMenuPolicy(Qt.CustomContextMenu)
        self.desktop_area.customContextMenuRequested.connect(self.show_context_menu)

        return self.desktop_area

    def create_taskbar(self):
        # Create a horizontal layout for the taskbar
        taskbar_layout = QHBoxLayout()

        # Start button (simulating the Windows Start button)
        start_button = QPushButton("Start", self)
        start_button.clicked.connect(self.show_start_menu)
        taskbar_layout.addWidget(start_button)

        # Wi-Fi indicator
        wifi_label = QLabel("Wi-Fi: Connected", self)
        taskbar_layout.addWidget(wifi_label)

        # Time display
        self.time_label = QLabel(self)
        taskbar_layout.addWidget(self.time_label)

        # Shutdown button
        shutdown_button = QPushButton("Power", self)
        shutdown_button.clicked.connect(self.shutdown_computer)
        taskbar_layout.addWidget(shutdown_button)

        # Container widget for the taskbar
        taskbar_container = QWidget()
        taskbar_container.setLayout(taskbar_layout)
        taskbar_container.setStyleSheet("background-color: #2d2d2d; color: white; padding: 5px;")

        return taskbar_container

    def show_context_menu(self, pos):
        context_menu = QMenu(self)

        # Add actions for creating a folder and a file
        create_folder_action = context_menu.addAction("Create Folder")
        create_file_action = context_menu.addAction("Create File")
        create_browser_action = context_menu.addAction("Open Browser")
        open_cmd_action = context_menu.addAction("Open Command Prompt")
        open_notepad_action = context_menu.addAction("Open Notepad")  # Add Notepad action

        # Connect actions to their respective functions
        create_folder_action.triggered.connect(self.create_folder)
        create_file_action.triggered.connect(self.create_file)
        create_browser_action.triggered.connect(self.open_browser)
        open_cmd_action.triggered.connect(self.open_command_prompt)
        open_notepad_action.triggered.connect(self.open_notepad)  # Connect to open_notepad

        # Show the context menu at the cursor position
        context_menu.exec_(self.desktop_area.mapToGlobal(pos))

    def create_folder(self):
        # Prompt user to enter folder name
        folder_name, ok = QInputDialog.getText(self, 'Create Folder', 'Enter folder name:')

        if ok and folder_name:
            folder_btn = QPushButton(folder_name, self)
            folder_btn.setIcon(QIcon('book_icon.png'))  # Use a book-like icon
            folder_btn.setIconSize(QSize(40, 40))
            folder_btn.setFixedSize(80, 120)
            folder_btn.setStyleSheet("text-align: top; padding-top: 5px; background-color: #D8BFD8; border-radius: 5px; border: 1px solid #8B008B;")
            folder_btn.clicked.connect(lambda: self.open_folder(folder_name))

            # Add the folder to the desktop area
            self.desktop_area.layout().addWidget(folder_btn)

    def create_file(self):
        # Prompt user to enter file name
        file_name, ok = QInputDialog.getText(self, 'Create File', 'Enter file name:')

        if ok and file_name:
            file_btn = QPushButton(file_name, self)
            file_btn.setIcon(QIcon('file_icon.png'))  # Use a file-like icon
            file_btn.setIconSize(QSize(40, 40))
            file_btn.setFixedSize(80, 120)
            file_btn.setStyleSheet("text-align: top; padding-top: 5px; background-color: #ADD8E6; border-radius: 5px; border: 1px solid #4682B4;")
            file_btn.clicked.connect(lambda: self.open_file(file_name))

            # Add the file to the desktop area
            self.desktop_area.layout().addWidget(file_btn)

    def open_folder(self, folder_name):
        print(f"Opening folder: {folder_name}")

    def open_file(self, file_name):
        print(f"Opening file: {file_name}")

    def open_browser(self):
        self.browser_window = BrowserWindow(self)
        self.browser_window.setWindowModality(Qt.ApplicationModal)
        self.browser_window.show()

    def open_command_prompt(self):
        self.cmd_window = CommandPromptWindow(self)
        self.cmd_window.setWindowModality(Qt.ApplicationModal)
        self.cmd_window.show()

    def open_notepad(self):
        try:
            subprocess.Popen("notepad.exe")  # Windows command to open Notepad
        except Exception as e:
            self.show_message("Error", f"Failed to open Notepad: {e}")
        
    def open_calculator(self):
        try:
            subprocess.Popen("calc.exe")  # Windows command to open Calculator
        except Exception as e:
            self.show_message("Error", f"Failed to open Calculator: {e}")

    def show_start_menu(self):
        start_menu_dialog = QDialog(self)
        start_menu_dialog.setWindowTitle("Start Menu")
        start_menu_dialog.setFixedSize(300, 400)

        layout = QVBoxLayout(start_menu_dialog)

        app_list = QListWidget(start_menu_dialog)
        app_list.addItems(["Calculator", "Notepad", "Add Folder", "Create File.txt", "Microsoft Office", "Word.Doc"])
        app_list.itemDoubleClicked.connect(self.launch_application)
        layout.addWidget(app_list)

        close_button = QPushButton("Close", start_menu_dialog)
        close_button.clicked.connect(start_menu_dialog.close)
        layout.addWidget(close_button)

        start_menu_dialog.exec_()

    def launch_application(self, item):
        app_name = item.text()
        if app_name == "Calculator":
            self.open_calculator()
        elif app_name == "Notepad":
            self.open_notepad()
        elif app_name == "Microsoft Office":
            self.open_microsoft_office()
        elif app_name == "Word.Doc":
            self.open_word_document()
        elif app_name == "Add Folder":
            self.create_folder()
        elif app_name == "Create File.txt":
            self.create_file()
        else:
            self.show_message("Application Not Found", f"Cannot launch: {app_name}")

    def open_microsoft_office(self):
        # Simulate opening Microsoft Office
        self.show_message("Microsoft Office", "Launching Microsoft Office is not implemented yet. You can open Office documents manually.")

    def open_word_document(self):
        # Simulate opening a Word document
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Word Document", "", "Word Documents (*.docx *.doc);;All Files (*)")
        if file_name:
            # Open the Word document using a default application (you may need to install additional packages for full integration)
            try:
                subprocess.Popen(["start", file_name], shell=True)  # Windows command to open the file with the default program
            except Exception as e:
                self.show_message("Error", f"Failed to open Word document: {e}")

    def shutdown_computer(self):
        print("Shutting down...")
        self.close()

    def show_welcome_screen(self):
        welcome_label = QLabel("F Windows available for you!", self)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(QFont('Arial', 20))
        self.desktop_area.layout().addWidget(welcome_label)

    def update_time(self):
        current_time = QTime.currentTime().toString()
        self.time_label.setText(current_time)
        QTimer.singleShot(1000, self.update_time)

    def show_message(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Windows10UI()
    window.show()
    sys.exit(app.exec_())