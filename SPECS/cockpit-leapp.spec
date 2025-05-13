Name:           cockpit-leapp
Version:        0.1.7
Release:        2%{?dist}
Summary:        Leapp in-place upgrade Cockpit UI

License:        LGPLv2+
URL:            https://github.com/oamg/cockpit-leapp
Source0:        cockpit-leapp-%{version}.tar.gz

BuildArch:      noarch

Requires:       cockpit

#TODO: require just leapp-upgrade rpm for now as we probably want to upgrade
# cockpit-leapp package from RHEL 7 during IPU 7 -> 8. however, other leapp
# related packages must not be touched during the upgrade. Possibly we will
# need a change in the cockpit-leapp code. For now we are going this way
# to enable testing possibilities.
Requires:       leapp-upgrade

%description
Leapp in-place upgrade Cockpit UI

%prep
%setup -q -n cockpit-leapp-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/cockpit/leapp
cp -r public/* %{buildroot}/%{_datadir}/cockpit/leapp

%files
%license LICENSE.txt
%{_datadir}/cockpit/leapp

%post
touch %{_localstatedir}/log/leapp/remediations


%changelog
* Tue Sep 10 2024 Bob Mader <bob@redhat.com> - 0.1.7-2
- Initial build for EL9
- Applying changes for gating - adding the .fmf directory
- Resolves: RHEL-57044
