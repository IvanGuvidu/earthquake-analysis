from data_set_gen import data_set_gen
from complete_split_data import complete_data_and_split
from grafice import grafice
from eval_model import eval_model

df = data_set_gen()
complete_data_and_split(df)
grafice(df)
eval_model()