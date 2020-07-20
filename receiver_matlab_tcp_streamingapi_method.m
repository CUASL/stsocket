clear; clc;
t = tcpip('127.0.0.1', 3001, 'NetworkRole', 'server');
t.InputBufferSize = 1000000 ;
index = 0 ;
array = {} ;
while(1)
    fopen(t)
    pause(0.1)
    text = char(fread(t,[1, t.BytesAvailable]));
    
    data = jsondecode(text);
    array = [array,data] ;
    id = data.id
    message = data.text
    time = data.created_at
    fclose(t)
    index = index+1
 end