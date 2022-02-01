#
# Spec file for package levuaska-gtk-theme
#
# Copyright (c) 2016 Sam Hewitt
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name:           levuaska-gtk-theme
Version:        1.0
Release:        0
License:        GPL-3.0+
Summary:        Levuaska GTK theme
Url:            https://github.com/saimoomedits/levuaska
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.xz
BuildRequires:  automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       gtk2-engines

%description
Levuaska is a flat, dark theme based on modern design. Inspired by the Fleon gtk theme by Owl4ce.

%prep
%setup -q
chmod +x autogen.sh
chmod a-x AUTHORS README.md

%build
./autogen.sh
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
rm -f %{buildroot}%{_datadir}/themes/Levuaska/AUTHORS

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%{_datadir}/themes/Levuaska
