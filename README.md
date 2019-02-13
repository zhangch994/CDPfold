# 5sRNA secondary structure prediction process
1.data_pre_treatment.py----------------------------->Data preprocessing(Extract sequence and structure data)
2.data_select_5s_seq.py/data_select_5s_stru.py------>Pick out 5sRNA data
3.train_to_labelpng.py------------------------------>RNA representation and sliding window algorithm
4.trainning_data_standarding.py--------------------->Data normalization
5.base_balance.py----------------------------------->Balanced data
6.input.py/model.py--------------------------------->Convolutional neural network input and model
7.trainning.py-------------------------------------->Training model
8.validation.py------------------------------------->Validation model
9.test.py------------------------------------------->Test model

# General RNA secondary structure prediction process
1.delete_pseudoknot.py------------------------------>Delete pseudoknot data
2.data_pre_treatment.py----------------------------->Data preprocessing(Extract sequence and structure data)
3.train_to_labelpng.py------------------------------>RNA representation and sliding window algorithm
4.trainning_data_standarding.py--------------------->Data normalization
5.base_balance.py----------------------------------->Balanced data
6.input.py/model.py--------------------------------->Convolutional neural network input and model
7.trainning.py-------------------------------------->Training model
8.validation.py------------------------------------->Validation model
9.test.py------------------------------------------->Test model
