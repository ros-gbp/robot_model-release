Name:           ros-lunar-urdf-parser-plugin
Version:        1.12.10
Release:        1%{?dist}
Summary:        ROS urdf_parser_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/urdf
Source0:        %{name}-%{version}.tar.gz

Requires:       urdfdom-headers-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  urdfdom-headers-devel

%description
This package contains a C++ base class for URDF parsers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Jun 26 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.10-1
- Autogenerated by Bloom

* Sun Jun 25 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.10-0
- Autogenerated by Bloom

* Wed Apr 26 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.9-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-2
- Autogenerated by Bloom

* Mon Apr 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-1
- Autogenerated by Bloom

* Mon Apr 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-0
- Autogenerated by Bloom

