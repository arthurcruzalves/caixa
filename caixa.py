import sys
# importar os componentes para a construção da janela
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap 
# construção da classe janela com o nome de caixa 
class Caixa(QWidget):
# Criação do método __int__ que inicia a janela e exibe ela em tela 
    def __init__(self):
        super().__init__()
        # vamos definir a posição e o tamanho da tela 
        self.setGeometry(0,30,1000,800)

        # vamos definir o título da nossa janela 
        self.setWindowTitle("Caixa da Loja")

        # Vamos criar as labels que representam as colunas esquerda e direita

        #Label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#DCDCDC}")

        #Label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#4F4F4F}")

        #---------- Criar o contéudo da coluna da esquerda --------------
        self.v_layout_esquerda =  QVBoxLayout()       

        #Vamos criar uma label para adicionar o logo da nossa loja
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("C:/Users/arthur.calves2/Documents/JanelaCaixa/.venv/EA_Sports_FC_24_logo.png"))
        # Ajudar a label e a imagem para ficar do tamanho ideal
        self.logo_label.setScaledContents(True)
        # adicionar a label com a imagem na tela 
        self.v_layout_esquerda.addWidget(self.logo_label)

        # Vamos criar as Labels e as LinesEdits que ficarão na coluna da esquerda, dentro do layout vertical da esquerda
        self.codigo_produto_label = QLabel("Codigo do Produto")
        self.codigo_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.codigo_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codigo_produto_edit)

        self.nome_produto_label = QLabel("Nome do Produto")
        self.nome_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.nome_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.nome_produto_label)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)

        self.descricao_produto_label = QLabel("Descrição do Produto")
        self.descricao_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.descricao_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.descricao_produto_label)
        self.v_layout_esquerda.addWidget(self.descricao_produto_edit)

        self.quantidade_produto_label = QLabel("Quantidade do Produto")
        self.quantidade_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.quantidade_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.quantidade_produto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)

        self.preço_produto_label = QLabel("Preço do Produto")
        self.preço_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.preço_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.preço_produto_label)
        self.v_layout_esquerda.addWidget(self.preço_produto_edit)

        self.subtotal_produto_label = QLabel("Subtotal do Produto")
        self.subtotal_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.subtotal_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.subtotal_produto_label)
        self.v_layout_esquerda.addWidget(self.subtotal_produto_edit)



        # adicionar o layout vertical da esquerda com todos os controles: label e lineEdit dentro da coluna da
        # esquerda(label_coluna_esquerda)
        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)

        #------------ Controles da coluna da direita ------------
        self.v_layout_direita = QVBoxLayout()

        # Criar uma tabela e adicionar na coluna da direita esta tabela terá os nomes dos campos que estão ao esquerdo
        # Coluna da tabela
        colunas = ["Cod.Produto","Nome do Produto","Deacrição do Produto","Quantidade","Preço Unitário","Subtotal"]
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.v_layout_direita.addWidget(self.tabela)

        self.total_pagar_label = QLabel("Total a Pagar")
        self.total_pagar_edit = QLineEdit("0,00")
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_pagar_edit)

        self.label_coluna_direita.setLayout(self.v_layout_direita)

        #Criar o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        # Vamos adicionar as colunas esquerda e direita ao layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        #Adicionar o layout na tela
        self.setLayout(self.h_layout) 

app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()