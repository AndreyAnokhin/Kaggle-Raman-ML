## Raman spectroscopy of Diabetes

Dataset from https://www.kaggle.com/codina/raman-spectroscopy-of-diabetes

### Context

This is the dataset of our work where the application of portable Raman spectroscopy coupled with several supervised machine-learning techniques, is used to discern between diabetic patients (DM2) and healthy controls (Ctrl), with a high degree of accuracy.

### Content

The 4 CSV files contain the average of five Raman spectroscopy scans at 12 cm-1 resolution collected at different skin sites, such as the left earlobe, left inner arm, left thumbnail and left median cubital vein, with approximately 15 s total exposure time.
Please download code to read and plot the data from: https://github.com/guevaracodina/raman-diabetes

### Acknowledgements

Please cite: Guevara, E., Torres-Galván, J. C., Ramírez-Elías, M. G., Luevano-Contreras, C., & González, F. J. (2018). Use of Raman spectroscopy to screen diabetes mellitus with machine learning tools. Biomedical Optics Express, 9(10), 4998–5010. https://doi.org/10.1364/BOE.9.004998

### About this file

This file contains the average of five scans at 12 cm-1 resolution collected at the left earlobe, with approximately 15 s total exposure time, for N=20 subjects (11 diabetic patients and 9 healthy controls) The first row is a header with the variable names The second row has the wavenumbers of the Raman shift, from 0 to 3159 cm^-1 Rows 3 - 22 contain the Raman spectra of each subject, rows from 3 to 13 correspond to Diabetes Mellitus type 2 patients, while rows 14 to 22 correspond to controls

### Columns:

* `patientID` - Identifies the group to which patient belongs: DM2 if diabetic, Ctrl if healthy control
* `has_DM2` - flags subject group, true if subject has diabetes mellitus 2, false if healthy control
* `Var2-Var3161` - contain the Raman spectra of each sample, at the corresponding Raman shift from 0 to 3159 cm^-1