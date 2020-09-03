import requests 


header  =  {
    "Content-Type" : "application/x-www-form-urlencoded" , 
    "Authorization" : "Basic REFERTFFMDYtOUU5NS00RDNELUI5OUUtRkU0MzQ5QjdCOEFGOmU4OXlmVFk4eTF3MzRMT0NJSlhyelBTTzJzNkxVMnBGL2hPUHI0QWk3ODZzTjlYdGZ1bEVCZVFnVWNOSk1xYmdJNzNuam4vNXR2T0cyOTlCVFc1TXBBPT0="
}

body = {
    "message" : "test" , 
    "message_type" : 'ARN' ,
    "phone_number" : "212616952526" , 
    "sender_id" : 'Shirou'
}


res = requests.post("https://rest-api.telesign.com/v1/messaging" , data= body , headers = header)

print(dir(res))