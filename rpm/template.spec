Name:           ros-kinetic-joint-state-publisher
Version:        1.12.2
Release:        0%{?dist}
Summary:        ROS joint_state_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/joint_state_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-python-qt-binding
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-python-qt-binding
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-sensor-msgs

%description
This package contains a tool for setting and publishing joint state values for a
given URDF.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Apr 12 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.2-0
- Autogenerated by Bloom

* Mon Apr 11 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-3
- Autogenerated by Bloom

* Mon Apr 11 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-2
- Autogenerated by Bloom

* Sun Apr 10 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-1
- Autogenerated by Bloom

* Sun Apr 10 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Mon Apr 04 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

* Mon Apr 04 2016 David V. Lu!! <davidvlu@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

