import pm4py
from pm4py.visualization.bpmn import visualizer
import tkinter as tk
from tkinter import filedialog
import os
def select_bpmn_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    file_path = filedialog.askopenfilename(
        initialdir=".",  # Current program folder
        title="Select the BPMN file",
        filetypes=[("Files BPMN", "*.bpmn")]  # Only .bpmn files
    )
    return file_path

def visualize_bpmn(file_path):
    # Load the BPMN model from the file
    bpmn_model = pm4py.read_bpmn(file_path)
    # Generate the BPMN model visualization
    print(f'Showing the model {file_path}  ')
    gviz = visualizer.apply(bpmn_model)
    
    # Try to display it in the graphical environment itself
    visualizer.view(gviz)

    # Force the visualization to close
    input("Press Enter to close the visualization...")
def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    folder_path = filedialog.askdirectory(
        initialdir=".",  # Initial folder
        title="Select the folder with BPMN files"
    )
    return folder_path
# Function to visualize all BPMN files in a folder
def visualize_all_bpmn_in_folder():
    folder_path = selecionar_pasta()
    if folder_path:
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".bpmn"):
                file_path = os.path.join(folder_path, file_name)
                visualize_bpmn(file_path)  # Call the function to visualize each BPMN file
        print(f"Visualizations generated for all BPMN files in: {folder_path}")
    else:
        print("No folder was selected.")


if __name__ == "__main__":
  visualize_all_bpmn_in_folder()
  """"
    # BPMN file path
    file_path =select_bpmn_file()
if file_path:
    print(f"Selected file: {file_path}")
     # Visualizar o BPMN
    visualize_bpmn(file_path)
else:
    print("No file was selected.")
 """  

   
    


