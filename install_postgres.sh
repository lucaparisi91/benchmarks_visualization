cd /tmp
wget https://ftp.postgresql.org/pub/source/v17.2/postgresql-17.2.tar.bz2
tar -xvf postgresql-17.2.tar.bz2
cd postgresql-17.2
./configure
make 
make install