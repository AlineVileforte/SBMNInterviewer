Prompts-Nire2026

# Repositório de Experimentos de Elicitação de Processos de Negócio em SBMN

Este repositório contém os artefatos e recursos utilizados nos experimentos de elicitação de requisitos de processos de negócio baseados na notação SBMN (Simplified Business Process Model and Notation), conduzidos como parte da pesquisa de mestrado.

# Estrutura do Repositório

O repositório está organizado nas seguintes seções:

1. **Prompts de Elicitação**: Conjunto de prompts desenvolvidos para a elicitação de processos, incluindo abordagens simples e estruturadas
2. **Modelos BPMN**: Modelos em BPMN utilizados como casos de teste para validação dos prompts
3. **Modelos SBMN**: Modelos em notação SBMN produzidos pela aplicação dos prompts nos casos de teste
4. **Métricas**: Cálculos e resultados das métricas aplicadas para avaliação quantitativa dos experimentos

# Visualização dos Modelos BPMN

Para visualização gráfica dos arquivos BPMN, utilize o script `readBPMN.py` disponível neste repositório.

# Requisitos de Sistema

Antes de executar o script de visualização, certifique-se de:

1. Instalar o **Graphviz** no sistema operacional ([https://graphviz.org/download/](https://graphviz.org/download/))
2. Instalar as dependências Python:
   pip install pm4py
   pip install graphviz
 
# Execução

Ao executar o script `readBPMN.py`, uma janela de diálogo será exibida para seleção da pasta contendo os arquivos BPMN a serem visualizados.
