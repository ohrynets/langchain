import pandas
import json
#from langchain import PromptTemplate
#from langchain.llms import OpenAI
#from langchain.chat_models import ChatOpenAI
#from langchain.callbacks import get_openai_callback
#from langchain.prompts.chat import HumanMessagePromptTemplate

#from langchain.schema import (
    #AIMessage,
    #HumanMessage,
    #SystemMessage
#)

class Job_descrition_store:
    j = []
    def init(self):
        self.j = []


    def load_csv(self, data_name='data.csv'):
        df = pandas.read_csv(data_name)
        for index, row in df.iterrows():
            desc = row['Job Description']
            new_desc = Job_descritor(desc)
            self.j.append(new_desc.__dict__)
        return(self.j)


    def save_json(self, file_name='data.json'):
        desc_list = self.j
        with open(file_name, "w") as fp:
            json.dump(desc_list, fp, indent=4)   
        return 

class Job_descritor:

    def __init__(self, desc):
        self.desc = desc
    
    def get_desc(self):
        return self.desc


if __name__ == "__main__":
    job_description = Job_descrition_store()
    job_description.load_csv()
    print(job_description.save_json())
 