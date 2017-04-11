Name:           ros-lunar-robot-model
Version:        1.12.8
Release:        2%{?dist}
Summary:        ROS robot_model package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_model
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-collada-parser
Requires:       ros-lunar-collada-urdf
Requires:       ros-lunar-joint-state-publisher
Requires:       ros-lunar-kdl-parser
Requires:       ros-lunar-resource-retriever
Requires:       ros-lunar-urdf
Requires:       ros-lunar-urdf-parser-plugin
Requires:       urdfdom
BuildRequires:  ros-lunar-catkin

%description
robot_model contains packages for modeling various aspects of robot information,
specified in the Xml Robot Description Format (URDF). The core package of this
stack is urdf, which parses URDF files, and constructs an object model (C++) of
the robot.

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
* Tue Apr 11 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-2
- Autogenerated by Bloom

* Mon Apr 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-1
- Autogenerated by Bloom

* Mon Apr 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-0
- Autogenerated by Bloom

