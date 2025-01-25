FROM fedora:latest 
RUN dnf update -y
RUN dnf group -y install development-tools
RUN dnf install -y wget icu vim bison flex ghc-readline ghc-readline-devel perl-FindBin "perl-File*" libicu-devel

#WORKDIR /usr/share/grafana
#ENTRYPOINT ["/usr/share/grafana/bin/grafana","server"]


