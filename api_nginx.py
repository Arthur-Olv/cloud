server {
    listen 80;   
    server_name 34.248.235.255;    
    location / {        
        proxy_pass http://127.0.0.1:8000;    
    }
}