import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QFileDialog

class TransferDataGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Target IP
        target_ip_layout = QHBoxLayout()
        target_ip_label = QLabel("Target IP:")
        self.target_ip_input = QLineEdit()
        target_ip_layout.addWidget(target_ip_label)
        target_ip_layout.addWidget(self.target_ip_input)

        # Target Username
        target_username_layout = QHBoxLayout()
        target_username_label = QLabel("Target Username:")
        self.target_username_input = QLineEdit()
        target_username_layout.addWidget(target_username_label)
        target_username_layout.addWidget(self.target_username_input)

        # Target Password
        target_password_layout = QHBoxLayout()
        target_password_label = QLabel("Target Password:")
        self.target_password_input = QLineEdit()
        self.target_password_input.setEchoMode(QLineEdit.Password)  # Hide password input
        target_password_layout.addWidget(target_password_label)
        target_password_layout.addWidget(self.target_password_input)

        # Private Key Directory
        private_key_layout = QHBoxLayout()
        private_key_label = QLabel("Private Key Directory:")
        self.private_key_input = QLineEdit()
        private_key_browse_button = QPushButton("Browse")
        private_key_browse_button.clicked.connect(self.browse_private_key)
        private_key_layout.addWidget(private_key_label)
        private_key_layout.addWidget(self.private_key_input)
        private_key_layout.addWidget(private_key_browse_button)

        # Ignore Host Key checkbox
        self.ignore_host_key_checkbox = QCheckBox("Ignore Host Key")

        # Source Directory
        source_directory_layout = QHBoxLayout()
        source_directory_label = QLabel("Source Directory:")
        self.source_directory_input = QLineEdit()
        source_browse_button = QPushButton("Browse")
        source_browse_button.clicked.connect(self.browse_source_directory)
        source_directory_layout.addWidget(source_directory_label)
        source_directory_layout.addWidget(self.source_directory_input)
        source_directory_layout.addWidget(source_browse_button)

        # Target Directory
        target_directory_layout = QHBoxLayout()
        target_directory_label = QLabel("Target Directory:")
        self.target_directory_input = QLineEdit()
        target_directory_layout.addWidget(target_directory_label)
        target_directory_layout.addWidget(self.target_directory_input)

        # Buttons layout
        buttons_layout = QHBoxLayout()
        save_button = QPushButton("Save Config")
        load_button = QPushButton("Load Config")
        clear_button = QPushButton("Clear Config")
        upload_button = QPushButton("Upload")

        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(load_button)
        buttons_layout.addWidget(clear_button)
        buttons_layout.addWidget(upload_button)

        # Adding widgets to the main layout
        main_layout.addLayout(target_ip_layout)
        main_layout.addLayout(target_username_layout)
        main_layout.addLayout(target_password_layout)
        main_layout.addLayout(private_key_layout)
        main_layout.addWidget(self.ignore_host_key_checkbox)
        main_layout.addLayout(source_directory_layout)
        main_layout.addLayout(target_directory_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

        self.setWindowTitle("Transfer Data")
        self.setGeometry(300, 300, 600, 400)

    def browse_private_key(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Private Key File")
        if file_name:
            self.private_key_input.setText(file_name)

    def browse_source_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        if directory:
            self.source_directory_input.setText(directory)

# Main execution
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TransferDataGUI()
    ex.show()
    sys.exit(app.exec_())
