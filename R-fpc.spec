#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fpc
Version  : 2.1.11.1
Release  : 14
URL      : https://cran.r-project.org/src/contrib/fpc_2.1-11.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fpc_2.1-11.1.tar.gz
Summary  : Flexible Procedures for Clustering
Group    : Development/Tools
License  : GPL-2.0
Requires: R-flexmix
Requires: R-kernlab
Requires: R-mclust
Requires: R-mvtnorm
Requires: R-pdfCluster
Requires: R-prabclus
Requires: R-robustbase
Requires: R-tclust
Requires: R-trimcluster
BuildRequires : R-flexmix
BuildRequires : R-kernlab
BuildRequires : R-mclust
BuildRequires : R-mvtnorm
BuildRequires : R-pdfCluster
BuildRequires : R-prabclus
BuildRequires : R-robustbase
BuildRequires : R-tclust
BuildRequires : R-trimcluster
BuildRequires : clr-R-helpers

%description
Fixed point clustering. Linear regression clustering. Clustering by 
  merging Gaussian mixture components. Symmetric 
  and asymmetric discriminant projections for visualisation of the 
  separation of groupings. Cluster validation statistics
  for distance based clustering including corrected Rand index. 
  Cluster-wise cluster stability assessment. Methods for estimation of

%prep
%setup -q -c -n fpc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532099950

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532099950
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fpc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fpc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fpc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fpc|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fpc/DESCRIPTION
/usr/lib64/R/library/fpc/INDEX
/usr/lib64/R/library/fpc/Meta/Rd.rds
/usr/lib64/R/library/fpc/Meta/data.rds
/usr/lib64/R/library/fpc/Meta/features.rds
/usr/lib64/R/library/fpc/Meta/hsearch.rds
/usr/lib64/R/library/fpc/Meta/links.rds
/usr/lib64/R/library/fpc/Meta/nsInfo.rds
/usr/lib64/R/library/fpc/Meta/package.rds
/usr/lib64/R/library/fpc/NAMESPACE
/usr/lib64/R/library/fpc/R/fpc
/usr/lib64/R/library/fpc/R/fpc.rdb
/usr/lib64/R/library/fpc/R/fpc.rdx
/usr/lib64/R/library/fpc/data/tonedata.txt.gz
/usr/lib64/R/library/fpc/help/AnIndex
/usr/lib64/R/library/fpc/help/aliases.rds
/usr/lib64/R/library/fpc/help/fpc.rdb
/usr/lib64/R/library/fpc/help/fpc.rdx
/usr/lib64/R/library/fpc/help/paths.rds
/usr/lib64/R/library/fpc/html/00Index.html
/usr/lib64/R/library/fpc/html/R.css
