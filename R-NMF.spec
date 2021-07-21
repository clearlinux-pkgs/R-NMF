#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-NMF
Version  : 0.21.0
Release  : 33
URL      : https://cran.r-project.org/src/contrib/NMF_0.21.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/NMF_0.21.0.tar.gz
Summary  : Algorithms and Framework for Nonnegative Matrix Factorization
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-NMF-lib = %{version}-%{release}
Requires: R-RColorBrewer
Requires: R-colorspace
Requires: R-digest
Requires: R-doParallel
Requires: R-foreach
Requires: R-ggplot2
Requires: R-gridBase
Requires: R-pkgmaker
Requires: R-registry
Requires: R-reshape2
Requires: R-rngtools
Requires: R-stringr
BuildRequires : R-RColorBrewer
BuildRequires : R-colorspace
BuildRequires : R-digest
BuildRequires : R-doParallel
BuildRequires : R-foreach
BuildRequires : R-ggplot2
BuildRequires : R-gridBase
BuildRequires : R-pkgmaker
BuildRequires : R-registry
BuildRequires : R-reshape2
BuildRequires : R-rngtools
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
Factorization (NMF). The package implements a set of already published algorithms
    and seeding methods, and provides a framework to test, develop and plug
    new/custom algorithms. Most of the built-in algorithms have been optimized
    in C++, and the main interface function provides an easy way of performing
    parallel computations on multicore machines.

%package lib
Summary: lib components for the R-NMF package.
Group: Libraries

%description lib
lib components for the R-NMF package.


%prep
%setup -q -c -n NMF
cd %{_builddir}/NMF

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590005788

%install
export SOURCE_DATE_EPOCH=1590005788
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NMF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NMF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NMF
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc NMF || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/NMF/CITATION
/usr/lib64/R/library/NMF/DESCRIPTION
/usr/lib64/R/library/NMF/INDEX
/usr/lib64/R/library/NMF/Meta/Rd.rds
/usr/lib64/R/library/NMF/Meta/data.rds
/usr/lib64/R/library/NMF/Meta/demo.rds
/usr/lib64/R/library/NMF/Meta/features.rds
/usr/lib64/R/library/NMF/Meta/hsearch.rds
/usr/lib64/R/library/NMF/Meta/links.rds
/usr/lib64/R/library/NMF/Meta/nsInfo.rds
/usr/lib64/R/library/NMF/Meta/package.rds
/usr/lib64/R/library/NMF/Meta/vignette.rds
/usr/lib64/R/library/NMF/NAMESPACE
/usr/lib64/R/library/NMF/NEWS
/usr/lib64/R/library/NMF/R/NMF
/usr/lib64/R/library/NMF/R/NMF.rdb
/usr/lib64/R/library/NMF/R/NMF.rdx
/usr/lib64/R/library/NMF/REFERENCES.bib
/usr/lib64/R/library/NMF/data/esGolub.rda
/usr/lib64/R/library/NMF/demo/aheatmap.R
/usr/lib64/R/library/NMF/demo/heatmaps.R
/usr/lib64/R/library/NMF/demo/nmf.R
/usr/lib64/R/library/NMF/doc/NMF-vignette.R
/usr/lib64/R/library/NMF/doc/NMF-vignette.Rnw
/usr/lib64/R/library/NMF/doc/NMF-vignette.pdf
/usr/lib64/R/library/NMF/doc/consensus.pdf
/usr/lib64/R/library/NMF/doc/heatmaps.R
/usr/lib64/R/library/NMF/doc/heatmaps.Rnw
/usr/lib64/R/library/NMF/doc/heatmaps.pdf
/usr/lib64/R/library/NMF/doc/index.html
/usr/lib64/R/library/NMF/help/AnIndex
/usr/lib64/R/library/NMF/help/NMF.rdb
/usr/lib64/R/library/NMF/help/NMF.rdx
/usr/lib64/R/library/NMF/help/aliases.rds
/usr/lib64/R/library/NMF/help/paths.rds
/usr/lib64/R/library/NMF/html/00Index.html
/usr/lib64/R/library/NMF/html/R.css
/usr/lib64/R/library/NMF/scripts/grid.R
/usr/lib64/R/library/NMF/scripts/report.Rmd

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/NMF/libs/NMF.so
/usr/lib64/R/library/NMF/libs/NMF.so.avx2
/usr/lib64/R/library/NMF/libs/NMF.so.avx512
