#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : pypi-orjson
Version  : 3.10.16
Release  : 20
URL      : https://files.pythonhosted.org/packages/98/c7/03913cc4332174071950acf5b0735463e3f63760c80585ef369270c2b372/orjson-3.10.16.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/c7/03913cc4332174071950acf5b0735463e3f63760c80585ef369270c2b372/orjson-3.10.16.tar.gz
Summary  : Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT Unlicense
Requires: pypi-orjson-license = %{version}-%{release}
Requires: pypi-orjson-python = %{version}-%{release}
Requires: pypi-orjson-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(maturin)
BuildRequires : pypi-maturin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# orjson
orjson is a fast, correct JSON library for Python. It
[benchmarks](https://github.com/ijl/orjson?tab=readme-ov-file#performance) as the fastest Python
library for JSON and is more correct than the standard json library or other
third-party libraries. It serializes
[dataclass](https://github.com/ijl/orjson?tab=readme-ov-file#dataclass),
[datetime](https://github.com/ijl/orjson?tab=readme-ov-file#datetime),
[numpy](https://github.com/ijl/orjson?tab=readme-ov-file#numpy), and
[UUID](https://github.com/ijl/orjson?tab=readme-ov-file#uuid) instances natively.

%package license
Summary: license components for the pypi-orjson package.
Group: Default

%description license
license components for the pypi-orjson package.


%package python
Summary: python components for the pypi-orjson package.
Group: Default
Requires: pypi-orjson-python3 = %{version}-%{release}

%description python
python components for the pypi-orjson package.


%package python3
Summary: python3 components for the pypi-orjson package.
Group: Default
Requires: python3-core
Provides: pypi(orjson)

%description python3
python3 components for the pypi-orjson package.


%prep
%setup -q -n orjson-3.10.16
cd %{_builddir}/orjson-3.10.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742848446
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-orjson
cp %{_builddir}/orjson-%{version}/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/bytecount-0.6.8/LICENSE.Apache2 %{buildroot}/usr/share/package-licenses/pypi-orjson/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/orjson-%{version}/include/cargo/bytecount-0.6.8/LICENSE.MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/9ec2af04328d0eb6ec89ca6d75156ffc7aecf869 || :
cp %{_builddir}/orjson-%{version}/include/cargo/castaway-0.2.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/fd33e0d46674b32eb66a5f1134e8d8a2d2f684c9 || :
cp %{_builddir}/orjson-%{version}/include/cargo/cc-1.2.17/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/include/cargo/cc-1.2.17/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/orjson-%{version}/include/cargo/cfg-if-1.0.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/include/cargo/cfg-if-1.0.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/orjson-%{version}/include/cargo/compact_str-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/5c59637187123fdaf921408bc38718e196e5ee9a || :
cp %{_builddir}/orjson-%{version}/include/cargo/crunchy-0.2.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/ef9d72cbd46e61ffd8d8a6f906ff553eb5f6233c || :
cp %{_builddir}/orjson-%{version}/include/cargo/encoding_rs-0.8.35/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/orjson-%{version}/include/cargo/encoding_rs-0.8.35/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/b4872d72eb3ccfa74730cc229184eec04f303e7d || :
cp %{_builddir}/orjson-%{version}/include/cargo/encoding_rs-0.8.35/LICENSE-WHATWG %{buildroot}/usr/share/package-licenses/pypi-orjson/1e35cd39af07e5460de3011d5ef8f6a775ee54ae || :
cp %{_builddir}/orjson-%{version}/include/cargo/gimli-0.31.1/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/include/cargo/gimli-0.31.1/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/orjson-%{version}/include/cargo/half-2.5.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/a6a5418b4d67d9f3a33cbf184b25ac7f9fa87d33 || :
cp %{_builddir}/orjson-%{version}/include/cargo/half-2.5.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/218fc8c15534e8840cbff5801582c450c97869ab || :
cp %{_builddir}/orjson-%{version}/include/cargo/itoa-1.0.15/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/itoa-1.0.15/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/itoap-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/6361d03d8dd1d25985f93efb8b07ec973a7258d0 || :
cp %{_builddir}/orjson-%{version}/include/cargo/jiff-0.2.5/COPYING %{buildroot}/usr/share/package-licenses/pypi-orjson/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/orjson-%{version}/include/cargo/jiff-0.2.5/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/orjson-%{version}/include/cargo/jiff-0.2.5/UNLICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/orjson-%{version}/include/cargo/jiff-static-0.2.5/COPYING %{buildroot}/usr/share/package-licenses/pypi-orjson/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/orjson-%{version}/include/cargo/jiff-static-0.2.5/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/orjson-%{version}/include/cargo/jiff-static-0.2.5/UNLICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/orjson-%{version}/include/cargo/libc-0.2.171/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/libc-0.2.171/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/orjson-%{version}/include/cargo/memchr-2.7.4/COPYING %{buildroot}/usr/share/package-licenses/pypi-orjson/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/orjson-%{version}/include/cargo/memchr-2.7.4/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/orjson-%{version}/include/cargo/memchr-2.7.4/UNLICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/orjson-%{version}/include/cargo/once_cell-1.21.1/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/include/cargo/once_cell-1.21.1/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/portable-atomic-1.11.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/orjson-%{version}/include/cargo/portable-atomic-1.11.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/portable-atomic-util-0.2.4/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/orjson-%{version}/include/cargo/portable-atomic-util-0.2.4/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/proc-macro2-1.0.94/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/proc-macro2-1.0.94/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/quote-1.0.40/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/quote-1.0.40/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/rustversion-1.0.20/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/rustversion-1.0.20/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/ryu-1.0.20/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/ryu-1.0.20/LICENSE-BOOST %{buildroot}/usr/share/package-licenses/pypi-orjson/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/orjson-%{version}/include/cargo/serde-1.0.219/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/serde-1.0.219/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/serde_derive-1.0.219/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/serde_derive-1.0.219/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/serde_json-1.0.140/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/serde_json-1.0.140/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/shlex-1.3.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/a97a2888bca904918b3b9ec008fde1d6e9905a6d || :
cp %{_builddir}/orjson-%{version}/include/cargo/shlex-1.3.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/64e8197cb5ae680fcf996cc0ac8760e9f1e2e3a6 || :
cp %{_builddir}/orjson-%{version}/include/cargo/simdutf8-0.1.5/LICENSE-Apache %{buildroot}/usr/share/package-licenses/pypi-orjson/736872921ab5596e857b333eb7854a53212dbab1 || :
cp %{_builddir}/orjson-%{version}/include/cargo/simdutf8-0.1.5/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/4436a9ca3f5b79c93630c2feeda4c6b498839596 || :
cp %{_builddir}/orjson-%{version}/include/cargo/smallvec-1.14.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/include/cargo/smallvec-1.14.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/c61640f6c218caf86d1b8072e09668a8362dba04 || :
cp %{_builddir}/orjson-%{version}/include/cargo/static_assertions-1.1.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/orjson-%{version}/include/cargo/static_assertions-1.1.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/972723ef8f594b1c7515e4c227ff9d5912041fac || :
cp %{_builddir}/orjson-%{version}/include/cargo/syn-2.0.100/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/syn-2.0.100/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/target-lexicon-0.13.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/unicode-ident-1.0.18/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/unicode-ident-1.0.18/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/unwinding-0.2.5/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/orjson-%{version}/include/cargo/unwinding-0.2.5/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/orjson-%{version}/include/cargo/uuid-1.16.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/include/cargo/uuid-1.16.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/459ceba57b368122a3cb1fd48edea59d1363cad7 || :
cp %{_builddir}/orjson-%{version}/include/cargo/version_check-0.9.5/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/orjson-%{version}/include/cargo/version_check-0.9.5/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/cfcb552ef0afbe7ccb4128891c0de00685988a4b || :
cp %{_builddir}/orjson-%{version}/include/cargo/xxhash-rust-0.8.15/LICENSE %{buildroot}/usr/share/package-licenses/pypi-orjson/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/orjson-%{version}/include/pyo3/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/orjson-%{version}/include/pyo3/pyo3-build-config/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/orjson-%{version}/include/pyo3/pyo3-ffi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-orjson/959ce149b1615b8bff3437f59282396756987859 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-orjson/1e35cd39af07e5460de3011d5ef8f6a775ee54ae
/usr/share/package-licenses/pypi-orjson/218fc8c15534e8840cbff5801582c450c97869ab
/usr/share/package-licenses/pypi-orjson/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-orjson/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-orjson/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-orjson/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/pypi-orjson/4436a9ca3f5b79c93630c2feeda4c6b498839596
/usr/share/package-licenses/pypi-orjson/459ceba57b368122a3cb1fd48edea59d1363cad7
/usr/share/package-licenses/pypi-orjson/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/pypi-orjson/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-orjson/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-orjson/5c59637187123fdaf921408bc38718e196e5ee9a
/usr/share/package-licenses/pypi-orjson/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/pypi-orjson/6361d03d8dd1d25985f93efb8b07ec973a7258d0
/usr/share/package-licenses/pypi-orjson/64e8197cb5ae680fcf996cc0ac8760e9f1e2e3a6
/usr/share/package-licenses/pypi-orjson/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-orjson/736872921ab5596e857b333eb7854a53212dbab1
/usr/share/package-licenses/pypi-orjson/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/pypi-orjson/959ce149b1615b8bff3437f59282396756987859
/usr/share/package-licenses/pypi-orjson/972723ef8f594b1c7515e4c227ff9d5912041fac
/usr/share/package-licenses/pypi-orjson/9ec2af04328d0eb6ec89ca6d75156ffc7aecf869
/usr/share/package-licenses/pypi-orjson/a6a5418b4d67d9f3a33cbf184b25ac7f9fa87d33
/usr/share/package-licenses/pypi-orjson/a97a2888bca904918b3b9ec008fde1d6e9905a6d
/usr/share/package-licenses/pypi-orjson/b4872d72eb3ccfa74730cc229184eec04f303e7d
/usr/share/package-licenses/pypi-orjson/c61640f6c218caf86d1b8072e09668a8362dba04
/usr/share/package-licenses/pypi-orjson/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-orjson/cfcb552ef0afbe7ccb4128891c0de00685988a4b
/usr/share/package-licenses/pypi-orjson/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/pypi-orjson/ef9d72cbd46e61ffd8d8a6f906ff553eb5f6233c
/usr/share/package-licenses/pypi-orjson/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/pypi-orjson/fd33e0d46674b32eb66a5f1134e8d8a2d2f684c9
/usr/share/package-licenses/pypi-orjson/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
