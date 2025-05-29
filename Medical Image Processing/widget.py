import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox, QSlider
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
from ui_form import Ui_Widget  # Qt Designer ile oluşturulan arayüz dosyasının Python sınıfı

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.original_label.setAlignment(Qt.AlignCenter)
        self.ui.processed_label.setAlignment(Qt.AlignCenter)

        self.ui.load_button.clicked.connect(self.load_image)
        self.ui.brightness_slider.valueChanged.connect(self.update_processing)
        self.ui.contrast_slider.valueChanged.connect(self.update_processing)
        self.ui.edge_button.clicked.connect(self.apply_edge_detection)
        self.ui.sharpen_button.clicked.connect(self.apply_sharpening)
        self.ui.hist_button.clicked.connect(self.show_histogram)
        self.ui.auto_enhance_button.clicked.connect(self.apply_clahe)
        self.ui.highlight_button.clicked.connect(self.highlight_abnormalities)
        self.ui.undo_button.clicked.connect(self.undo)
        self.ui.redo_button.clicked.connect(self.redo)
        self.ui.reset_button.clicked.connect(self.reset_image)

        self.brightness = 0
        self.contrast = 1.0
        self.history = []
        self.history_index = -1

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Görsel Seç", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            if pixmap.isNull():
                print("Görsel okunamadı!")
                return

            self.ui.original_label.setPixmap(pixmap.scaled(self.ui.original_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

            with open(file_path, "rb") as f:
                data = f.read()
                img_array = np.frombuffer(data, np.uint8)
                cv_image = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

            if cv_image is None:
                print("OpenCV ile görsel işlenemedi.")
                return

            self.image = cv_image
            self.processed_image = cv_image.copy()

            self.processed_image = cv2.medianBlur(self.processed_image, 5)
            self.processed_image = cv2.GaussianBlur(self.processed_image, (5, 5), 0)
            self.save_to_history()
            self.update_image_views()

    def update_processing(self):
        if hasattr(self, "image"):
            self.brightness = self.ui.brightness_slider.value()
            self.contrast = self.ui.contrast_slider.value() / 100.0
            self.processed_image = cv2.convertScaleAbs(self.image, alpha=self.contrast, beta=self.brightness)
            self.save_to_history()
            self.update_image_views()

    def apply_edge_detection(self):
        if hasattr(self, "processed_image"):
            thresh1 = self.ui.canny_thresh1_spin.value()
            thresh2 = self.ui.canny_thresh2_spin.value()
            edges = cv2.Canny(self.processed_image, threshold1=thresh1, threshold2=thresh2)
            self.processed_image = edges
            self.save_to_history()
            self.update_image_views()

    def convert_cv_to_pixmap(self, cv_image):
        h, w = cv_image.shape
        bytes_per_line = w
        q_img = QImage(cv_image.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        return QPixmap.fromImage(q_img)

    def update_image_views(self):
        if hasattr(self, "image") and hasattr(self, "processed_image"):
            orig_pixmap = self.convert_cv_to_pixmap(self.image)
            proc_pixmap = self.convert_cv_to_pixmap(self.processed_image)

            self.ui.original_label.setPixmap(orig_pixmap.scaled(self.ui.original_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.ui.processed_label.setPixmap(proc_pixmap.scaled(self.ui.processed_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def apply_sharpening(self):
        if hasattr(self, "processed_image"):
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            self.processed_image = cv2.filter2D(self.processed_image, -1, kernel)
            self.save_to_history()
            self.update_image_views()

    def show_histogram(self):
        if hasattr(self, "image"):
            self.bin_size=10
            hist = cv2.calcHist([self.image], [0], None, [self.bin_size], [0, 256])
            dark_pixels = hist[:10].sum()
            bright_pixels = hist[245:].sum()
            threshold = 1000

            if dark_pixels > threshold or bright_pixels > threshold:
                QMessageBox.warning(self, "Uyarı", "Histogramda anormal alanlar tespit edildi.")

            plt.figure("Histogram")
            plt.title("Gri Seviye Histogram")
            plt.xlabel("Piksel Değeri")
            plt.ylabel("Frekans")
            plt.bar(range(self.bin_size), hist.flatten(), color='gray', alpha=0.7)
            plt.xlim([0, self.bin_size])
            plt.grid(True)
            plt.legend()
            plt.show()

    def apply_clahe(self):
        if hasattr(self, "processed_image"):
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            self.processed_image = clahe.apply(self.processed_image)
            self.save_to_history()
            self.update_image_views()

    def highlight_abnormalities(self):
        if hasattr(self, "processed_image"):
            thresh1 = self.ui.canny_thresh1_spin.value()
            thresh2 = self.ui.canny_thresh2_spin.value()
            area_threshold = self.ui.area_threshold_spin.value()

            edges = cv2.Canny(self.processed_image, threshold1=thresh1, threshold2=thresh2)
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            highlighted = cv2.cvtColor(self.processed_image, cv2.COLOR_GRAY2BGR)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > area_threshold:
                    (x, y), radius = cv2.minEnclosingCircle(contour)
                    center = (int(x), int(y))
                    radius = int(radius)
                    cv2.circle(highlighted, center, radius, (0, 0, 255), 2)
            self.processed_image = cv2.cvtColor(highlighted, cv2.COLOR_BGR2GRAY)
            self.save_to_history()
            self.update_image_views()

    def save_to_history(self):
        if hasattr(self, "processed_image"):
            if len(self.history) >= 20:
                self.history.pop(0)
                self.history_index -= 1
            self.history = self.history[:self.history_index + 1]
            self.history.append(self.processed_image.copy())
            self.history_index += 1

    def undo(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.processed_image = self.history[self.history_index].copy()
            self.update_image_views()

    def redo(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.processed_image = self.history[self.history_index].copy()
            self.update_image_views()

    def reset_image(self):
        if hasattr(self, "image"):
            self.processed_image = self.image.copy()
            self.save_to_history()
            self.update_image_views()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
