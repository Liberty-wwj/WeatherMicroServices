# WeatherMicroServices

# Step1: Create your own network in Docker
docker network create --subnet=172.22.0.0/16 cs571_n1 

# Step2: Build an image for weather_service
docker build . -f DOCKERFILE -t weather_s_v1 

# Step3: Run the weather_service contanier
docker run -d --name c_weather_service_v1 --network cs571_n1 --hostname hn_weather --ip 172.22.0.1 -p 8600:5000 weather_s_v1

# Step4: Build an image for city_name to weather
docker build . -f DOCKERFILE -t zip_s_v1   

# Step5: Run the city_name_to_weather container
docker run -d --name c_zip_service_v1 --network cs571_n1 --hostname hn_zip --ip 172.22.0.2 -p 8601:5000 zip_s_v1

# How to access the service to get weather for a specific city?
    You can use this format of URL: http://127.0.0.1:8601/zipcode/ca/milpitas
    Please keep in mind that you need to have both state name and city name 

![Result pic](https://user-images.githubusercontent.com/98154132/217987084-1a33d13f-c9a5-438c-9baa-53ccc9392e97.jpg)
