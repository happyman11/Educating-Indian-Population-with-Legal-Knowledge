
from django.db import models
from django.utils import timezone


class FileModel(models.Model):
    Act_name = models.CharField(max_length=100)  
    updated_on = models.DateTimeField(default=timezone.now)  
    doc = models.FileField(upload_to='media/')  

    def __str__(self):
        return self.Act_name
    


class VectorDBInformation(models.Model):
    Type = models.CharField(max_length=100)  
    Checked_on = models.DateTimeField(default=timezone.now)  
    DB_name = models.CharField(max_length=100)
    Status = models.BooleanField(default=False)  
    Records_count = models.IntegerField(default=0)  
    Path=models.CharField(max_length=1000)


    def __str__(self):
        return f"{self.DB_name} - {self.Type}"



MODEL_CHOICES = [
                        ("gemini-2.0-flash", "GOOGLE>gemini-2.0-flash"),
                        ("gemini-2.5-flash", "GOOGLE>gemini-2.5-flash"),
                        ("gemini-2.5-pro", "GOOGLE>gemini-2.5-pro"),
                        ("gemini-1.5-flash","GOOGLE>gemini-1.5-flash"),
                        ("gemma3:4b", "OLLAMA>gemma3:4b"),
                        ("llama3.2:latest", "OLLAMA>llama3.2:latest"),
                        ("llama3.2:1b", "OLLAMA>llama3.2:1b"),
                        ("deepseek-r1:latest", "OLLAMA>deepseek-r1:latest"),
                        ("gemma2:2b", "OLLAMA>gemma2:2b"),
                        ("deepseek-r1:1.5b", "OLLAMA>deepseek-r1:1.5b"),
                        ("llama2:chat", "OLLAMA>llama2:chat"),
                        ("llama3.2:latest", "OLLAMA>llama3.2:latest"),
                        ("meta/Llama-4-Scout-17B-16E-Instruct(github)", "GithubModels>Openai-GPT-5"),
                        ]
    
class BareActsAgentConfiguration(models.Model):
    Model_Name=models.CharField(max_length=50,choices=MODEL_CHOICES, default="gemini-2.0-flash")
    Router_Model=models.CharField(max_length=50,choices=MODEL_CHOICES, default="gemini-2.0-flash")
    Retriever_Model=models.CharField(max_length=50,choices=MODEL_CHOICES, default="gemini-2.0-flash")
    Grader_Model=models.CharField(max_length=50,choices=MODEL_CHOICES, default="gemini-2.5-flash")
    Answer_Model=models.CharField(max_length=50,choices=MODEL_CHOICES, default="gemini-2.5-pro")
    def __str__(self):
        return f"{self.Model_Name}-{self.Router_Model}-{self.Retriever_Model}-{self.Grader_Model}-{self.Answer_Model}"
  
WEB_MODEL_CHOICES = [
                        ("gemini-2.0-flash", "GOOGLE>gemini-2.0-flash"),
                        ("gemini-2.5-flash", "GOOGLE>gemini-2.5-flash"),
                        ("gemini-2.5-pro", "GOOGLE>gemini-2.5-pro"),
                        ("gemini-1.5-flash","GOOGLE>gemini-1.5-flash"),
                    ]  
class WebsearchAgentConfiguration(models.Model):
    Querry_Generator_Model=models.CharField(max_length=50,choices=WEB_MODEL_CHOICES, default="gemini-2.0-flash")
    Reflexion_Model=models.CharField(max_length=50,choices=WEB_MODEL_CHOICES, default="gemini-2.5-flash")
    Answer_Model=models.CharField(max_length=50,choices=WEB_MODEL_CHOICES, default="gemini-2.5-pro")
    Initial_Querry=models.SmallIntegerField(default=3)
    Max_Research_Loops=models.SmallIntegerField(default=2)
    def __str__(self):
        return f"{self.Querry_Generator_Model}-{self.Reflexion_Model}-{self.Answer_Model}-{self.Initial_Querry}-{self.Max_Research_Loops}"

class ReflexionAgentConfiguration(models.Model):
    Reflexion_Model=models.CharField(max_length=50,choices=MODEL_CHOICES, default="gemini-2.5-pro")
    def __str__(self):
        return f"{self.Reflexion_Model}"
    

class Extension_Data(models.Model):
    Thread_Id=models.TextField(blank=True, null=True, default="")
    User_Querry=models.TextField(blank=True, null=True, default="")
    Web_Search_Answer=models.TextField(blank=True, null=True, default="")
    IT_Act_Answer=models.TextField(blank=True, null=True, default="")
    IT_Act_Document=models.TextField(blank=True, null=True, default="")
    BNS_Act_Answer=models.TextField(blank=True, null=True, default="")
    BNS_Act_Document=models.TextField(blank=True, null=True, default="")
    BSA_Act_Answer=models.TextField(blank=True, null=True, default="")
    BSA_Act_Document=models.TextField(blank=True, null=True, default="")
    DPDP_Act_Answer=models.TextField(blank=True, null=True, default="")
    DPDP_Act_Document=models.TextField(blank=True, null=True, default="")
    Acts_Combined_Answers=models.TextField(blank=True, null=True, default="")
    Web_Bare_Act_Combined=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
   
     
    def __str__(self):
        return f"{self.Thread_Id}"
    
    
class Extension_Data_BSA(models.Model):
    Thread_Id=models.TextField(blank=True, null=True, default="")
    User_Querry=models.TextField(blank=True, null=True, default="")
    BSA_Act_Answer=models.TextField(blank=True, null=True, default="")
    BSA_Act_Document=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.Thread_Id}"
    
class Extension_Data_BNS(models.Model):
    Thread_Id=models.TextField(blank=True, null=True, default="")
    User_Querry=models.TextField(blank=True, null=True, default="")
    BNS_Act_Answer=models.TextField(blank=True, null=True, default="")
    BNS_Act_Document=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.Updated_on}"

class Extension_Data_DPDP(models.Model):
    Thread_Id=models.TextField(blank=True, null=True, default="")
    User_Querry=models.TextField(blank=True, null=True, default="")
    DPDP_Act_Answer=models.TextField(blank=True, null=True, default="")
    DPDP_Act_Document=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.Updated_on}"
    
class Extension_Data_IT(models.Model):
    Thread_Id=models.TextField(blank=True, null=True, default="")
    User_Querry=models.TextField(blank=True, null=True, default="")
    IT_Act_Answer=models.TextField(blank=True, null=True, default="")
    IT_Act_Document=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.Thread_Iddated_on}"
    
class Extension_Data_Web_Search(models.Model):
    Thread_Id=models.TextField(blank=True, null=True, default="")
    User_Querry=models.TextField(blank=True, null=True, default="")
    Web_Answer=models.TextField(blank=True, null=True, default="")
    Search_Querry=models.TextField(blank=True, null=True, default="")
    Sources_Gathered=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.Thread_Id}"


class Githhub_Model_API(models.Model):
    API_Path_Githhub=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.API_Path_Githhub}"
    
class Langgraph_Deployed_API(models.Model):
    API_Path=models.TextField(blank=True, null=True, default="")
    Updated_on = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.API_Path}"

class Langgraph_Deployed_Agent_Name(models.Model):
    Web_Search_Agent=models.TextField(default="agent_WS")
    DPDP_Agent=models.TextField(default="agent_DPDP")
    BSA_Agent=models.TextField(default="agent_BSA")
    BNS_Agent=models.TextField(default="agent_BNS")
    IT_Agent=models.TextField(default="agent_IT")
    Chat=models.TextField(default="agent_all")
    Updated_on = models.DateTimeField(default=timezone.now) 
    API_Link= models.ForeignKey(Langgraph_Deployed_API, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Updated_on}"
    
class Visual_explanation(models.Model):
    Thread_Id=models.TextField(blank=True, null=True, default="")
    doc = models.FileField(upload_to='media/') 
    agent_name=models.TextField(default="agent_DPDP")
    Updated_on = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return f"{self.Updated_on}"
    
    


    