import pm4py
from pm4py.visualization.bpmn import visualizer
import tkinter as tk
from tkinter import filedialog
import os
def selecionar_arquivo_bpmn():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    file_path = filedialog.askopenfilename(
        initialdir=".",  # Pasta atual do programa
        title="Selecione o arquivo BPMN",
        filetypes=[("Arquivos BPMN", "*.bpmn")]  # Apenas arquivos .bpmn
    )
    return file_path

def visualize_bpmn(file_path):
    # Carregar o modelo BPMN a partir do arquivo
    bpmn_model = pm4py.read_bpmn(file_path)
    # Gerar a visualização do modelo BPMN
    print(f'Mostrando o modelo {file_path}  ')
    gviz = visualizer.apply(bpmn_model)
    
    # Tentar visualizar no próprio ambiente gráfico
    visualizer.view(gviz)

    # Forçar o fechamento da visualização
    input("Pressione Enter para fechar a visualização...")
def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    folder_path = filedialog.askdirectory(
        initialdir=".",  # Pasta inicial
        title="Selecione a pasta com arquivos BPMN"
    )
    return folder_path
# Função para visualizar todos os arquivos BPMN em uma pasta
def visualize_all_bpmn_in_folder():
    folder_path = selecionar_pasta()
    if folder_path:
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".bpmn"):
                file_path = os.path.join(folder_path, file_name)
                visualize_bpmn(file_path)  # Chama a função para visualizar cada arquivo BPMN
        print(f"Visualizações geradas para todos os arquivos BPMN em: {folder_path}")
    else:
        print("Nenhuma pasta foi selecionada.")


if __name__ == "__main__":
  visualize_all_bpmn_in_folder()
  """"
    # Caminho do arquivo BPMN
    file_path =selecionar_arquivo_bpmn()
if file_path:
    print(f"Arquivo selecionado: {file_path}")
     # Visualizar o BPMN
    visualize_bpmn(file_path)
else:
    print("Nenhum arquivo foi selecionado.")
 """  

   
    

