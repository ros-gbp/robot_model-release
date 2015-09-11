Name:           ros-indigo-joint-state-publisher
Version:        1.11.8
Release:        0%{?dist}
Summary:        ROS joint_state_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/joint_state_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       wxPython-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  wxPython-devel

%description
This package contains a tool for setting and publishing joint state values for a
given URDF.

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
* Fri Sep 11 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

* Wed Apr 22 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

