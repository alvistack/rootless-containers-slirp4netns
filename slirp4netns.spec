# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: slirp4netns
Epoch: 100
Version: 1.3.0
Release: 1%{?dist}
Summary: User-mode networking for unprivileged network namespaces
License: GPL-2.0-only
URL: https://github.com/rootless-containers/slirp4netns/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: libslirp-devel
BuildRequires: libtool
BuildRequires: pkgconfig
Requires: libcap.so.2()(64bit)
Requires: libglib-2.0.so.0()(64bit)
Requires: libseccomp.so.2()(64bit)
Requires: libslirp.so.0()(64bit)

%description
slirp4netns provides user-mode networking ("slirp") for unprivileged
network namespaces.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
autoreconf -i
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/*
rm -rf %{buildroot}/%{_mandir}/man1/*

%files
%license COPYING
%{_bindir}/slirp4netns

%changelog
