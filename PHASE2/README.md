```
# SBMN Interviewer – Phase 2 Experimental Artifacts

This repository contains the artifacts generated during **Phase 2 of the experiments** described in the study on SBMN-based business process control-flow elicitation using LLM interviewers.

In this phase, the **Structured SBMN Interviewer prompt** was used to conduct elicitation interviews with domain experts. The resulting SBMN models were then transformed into BPMN models and evaluated.

The repository provides the materials required to understand and reproduce the experimental setup.

---

# Repository Structure

The repository is organized as follows:

### 1. Appendix
This folder contains the **complete interview reports generated during the elicitation sessions**.

Each document includes:

- Process overview
- Activity list (AFOs)
- Interview statistics
- Interview transcript (questions and answers)
- Final SBMN model
- Consistency verification results

These files document the full interaction between the interviewer and the domain expert.

---

### 2. MODELS_BPMN

This folder contains BPMN process models used during the experiments.

It is divided into two subfolders:

**rm_bpmn**
- Reference BPMN models used as the ground truth processes for the experiments.

**results_bpmn**
- BPMN models generated from the SBMN models obtained during the interviews.

These models were later used for experimental evaluation.

---

### 3. MODELS_SBMN

This folder contains the **SBMN models produced from the elicitation interviews**.

Each model represents the control-flow constraints identified during the interview process.

---

### 4. StructuredPrompt_V8_EN

This file contains the **structured prompt used to configure the SBMN interviewer in Phase 2**.

The prompt defines:

- the interview protocol
- the SBMN operators and their semantics
- the reasoning rules used during elicitation
- consistency verification mechanisms

---

### 5. readBPMN_EN

This script allows the visualization of BPMN models stored in the repository.

It uses the **pm4py** library and **Graphviz** to generate graphical representations of BPMN files.

---

# BPMN Model Visualization

To visualize BPMN models, run the script:
readBPMN.py


A dialog window will appear allowing you to select the folder containing the BPMN files.

---

# System Requirements

Before executing the visualization script, make sure the following dependencies are installed.

### Install Graphviz

Download from:

https://graphviz.org/download/

---

### Install Python dependencies
pip install pm4py
pip install graphviz


---

# Experimental Context

These artifacts correspond to the **Phase 2 evaluation**, in which the structured SBMN interviewer was applied to multiple process cases.

The experiments generated:

- elicitation interview transcripts
- SBMN models derived from interviews
- BPMN models generated from SBMN
- supporting documentation for the elicitation process

The repository is intended to support **transparency, reproducibility, and inspection of the elicitation process**.