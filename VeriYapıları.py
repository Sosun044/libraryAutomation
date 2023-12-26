import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog, QDialog, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
#üYE SINIFINI olusturdum ağaçlar yapısıyla
#UserNode kısmı uyeleri ne tür prametreler diye kaydedeciğimi bilerek düşünebilirsiniz
class UserNode:
    def __init__(self,kullanici_ad, e_posta = None):
        self.kullanici_ad = kullanici_ad
        self.e_posta = e_posta
        self.left = None
        self.right = None
#UserTree agaç yapısında var olmasını gösteren kısım root bas kısmı ve sonradan yukardaki left ve right yazıldıgı gibi sağ ve sola dallanma
class UserTree:
    def __init__(self):
        self.root = None
        self.add_user("Admin","yalovauni77@yalova.edu.tr")
        self.add_user("Muhammed", "210101068@ogrenci.yalova.edu.tr")
        self.add_user("Yaşar", "210101000@ogrenci.yalova.edu.tr")
        self.add_user("Mehmet18", "Mehmetyazıcıoglu@gmail.com")
#kullanıcı eklenmesi icin
    def add_user(self,kullanici_ad, e_posta= None):
        self.root = self._add_user(self.root, kullanici_ad, e_posta)
#kullanıcı eklenmesi sırasında yapılacak kontroller agaç kısmında
    def _add_user(self, root, kullanici_ad, e_posta):
        if root is None:
            return UserNode(kullanici_ad, e_posta)
        if kullanici_ad < root.kullanici_ad:
            root.left = self._add_user(root.left, kullanici_ad, e_posta)
        elif kullanici_ad > root.kullanici_ad:
            root.right = self._add_user(root.right, kullanici_ad, e_posta)
        return root
    def display_users(self, root):
        if root:
            self.display_users(root.left)
            print(root.kullanici_ad, root.e_posta)
            self.display_users(root.right)
    #silmek icin yazılan fonksiyon
    def remove_user(self, kullanici_ad):
        self.root = self._remove_user(self.root, kullanici_ad)

    def _remove_user(self, root, kullanici_ad):
        if root is None:
            return root

        if kullanici_ad < root.kullanici_ad:
            root.left = self._remove_user(root.left, kullanici_ad)
        elif kullanici_ad > root.kullanici_ad:
            root.right = self._remove_user(root.right, kullanici_ad)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.kullanici_ad = self._min_value_node(root.right).kullanici_ad
            root.right = self._remove_user(root.right, root.kullanici_ad)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    #bir sıralı hale getirilir burda dizi gibi düşünebilirsiniz
    def get_user_list(self):
        user_list = []
        self._get_user_list(self.root, user_list)
        return user_list

    def _get_user_list(self, root, user_list):
        if root:
            self._get_user_list(root.left, user_list)
            user_list.append([root.kullanici_ad, root.e_posta])
            self._get_user_list(root.right, user_list)

#kitaplar icin olusturulan sınıf
class BookNode:
    def __init__(self, data, author=None, publication_date=None, genre=None):
        self.data = data
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.left = None
        self.right = None
class BookTree:
    def __init__(self):
        self.root = None
        # Hazırda bulunan kitaplar
        self.add_book("Ölü Ozanlar Derneği", "Robin Williams", "1989-10-01", "Dram")
        self.add_book("Tutunamayanlar", "Oğuz Atay", "2000-02-01", "Psikoloji")
        self.add_book("Sefiller", "Victor Hugo", "1862-06-08", "Roman")
        self.add_book("Kinyas ve Kayra", "Hakan Günday", "2011-04-01", "Roman")
    def add_book(self, data, author=None, publication_date=None, genre=None):
        self.root = self._add_book(self.root, data, author, publication_date, genre)

    def _add_book(self, root, data, author, publication_date, genre):
        if root is None:
            return BookNode(data, author, publication_date, genre)
        if data < root.data:
            root.left = self._add_book(root.left, data, author, publication_date, genre)
        elif data > root.data:
            root.right = self._add_book(root.right, data, author, publication_date, genre)
        return root


    def display_books(self, root):
        if root:
            self.display_books(root.left)
            print(root.data, root.author, root.publication_date, root.genre)
            self.display_books(root.right)
#silme fonkisyonu
    def remove_book(self, data):
        self.root = self._remove_book(self.root, data)

    def _remove_book(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self._remove_book(root.left, data)
        elif data > root.data:
            root.right = self._remove_book(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.data = self._min_value_node(root.right).data
            root.right = self._remove_book(root.right, root.data)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_book_list(self):
        book_list = []
        self._get_book_list(self.root, book_list)
        return book_list

    def _get_book_list(self, root, book_list):
        if root:
            self._get_book_list(root.left, book_list)
            book_list.append([root.data, root.author, root.publication_date, root.genre])
            self._get_book_list(root.right, book_list)
            #arayüz kısmı
class Interface(QWidget):
    def __init__(self, book_tree, user_tree):
        super().__init__()
        self.user_tree = user_tree
        self.book_tree = book_tree
        self.init_ui()

    def init_ui(self):
        # arka plan resmi
        arka_plan_resmi = QLabel(self)
        arka_plan_resmi.setPixmap(QPixmap('kutuphane.png'))
        arka_plan_resmi.setScaledContents(True)
        arka_plan_resmi.setFixedSize(800, 600)
#kitap ve uyeler table_widget kısmında gözüküyor
        self.table_widget = QTableWidget(7,7,self)
        self.table_widget.setGeometry(0, 0, 800, 600)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Kitap İsmi", "Yazar", "Yayın Tarihi", "Tür"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table_widget1 = QTableWidget(7, 7, self)
        self.table_widget1.setGeometry(0, 0, 800, 600)
        self.table_widget1.setColumnCount(2)
        self.table_widget1.setHorizontalHeaderLabels(["Kullanıcı İsmi", "e_posta"])
        self.table_widget1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

#butonlarımız
        self.uye_ekle = QPushButton("üye Ekle",self)
        self.uye_ekle.setStyleSheet("background-color: #FFFF00; color: red; font-size: 18px;")
        self.uye_ekle.clicked.connect(self.show_add_user)


        self.uye_listele = QPushButton("Üye Listele",self)
        self.uye_listele.setStyleSheet("background-color: #FF0000; color: yellow; font-size: 18px;")
        self.uye_listele.clicked.connect(self.list_users)

        self.uye_sil = QPushButton("Üye Sil", self)
        self.uye_sil.setStyleSheet("background-color: #FFFF00; color: red; font-size: 18px;")
        self.uye_sil.clicked.connect(self.show_remove_user)



        self.kitap_ekle = QPushButton("Kitap Ekle", self)
        self.kitap_ekle.setStyleSheet("background-color: #FFFF00; color: red; font-size: 18px;")
        self.kitap_ekle.clicked.connect(self.show_add_book)

        self.kitap_sil = QPushButton("Kitap Sil", self)
        self.kitap_sil.setStyleSheet("background-color: #FFFF00; color: red; font-size: 18px;")
        self.kitap_sil.clicked.connect(self.show_remove_book)

        self.kitap_listele = QPushButton("Kitap Listele", self)
        self.kitap_listele.setStyleSheet("background-color: #FF0000; color: yellow; font-size: 18px;")
        self.kitap_listele.clicked.connect(self.list_books)
#assagı yukarı , saga sola yerleştirme
        h_box = QHBoxLayout()
        h_box.addWidget(self.kitap_ekle)
        h_box.addWidget(self.kitap_listele)
        h_box.addWidget(self.kitap_sil)

        h1_box = QHBoxLayout()
        h1_box.addWidget(self.uye_ekle)
        h1_box.addWidget(self.uye_listele)
        h1_box.addWidget(self.uye_sil)

        v_box = QVBoxLayout()
        v_box.addWidget(self.table_widget)
        v_box.addWidget(self.table_widget1)
        v_box.addStretch()
        v_box.addLayout(h1_box)
        v_box.addLayout(h_box)

        # Arka plan rengini ayarlayalım
        self.setStyleSheet("background-color: white;")

        # Sayfa boyutunu ayarlayalım
        self.resize(800, 600)
        self.setWindowTitle("Kütüphane Otomasyonu")
        self.setLayout(v_box)
#kitap ekle butonuna tıklanınca show_add_user kısmına gidilir aynısı diger butonlardada kullanılır ama farklı fonksiyonlar
#listelemek icin list_user silmek icin show_remove_user vs.
    def show_add_user(self):
        self.add1 = AddUser(self.user_tree,parent = None)
        self.add1.show()

    def list_users(self):
        user_list = self.user_tree.get_user_list()
        self.table_widget1.setRowCount(len(user_list))
        for row_position, user in enumerate(user_list):
            for i, item in enumerate(user):
                self.table_widget1.setItem(row_position, i, QTableWidgetItem(str(item)))

    def show_remove_user(self):
        selected_items = self.table_widget1.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Üye Seçilmemiş", "Lütfen silmek istediğiniz Üyeyi seçin.")
            return

        selected_row = selected_items[0].row()
        kullanici_ad = self.table_widget1.item(selected_row, 0).text()

        reply = QMessageBox.question(
            self, "Üye Sil",
            f"{kullanici_ad} kullanici adına sahip kişiyi silmek istediğinize emin misiniz?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.user_tree.remove_user(kullanici_ad)
            self.list_users()

    def show_add_book(self):
        self.add = AddBookDialog(self.book_tree,parent = None)
        self.add.show()
    def list_books(self):
        self.table_widget.setRowCount(0)
        book_list = self.book_tree.get_book_list()
        for book in book_list:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for i, item in enumerate(book):
                self.table_widget.setItem(row_position, i, QTableWidgetItem(str(item)))


    def show_remove_book(self):
        selected_items = self.table_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Kitap Seçilmemiş", "Lütfen silmek istediğiniz kitabı seçin.")
            return

        selected_row = selected_items[0].row()
        kitap_ismi = self.table_widget.item(selected_row, 0).text()

        reply = QMessageBox.question(
            self, "Kitap Sil",
            f"{kitap_ismi} isimli kitabı silmek istediğinize emin misiniz?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.book_tree.remove_book(kitap_ismi)
            self.list_books()
#yeni bir pencere acılacak kısımlardan biri kitap ekle kısmı oldugu icin burda AddBookDialog sınıfını açtım
class AddBookDialog(QDialog):
    def __init__(self, book_tree, parent=None):
        super().__init__(parent)
        self.book_tree = book_tree
        self.init_ui()

    def init_ui(self):

        # arka plan resmi
        arka_plan_resmi = QLabel(self)
        arka_plan_resmi.setPixmap(QPixmap('kitapekle.png'))
        arka_plan_resmi.setScaledContents(True)
        arka_plan_resmi.setFixedSize(450, 300)

        self.kitap_ismi_label = QLabel("Kitap İsmi:")
        self.kitap_ismi_label.setStyleSheet("color: black; font-size: 20px;")
        self.yazar_label = QLabel("Yazar:")
        self.yazar_label.setStyleSheet("color: black; font-size: 20px;")
        self.yayin_tarihi_label = QLabel("Yayın Tarihi:")
        self.yayin_tarihi_label.setStyleSheet("color: black; font-size: 20px;")
        self.tur_label = QLabel("Tür:")
        self.tur_label.setStyleSheet("color: black; font-size: 20px;")


        self.kitap_ismi_line = QLineEdit()
        self.yazar_line = QLineEdit()
        self.yayin_tarihi_line = QLineEdit()
        self.tur_line = QLineEdit()

        self.kitap_ekle_button = QPushButton("Kitap Ekle")
        self.kitap_ekle_button.setStyleSheet("background-color: #FFFF00; color: red; font-size: 18px;")
        self.kitap_ekle_button.clicked.connect(self.add_book)
        self.cikis_buton = QPushButton("Çıkış")
        self.cikis_buton.clicked.connect(self.cikis)
        self.cikis_buton.setStyleSheet("background-color: #FF0000; color: yellow; font-size: 18px;")
        v1_box = QVBoxLayout()
        v1_box.addWidget(self.kitap_ismi_label)
        v1_box.addWidget(self.yazar_label)
        v1_box.addWidget(self.yayin_tarihi_label)
        v1_box.addWidget(self.tur_label)
        v1_box.addWidget(self.kitap_ekle_button)
        v1_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.kitap_ismi_line)
        v_box.addWidget(self.yazar_line)
        v_box.addWidget(self.yayin_tarihi_line)
        v_box.addWidget(self.tur_line)
        v_box.addWidget(self.cikis_buton)
        v_box.addStretch()


        h1_box = QHBoxLayout()
        h1_box.addLayout(v1_box)
        h1_box.addLayout(v_box)
        h1_box.addStretch()



        self.setLayout(h1_box)
        self.setWindowTitle("Kitap Ekle")
        self.resize(450,300)
        self.show()

    def add_book(self):
        kitap_ismi = self.kitap_ismi_line.text()
        yazar = self.yazar_line.text()
        yayin_tarihi = self.yayin_tarihi_line.text()
        tur = self.tur_line.text()

        if kitap_ismi:
            self.book_tree.add_book(kitap_ismi, yazar, yayin_tarihi, tur)
            # QDialog penceresini kapatır
            self.accept()
        else:
            QMessageBox.warning(self, "Hata", "Lütfen kitap ismini girin.")

    def cikis(self):
        self.close()
#tekrar burdada yeni bir sınıf yeni bir pencere anlamı gibi
class AddUser(QDialog):
    def __init__(self, user_tree, parent=None):
        super().__init__(parent)
        self.user_tree = user_tree
        self.init_ui()

    def init_ui(self):

        # arka plan resmi
        arka_plan_resmi = QLabel(self)
        arka_plan_resmi.setPixmap(QPixmap('yeni-uyelik.png'))
        arka_plan_resmi.setScaledContents(True)
        arka_plan_resmi.setFixedSize(450, 300)

        self.kullanici_ad_label = QLabel("Kullanici Ad")
        self.kullanici_ad_label.setStyleSheet("color: black; font-size: 20px;")

        self.e_posta_label = QLabel("e_posta")
        self.e_posta_label.setStyleSheet("color: black; font-size: 20px;")

        self.kullanici_ad_line = QLineEdit()
        self.e_posta_line = QLineEdit()

        self.uye_ekle_button = QPushButton("Uye Ekle")
        self.uye_ekle_button.setStyleSheet("background-color: #FFFF00; color: red; font-size: 18px;")
        self.uye_ekle_button.clicked.connect(self.add_user)
        self.cikis_buton = QPushButton("Çıkış")
        self.cikis_buton.clicked.connect(self.cikis)
        self.cikis_buton.setStyleSheet("background-color: #FF0000; color: yellow; font-size: 18px;")

        v1_box = QVBoxLayout()
        v1_box.addWidget(self.kullanici_ad_label)
        v1_box.addWidget(self.e_posta_label)
        v1_box.addStretch()
        v1_box.addWidget(self.uye_ekle_button)

        v_box = QVBoxLayout()
        v_box.addWidget(self.kullanici_ad_line)
        v_box.addWidget(self.e_posta_line)
        v_box.addStretch()
        v_box.addWidget(self.cikis_buton)

        h1_box = QHBoxLayout()
        h1_box.addLayout(v1_box)
        h1_box.addLayout(v_box)
        h1_box.addStretch()

        self.setLayout(h1_box)
        self.setWindowTitle("Üye Ekle")
        self.resize(450, 300)
        self.show()




    def add_user(self):
        kullanici_ad = self.kullanici_ad_line.text()
        e_posta = self.e_posta_line.text()


        if kullanici_ad:
            self.user_tree.add_user(kullanici_ad,e_posta)
            # QDialog penceresini kapatır
            self.accept()
        else:
            QMessageBox.warning(self, "Hata", "Lütfen Uye kullanici adını giriniz.")

    def cikis(self):
        self.close()

#burda ipin ucu gibi object orianted kısmında benzerlik kurarsak burda sınıflar ve gözükenler arası baglantı
#bide PyQt5 icin sart olan bazı yazılar assagıda app gibi
app = QApplication(sys.argv)
book_tree = BookTree()
user_tree = UserTree()
window = Interface(book_tree, user_tree)
window.show()
sys.exit(app.exec_())
