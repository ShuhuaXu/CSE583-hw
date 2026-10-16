mkdir pronto
cd pronto
echo 'The Pronto Bike dataset contains trip-level records from Seattle’s former bike-sharing system, including ride times, station locations, and bicycle usage information.' > README.txt
mkdir data
cd data
curl -O 'https://s3.amazonaws.com/pronto-data/open_data_year_one.zip'
unzip open_data_year_one.zip
head *.csv
