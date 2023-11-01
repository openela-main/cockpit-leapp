Name:           cockpit-leapp
Version:        0.1.6
Release:        5%{?dist}
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
* Thu Mar 20 2022 Petr Stodulka <pstodulk@redhat.com> - 0.1.6-5
- Rebuild
- Resolves: #2037743

* Tue Jan 25 2022 Petr Stodulka <pstodulk@redhat.com> - 0.1.6-3
- Updated dependencies to make possible the upgrade of the package
  during IPU 7 -> 8
- Resolves: #2037743

* Wed Oct 27 2021 Petr Stodulka <pstodulk@redhat.com> - 0.1.6-2
- Updated dependencies regarding rename of binary packages
  in leapp-repository
  Resolves: #2017115

* Mon Oct 25 2021 Dominik Rehak <drehak@redhat.com> - 0.1.6-1
- Update to 0.1.6
- Fix showing report entries with unknown resource types
  Resolves: #2017115

* Thu Oct 22 2020 Dominik Rehak <drehak@redhat.com> - 0.1.5-1
- Update to 0.1.5
- Fix execution of remediations and error redirect
  Resolves: #1890682

* Thu Sep 17 2020 Dominik Rehak <drehak@redhat.com> - 0.1.4-1
- Update to 0.1.4
- Require superuser in all file/process API calls
  Resolves: #1859779

* Wed Sep 09 2020 Dominik Rehak <drehak@redhat.com> - 0.1.3-1
- Update to 0.1.3
- Fix running remediation commands
  Resolves: #1877313
- Fix showing report when not logged in as superuser
  Resolves: #1859779

* Wed Sep 02 2020 Dominik Rehak <drehak@redhat.com> - 0.1.2-1
- Update to 0.1.2
- Fix showing remediations when leapp is killed
  Resolves: #1873184
- Add support of dialog related report entries
  Resolves: #1873608

* Tue Nov 26 2019 Petr Stodulka <pstodulk@redhat.com> - 0.1.1-1
- Update to 0.1.1
- Fix crash issues due to invalid severity in report
  Resolves: #1776938

* Fri Nov 01 2019 Michal Reznik <mreznik@redhat.com> - 0.1.0-5
- Add "back" button to "Remediation Plan"

* Wed Oct 30 2019 Michal Reznik <mreznik@redhat.com> - 0.1.0-4
- Add "remediations" file to /var/log/leapp
