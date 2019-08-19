from django.db import models

# Create your models here.
class staffs(models.Model):
    id = models.IntegerField(primary_key=True)  
    communication_id = models.IntegerField()  #一事通id
    username = models.CharField(max_length=50)  #用户名字
    password = models.CharField(max_length=16)  #密码
    email = models.CharField(max_length=50)    #邮箱
    room_Manager1_id = models.IntegerField()   #一级室经理id
    room_Manager2_id = models.IntegerField()    #二级室经理id
    room_add = models.CharField(max_length=50)  #室地址
    role = models.IntegerField()   #（0为答辩人员，1为评审人员，2为管理人员）

class templates(models.Model):
    id = models.IntegerField(primary_key=True)
    template_name = models.CharField(max_length=50) #材料名称
    path = models.CharField(max_length=255) #材料路径
    
class plans(models.Model):
    defense_id = models.IntegerField()  #答辩人员的id
    defense_time = models.IntegerField() #答辩时间
    review1_id = models.IntegerField()  #评委1
    review2_id = models.IntegerField()  #评委2
    review3_id = models.IntegerField()  #评委3
    denfense_add = models.CharField(max_length=255) #答辩地址
    tutor_id = models.IntegerField()  #导师id
    score = models.IntegerField()  #分数
    proposal = models.CharField(max_length=200) #评委意见