#!/usr/bin/env python3
"""
The Villain Arc Opt-In Dialog
Brings the pain only if you consent to it.
"""

import sys
import os
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, 
                             QPushButton, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QPalette, QColor

class VillainOptInDialog(QDialog):
    """The first point of contact - sets the tone for the pain to come."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Villain Arc Productivity System")
        self.setFixedSize(500, 300)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Dialog)
        
        # Make it look menacing
        self.set_dark_theme()
        self.setup_ui()
        
    def set_dark_theme(self):
        """Because villains prefer dark mode."""
        self.setStyleSheet("""
            QDialog {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QPushButton {
                background-color: #333333;
                color: white;
                border: 2px solid #555555;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #444444;
                border: 2px solid #666666;
            }
            QPushButton#accept_btn {
                background-color: #d32f2f;
                border: 2px solid #f44336;
            }
            QPushButton#accept_btn:hover {
                background-color: #f44336;
            }
        """)
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Title - make it intimidating
        title = QLabel("THE VILLAIN ARC AWAITS")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(title)
        
        # Description
        desc = QLabel(
            "This system will interrupt your flow state every 25 minutes with math challenges.\n\n"
            "Failures result in exponential lock times and brutal roasts.\n\n"
            "Success requires surrendering your ego and embracing the pain.\n\n"
            "Do you wish to proceed?"
        )
        desc.setAlignment(Qt.AlignCenter)
        desc.setWordWrap(True)
        layout.addWidget(desc)
        
        # Button layout
        button_layout = QHBoxLayout()
        
        # The "Be a Good Boy" option (but framed differently)
        reject_btn = QPushButton("❌ Live in Comfort")
        reject_btn.clicked.connect(self.reject_villainy)
        button_layout.addWidget(reject_btn)
        
        # The villainous acceptance
        accept_btn = QPushButton("🔥 Embrace the Villain Arc")
        accept_btn.setObjectName("accept_btn")
        accept_btn.clicked.connect(self.accept_villainy)
        button_layout.addWidget(accept_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def accept_villainy(self):
        """User has chosen pain. Begin the initialization."""
        reply = QMessageBox.question(
            self, 
            "Final Warning", 
            "Last chance to turn back.\n\n"
            "Once activated, the system will:\n"
            "• Interrupt your flow state every 25 minutes\n"
            "• Lock your screen for math challenges\n"
            "• Roast you mercilessly for failures\n"
            "• Respect no excuses\n\n"
            "Proceed?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.accept()  # Dialog returns Accepted
        else:
            # They got scared
            QMessageBox.information(
                self, 
                "Wisdom Prevails", 
                "The villain arc retreats... for now."
            )
            self.reject()
    
    def reject_villainy(self):
        """User chooses comfort over growth."""
        QMessageBox.information(
            self,
            "Comfort Zone Maintained",
            "The system will not activate.\n\n"
            "You may restart the villain arc anytime by running:\n"
            "`python3 system/optin_dialog.py`"
        )
        self.reject()

def main():
    app = QApplication(sys.argv)
    
    # Check if we're in a desktop environment (not SSH/headless)
    if not os.getenv('DISPLAY'):
        print("No display detected - cannot show opt-in dialog")
        return 1
    
    dialog = VillainOptInDialog()
    result = dialog.exec_()
    
    if result == QDialog.Accepted:
        print("USER ACCEPTED THE VILLAIN ARC - INITIALIZING SYSTEM...")
        # Here we'll call the Ollama manager and main daemon
        return 0
    else:
        print("User declined the villain arc. System remains dormant.")
        return 1

if __name__ == "__main__":
    sys.exit(main())