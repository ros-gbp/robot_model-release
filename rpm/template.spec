Name:           ros-indigo-urdf
Version:        1.11.11
Release:        0%{?dist}
Summary:        ROS urdf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/urdf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-rosconsole-bridge
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-urdf-parser-plugin
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-rosconsole-bridge
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-urdf-parser-plugin
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel

%description
This package contains a C++ parser for the Unified Robot Description Format
(URDF), which is an XML format for representing a robot model. The code API of
the parser has been through our review process and will remain backwards
compatible in future releases.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jun 10 2016 Ioan Sucan <isucan@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

* Tue Feb 23 2016 Ioan Sucan <isucan@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

* Mon Feb 22 2016 Ioan Sucan <isucan@gmail.com> - 1.11.9-0
- Autogenerated by Bloom

* Fri Sep 11 2015 Ioan Sucan <isucan@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

* Wed Apr 22 2015 Ioan Sucan <isucan@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

