# hotel-price-comparison-api
Extracting price of hotel rooms and comparing them(MakCorps)


This project is all about extracting prices from more than 200 websites like expedia and hotels.com. This API provides you with prices from different websites and reviews and ratings of the hotel.

Please, do not abuse the terms and conditions of the project. Hope this project can help junior developers to make android and web apps on hotel management.



So here , we have stated two simple steps through CURL to make a query to our API.

1) JWT token.

curl --request POST \
  --url 'https://api.makcorps.com/auth' \
  --header 'Content-Type: application/json' \
  --data '{
	"username":"xxxxx",
	"password":"xxxxx"
}'

2) Get request to our /city endpoint 


curl --request GET \
  --url https://api.makcorps.com/free/london \
  --header 'Authorization: JWT eyJ0eXAiOiJKV1Q'


put your JWT token after JWT in step 2



