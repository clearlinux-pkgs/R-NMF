#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-NMF
Version  : 0.21.0
Release  : 17
URL      : https://cran.r-project.org/src/contrib/NMF_0.21.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/NMF_0.21.0.tar.gz
Summary  : Algorithms and Framework for Nonnegative Matrix Factorization
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-NMF-lib = %{version}-%{release}
BuildRequires : R-RColorBrewer
BuildRequires : R-Rcpp
BuildRequires : R-bibtex
BuildRequires : R-colorspace
BuildRequires : R-doParallel
BuildRequires : R-foreach
BuildRequires : R-ggplot2
BuildRequires : R-gridBase
BuildRequires : R-gtable
BuildRequires : R-lazyeval
BuildRequires : R-munsell
BuildRequires : R-pkgmaker
BuildRequires : R-plyr
BuildRequires : R-registry
BuildRequires : R-reshape2
BuildRequires : R-rngtools
BuildRequires : R-scales
BuildRequires : R-tibble
BuildRequires : R-withr
BuildRequires : R-xtable
BuildRequires : buildreq-R
BuildRequires : texlive

%description
## Background
Nonnegative Matrix Factorization (NMF) is an unsupervised learning technique that has been applied successfully in several fields, including signal processing, face recognition and text mining.
Recent applications of NMF in bioinformatics have demonstrated its ability to extract meaningful information from high-dimensional data such as gene expression microarrays. Developments in NMF theory and applications have resulted in a variety of algorithms and methods.
However, most NMF implementations have been on commercial platforms, while those that are freely available typically require programming skills.
This limits their use by the wider research community.

%package lib
Summary: lib components for the R-NMF package.
Group: Libraries

%description lib
lib components for the R-NMF package.


%prep
%setup -q -c -n NMF

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552881502

%install
export SOURCE_DATE_EPOCH=1552881502
rm -rf %{buildroot}
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
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  NMF || :


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
