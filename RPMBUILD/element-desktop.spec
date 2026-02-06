%global debug_package %{nil}
%define _build_id_links none

Name:           element-desktop
Version:        1.12.9
Release:        1%{?dist}
Summary:        Element is a Matrix-based end-to-end encrypted messenger and secure collaboration app

License:        GPL-3.0-only
URL:            https://element.io
Source0:        https://packages.element.io/desktop/install/linux/glibc-x86-64/element-desktop-%{version}.tar.gz
Source1:        https://github.com/AliKarahanci/element-desktop-rpm/raw/main/src/element-desktop-share.tar.gz

BuildArch:      x86_64
AutoReqProv:    no
%global __strip /bin/true

%description
Element is a Matrix-based end-to-end encrypted messenger and secure collaboration app

%prep
%setup -q -n element-desktop-%{version}
%setup -q -T -D -a 1

%build
# nothing to build

%install
rm -rf %{buildroot}

# binary
mkdir -p %{buildroot}/opt/Element
cp -a * %{buildroot}/opt/Element/

# launcher
mkdir -p %{buildroot}/usr/bin
ln -s /opt/Element/element-desktop %{buildroot}/usr/bin/element-desktop

# share contents (applications, icons, doc)
mkdir -p %{buildroot}/usr/share
cp -a applications icons doc %{buildroot}/usr/share/

%files
/usr/bin/element-desktop
/opt/Element
/usr/share/applications
/usr/share/icons
/usr/share/doc

%changelog
* Fri Feb 06 2026 Ali <karahanciali@hotmail.com> - 1.12.9-1
- Initial RPM build
