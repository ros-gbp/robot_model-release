Name:           ros-jade-robot-model
Version:        1.11.11
Release:        0%{?dist}
Summary:        ROS robot_model package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_model
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-collada-parser
Requires:       ros-jade-collada-urdf
Requires:       ros-jade-joint-state-publisher
Requires:       ros-jade-kdl-parser
Requires:       ros-jade-resource-retriever
Requires:       ros-jade-urdf
Requires:       ros-jade-urdf-parser-plugin
Requires:       urdfdom
BuildRequires:  ros-jade-catkin

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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

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

