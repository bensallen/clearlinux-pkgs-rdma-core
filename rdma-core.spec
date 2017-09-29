#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rdma-core
Version  : 15
Release  : 7
URL      : https://github.com/linux-rdma/rdma-core/releases/download/v15/rdma-core-15.tar.gz
Source0  : https://github.com/linux-rdma/rdma-core/releases/download/v15/rdma-core-15.tar.gz
Summary  : RDMA core userspace libraries and daemons
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 MIT
Requires: rdma-core-bin
Requires: rdma-core-config
Requires: rdma-core-lib
Requires: rdma-core-data
Requires: rdma-core-doc
BuildRequires : cmake
BuildRequires : libnl-dev
BuildRequires : python

%description
RDMA core userspace infrastructure and documentation, including initialization
scripts, kernel driver-specific modprobe override configs, IPoIB network
scripts, dracut rules, and the rdma-ndd utility.

%package bin
Summary: bin components for the rdma-core package.
Group: Binaries
Requires: rdma-core-data
Requires: rdma-core-config

%description bin
bin components for the rdma-core package.


%package config
Summary: config components for the rdma-core package.
Group: Default

%description config
config components for the rdma-core package.


%package data
Summary: data components for the rdma-core package.
Group: Data

%description data
data components for the rdma-core package.


%package dev
Summary: dev components for the rdma-core package.
Group: Development
Requires: rdma-core-lib
Requires: rdma-core-bin
Requires: rdma-core-data
Provides: rdma-core-devel

%description dev
dev components for the rdma-core package.


%package doc
Summary: doc components for the rdma-core package.
Group: Documentation

%description doc
doc components for the rdma-core package.


%package lib
Summary: lib components for the rdma-core package.
Group: Libraries
Requires: rdma-core-data
Requires: rdma-core-config

%description lib
lib components for the rdma-core package.


%prep
%setup -q -n rdma-core-15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506721489
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DCMAKE_INSTALL_SYSCONFDIR=/usr/share/defaults/rdma-core
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1506721489
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/libexec/truescale-serdes.cmds
/usr/bin/cmtime
/usr/bin/ib_acme
/usr/bin/ibacm
/usr/bin/ibsrpdm
/usr/bin/ibv_asyncwatch
/usr/bin/ibv_devices
/usr/bin/ibv_devinfo
/usr/bin/ibv_rc_pingpong
/usr/bin/ibv_srq_pingpong
/usr/bin/ibv_uc_pingpong
/usr/bin/ibv_ud_pingpong
/usr/bin/ibv_xsrq_pingpong
/usr/bin/iwpmd
/usr/bin/mckey
/usr/bin/rcopy
/usr/bin/rdma_client
/usr/bin/rdma_server
/usr/bin/rdma_xclient
/usr/bin/rdma_xserver
/usr/bin/riostream
/usr/bin/rping
/usr/bin/rstream
/usr/bin/run_srp_daemon
/usr/bin/rxe_cfg
/usr/bin/srp_daemon
/usr/bin/srp_daemon.sh
/usr/bin/ucmatose
/usr/bin/udaddy
/usr/bin/udpong
/usr/libexec/srp_daemon/start_on_all_ports

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ibacm.service
/usr/lib/systemd/system/ibacm.socket
/usr/lib/systemd/system/iwpmd.service
/usr/lib/systemd/system/rdma-hw.target
/usr/lib/systemd/system/rdma-load-modules@.service
/usr/lib/systemd/system/srp_daemon.service
/usr/lib/systemd/system/srp_daemon_port@.service
/usr/lib/udev/rules.d/60-srp_daemon.rules
/usr/lib/udev/rules.d/75-rdma-description.rules
/usr/lib/udev/rules.d/90-iwpmd.rules
/usr/lib/udev/rules.d/90-rdma-hw-modules.rules
/usr/lib/udev/rules.d/90-rdma-ulp-modules.rules
/usr/lib/udev/rules.d/90-rdma-umad.rules

%files data
%defattr(-,root,root,-)
%exclude /usr/share/defaults/rdma-core/init.d/ibacm
%exclude /usr/share/defaults/rdma-core/init.d/iwpmd
%exclude /usr/share/defaults/rdma-core/init.d/srpd
%exclude /usr/share/defaults/rdma-core/modprobe.d/mlx4.conf
%exclude /usr/share/defaults/rdma-core/modprobe.d/truescale.conf
%exclude /usr/share/defaults/rdma-core/srp_daemon.conf
%exclude /usr/share/defaults/rdma-core/udev/rules.d/70-persistent-ipoib.rules
/usr/share/defaults/rdma-core/iwpmd.conf
/usr/share/defaults/rdma-core/libibverbs.d/bnxt_re.driver
/usr/share/defaults/rdma-core/libibverbs.d/cxgb3.driver
/usr/share/defaults/rdma-core/libibverbs.d/cxgb4.driver
/usr/share/defaults/rdma-core/libibverbs.d/hfi1verbs.driver
/usr/share/defaults/rdma-core/libibverbs.d/hns.driver
/usr/share/defaults/rdma-core/libibverbs.d/i40iw.driver
/usr/share/defaults/rdma-core/libibverbs.d/ipathverbs.driver
/usr/share/defaults/rdma-core/libibverbs.d/mlx4.driver
/usr/share/defaults/rdma-core/libibverbs.d/mlx5.driver
/usr/share/defaults/rdma-core/libibverbs.d/mthca.driver
/usr/share/defaults/rdma-core/libibverbs.d/nes.driver
/usr/share/defaults/rdma-core/libibverbs.d/ocrdma.driver
/usr/share/defaults/rdma-core/libibverbs.d/qedr.driver
/usr/share/defaults/rdma-core/libibverbs.d/rxe.driver
/usr/share/defaults/rdma-core/libibverbs.d/vmw_pvrdma.driver
/usr/share/defaults/rdma-core/rdma/modules/infiniband.conf
/usr/share/defaults/rdma-core/rdma/modules/iwarp.conf
/usr/share/defaults/rdma-core/rdma/modules/iwpmd.conf
/usr/share/defaults/rdma-core/rdma/modules/opa.conf
/usr/share/defaults/rdma-core/rdma/modules/rdma.conf
/usr/share/defaults/rdma-core/rdma/modules/roce.conf
/usr/share/defaults/rdma-core/rdma/modules/srp_daemon.conf

%files dev
%defattr(-,root,root,-)
/usr/include/infiniband/acm.h
/usr/include/infiniband/acm_prov.h
/usr/include/infiniband/arch.h
/usr/include/infiniband/cm.h
/usr/include/infiniband/cm_abi.h
/usr/include/infiniband/ib.h
/usr/include/infiniband/kern-abi.h
/usr/include/infiniband/mlx4dv.h
/usr/include/infiniband/mlx5dv.h
/usr/include/infiniband/opcode.h
/usr/include/infiniband/sa-kern-abi.h
/usr/include/infiniband/sa.h
/usr/include/infiniband/umad.h
/usr/include/infiniband/umad_cm.h
/usr/include/infiniband/umad_sa.h
/usr/include/infiniband/umad_sm.h
/usr/include/infiniband/umad_str.h
/usr/include/infiniband/umad_types.h
/usr/include/infiniband/verbs.h
/usr/include/rdma/rdma_cma.h
/usr/include/rdma/rdma_cma_abi.h
/usr/include/rdma/rdma_verbs.h
/usr/include/rdma/rsocket.h
/usr/lib64/libibcm.so
/usr/lib64/libibumad.so
/usr/lib64/libibverbs.so
/usr/lib64/libmlx4.so
/usr/lib64/libmlx5.so
/usr/lib64/librdmacm.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/rdma\-core/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/ibacm/libibacmp.so
/usr/lib64/libibcm.so.1
/usr/lib64/libibcm.so.1.0.15
/usr/lib64/libibumad.so.3
/usr/lib64/libibumad.so.3.0.15
/usr/lib64/libibverbs.so.1
/usr/lib64/libibverbs.so.1.1.15
/usr/lib64/libibverbs/libbnxt_re-rdmav15.so
/usr/lib64/libibverbs/libcxgb3-rdmav15.so
/usr/lib64/libibverbs/libcxgb4-rdmav15.so
/usr/lib64/libibverbs/libhfi1verbs-rdmav15.so
/usr/lib64/libibverbs/libhns-rdmav15.so
/usr/lib64/libibverbs/libi40iw-rdmav15.so
/usr/lib64/libibverbs/libipathverbs-rdmav15.so
/usr/lib64/libibverbs/libmlx4-rdmav15.so
/usr/lib64/libibverbs/libmlx5-rdmav15.so
/usr/lib64/libibverbs/libmthca-rdmav15.so
/usr/lib64/libibverbs/libnes-rdmav15.so
/usr/lib64/libibverbs/libocrdma-rdmav15.so
/usr/lib64/libibverbs/libqedr-rdmav15.so
/usr/lib64/libibverbs/librxe-rdmav15.so
/usr/lib64/libibverbs/libvmw_pvrdma-rdmav15.so
/usr/lib64/libmlx4.so.1
/usr/lib64/libmlx4.so.1.0.15
/usr/lib64/libmlx5.so.1
/usr/lib64/libmlx5.so.1.2.15
/usr/lib64/librdmacm.so.1
/usr/lib64/librdmacm.so.1.0.15
/usr/lib64/rsocket/librspreload.so
/usr/lib64/rsocket/librspreload.so.1
/usr/lib64/rsocket/librspreload.so.1.0.0
