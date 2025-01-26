wget https://ftp.postgresql.org/pub/source/v17.2/postgresql-17.2.tar.bz2
tar -xvf postgresql-17.2.tar.bz2
cd postgresql-17.2
./configure
make 
make install

# mkdir -p /usr/local/pgsql/data
# chown postgres /usr/local/pgsql/data
# su - postgres
# /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
# /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
# /usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start
# export PATH=/usr/local/pgsql:$PATH