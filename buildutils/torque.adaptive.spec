# since this spec file is 'pristine' (not requiring the use of configure, etc),
# it uses macros defined by the user to build correctly.
# Example of suggested build command:
#   rpmbuild -ba --define "version 4.2.0" --define "release_number 48"

%{!?version:%{error:%%version not defined.}}
%{!?release_number:%{error:%%release_number not defined.}}

# This is the name of the tarball of the source code. If not set,
# the default <name>-<version> tarball is used from the web site.
%{!?source_file:%{warn:%%source_file not defined.}}

# This is the name of the directory contained in the tarball.
# If it is not set, the default <name>-<version> directory name is used.
%{!?base_name:%{warn:%%base_name not defined.}}

%ifarch x86_64 amd64
%define _lib lib64
%endif

# To be able to distinguish between AC's and the community RPMs, and also to
# provide interoperability, we prefix the names of all the torque packages with
# 'moab'.
%define name_prefix     moab
%define project_name    torque
%define name        %{name_prefix}-%{project_name}

# These are the names of subpackages, of the form %%{name}-<subpackage> .
%define client_sub  client
%define common_sub  common
%define mom_sub     mom
%define server_sub  server
%define devel_sub   devel

%define community_top_pkg       %{project_name}
%define community_client_pkg    %{project_name}
%define community_mom_pkg       %{project_name}-client
%define community_server_pkg    %{project_name}-server
%define community_devel_pkg     %{project_name}-devel

%define common_pkg      %{name}-%{common_sub}
%define client_pkg      %{name}-%{client_sub}
%define server_pkg      %{name}-%{server_sub}
%define mom_pkg         %{name}-%{mom_sub}
%define devel_pkg       %{name}-%{devel_sub}

# End Autoconf variables #######################################################

# Nice error message if some macro is undefined.
%define macro_undefined_error() \
    %{error:%{?1:%%%{1}}%{!?1:macro} is not defined.}

### Features disabled by default
%bcond_with    blcr
%bcond_with    cpuset
%bcond_with    libcpuset
%bcond_with    memacct
%bcond_with    munge
%bcond_with    numa
%bcond_with    pam
%bcond_with    top

### Features enabled by default
%bcond_without scp
%bcond_without spool
%bcond_without syslog

### Autoconf macro expansions
%define ac_with_blcr       --%{?with_blcr:en}%{!?with_blcr:dis}able-blcr
%define ac_with_cpuset     --%{?with_cpuset:en}%{!?with_cpuset:dis}able-cpuset
%define ac_with_drmaa      --%{?with_drmaa:en}%{!?with_drmaa:dis}able-drmaa
%define ac_with_munge      --%{?with_munge:en}%{!?with_munge:dis}able-munge-auth
%define ac_with_numa       --%{?with_numa:en}%{!?with_numa:dis}able-numa-support
%define ac_with_memacct    --%{?with_memacct:en}%{!?with_memacct:dis}able-memacct
%define ac_with_libcpuset  --%{?with_libcpuset:en}%{!?with_libcpuset:dis}able-libcpuset
%define ac_with_top        --%{?with_top:en}%{!?with_top:dis}able-top-tempdir-only
%define ac_with_pam        --with%{!?with_pam:out}-pam%{?with_pam:=/%{_lib}/security}
%define ac_with_scp        --with-rcp=%{?with_scp:scp}%{!?with_scp:pbs_rcp}
%define ac_with_spool      --%{?with_spool:en}%{!?with_spool:dis}able-spool
%define ac_with_syslog     --%{?with_syslog:en}%{!?with_syslog:dis}able-syslog

### Build Requirements
%define breq_munge %{?with_munge:munge-devel}
%define breq_pam   %{?with_pam:pam-devel}
%define breq_scp   %{?with_scp:/usr/bin/scp}

# Missing:
# libcpuset -> libcpuset.so.*
# numa: hwloc.so.*
# cpuset: hwloc.so.*
# memacct: memacct.so.*

### Macro variables
%{!?torque_user:%global torque_user root}
%{!?torque_home:%global torque_home %{_var}/spool/%{project_name}}
%{!?sendmail_path:%global sendmail_path %{_sbindir}/sendmail}

# This ensures that the debugging symbols are not stripped
%define __os_install_post /usr/lib/rpm/brp-compress

# Additional autoconf variables
# Set according to the standard found here:
# http://www.gnu.org/prep/standards/html_node/Directory-Variables.html
%define _appstatedir            %{_localstatedir}/lib
%define _logdir                 %{_localstatedir}/log
%define _spooldir               %{_localstatedir}/spool
%define _initrddir              /etc/init.d

%define torque_sysconfdir       %{torque_home}
%define torque_appstatedir      %{torque_home}
%define torque_logdir           %{torque_home}
%define torque_spooldir         %{torque_home}

%define pkg_doc_dir             %{_docdir}/%{name}-%{version}
# These macros allow for easy searching and replacing of unwanted strings.
%define grep_safety_net_error \
    %{error:Usage: grep_safety_net <directory> <search-str> <repl-str>}

%define grep_safety_net() \
    %{!?1:%grep_safety_net_error} \
    %{!?2:%grep_safety_net_error} \
    %{!?3:%grep_safety_net_error} \
    for i in `%{__grep} -H -r -l -I %{?4} "%{2}" "%{1}"`; \
    do \
       %{__sed} -i "s|%{2}|%{3}|g" $i; \
    done
# These allow the automatic back up to take place.

%define pre_clear_back_up() \
    echo "  Removing files looking like " \
    echo "    '/var/tmp/backup-%{name}%{?1:-%{1}}.*\\.tar'..." \
    ls -1A /var/tmp | \
        grep 'backup-%{name}%{?1:-%{1}}.*\\.tar' | \
        xargs rm -f >/dev/null 2>&1 || :

%define pre_add_back_up_dir() \
    if [ -d "%{1}" ] \
    then \
        echo "  Adding '%{1}' to the back-up tar file" \
        echo "    '/var/tmp/backup-%{name}%{?2:-%{2}}.tar'..." \
        tar uf "/var/tmp/backup-%{name}%{?2:-%{2}}.tar" "%{1}" \
    fi

%define pre_add_back_up_file() \
    if [ -d "%{1}" ] \
    then \
        echo "  Adding '%{1}' to the back-up tar file" \
        echo "    '/var/tmp/backup-%{name}%{?2:-%{2}}.tar'..." \
        tar uf "/var/tmp/backup-%{name}%{?2:-%{2}}.tar" "%{1}" \
    fi

%define pre_zip_back_up() \
    if [ -s "/var/tmp/backup-%{name}%{?1:-%{1}}.tar" ] \
    then \
        echo "  gzipping the file " \
        echo "    '/var/tmp/backup-%{name}%{?1:-%{1}}.tar'..." \
        gzip "/var/tmp/backup-%{name}%{?1:-%{1}}.tar" \
    fi

Name:           %{name}
Version:        %{version}
Release:        %{release_number}
Summary:        Tera-scale Open-source Resource and QUEue manager
License:        OpenPBS License (ASF-like)
URL:            http://www.adaptivecomputing.com/products/open-source/torque/
Group:          Applications/System
Packager:       %{?_packager:%{_packager}}%{!?_packager:%{_vendor}}
Distribution:   %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
BuildRequires:  %{breq_munge} %{breq_pam} %{breq_scp} make
Source:         %{?source_file}%{!?source_file:"http://www.adaptivecomputing.com/resources/downloads/%{project_name}/%{project_name}-%{version}.tar.gz"}
Vendor:         %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:%{_vendor}}

%description
TORQUE is an open source resource manager providing control over batch
jobs and distributed compute nodes. It is a community effort based on
the original *PBS project and has incorporated significant advances in the
areas of scalability, fault tolerance, and feature extensions contributed by
NCSA, OSC, USC, the U.S. Dept of Energy, Sandia, PNNL, U of Buffalo, TeraGrid,
and many other leading edge HPC organizations.

This edition of the TORQUE has been packaged specifically for the MOAB HPC
Suite.

%package    %{common_sub}
Group:      Applications/System
Summary:    TORQUE Common Files

%description %{common_sub}
Common files shared by TORQUE Server, Client, and MOM packages

%package    %{client_sub}
Summary:    TORQUE Client
Group:      Applications/System
Conflicts:  pbspro, openpbs, openpbs-oscar
Obsoletes:  scatorque <= %{version}-%{release}
Provides:   pbs, pbs-docs %{?with_pam:, pbs-pam}
Provides:   %{community_client_pkg} = %{version}-%{release}
Obsoletes:  %{community_client_pkg} < %{version}-%{release}
%ifarch x86_64 amd64
Provides:   %{community_client_pkg}(x86-64) = %{version}-%{release}
Obsoletes:  %{community_client_pkg}(x86-64) < %{version}-%{release}
%endif
Provides:   %{community_top_pkg}-docs = %{version}-%{release}
Obsoletes:  %{community_top_pkg}-docs < %{version}-%{release}
Requires:   %{common_pkg}

%description %{client_sub}
TORQUE Client provides the client utilities necessary for interacting with
TORQUE Server.

%package    %{server_sub}
Summary:    TORQUE Server
Group:      System Environment/Daemons
Provides:   pbs-server = %{version}-%{release}
Provides:   %{community_server_pkg} = %{version}-%{release}
Obsoletes:  %{community_server_pkg} < %{version}-%{release}
%ifarch x86_64 amd64
Provides:   %{community_server_pkg}(x86-64) = %{version}-%{release}
Obsoletes:  %{community_server_pkg}(x86-64) < %{version}-%{release}
%endif
Requires:   %{common_pkg}
Requires:   %{client_pkg}

%description %{server_sub}
TORQUE Resource Manager provides control over batch jobs and distributed
computing resources. It is an advanced open-source product based on the
original PBS project* and incorporates the best of both community and
professional development.

%package    %{devel_sub}
Summary:    TORQUE Development Files
Group:      Applications/System
Requires:   %{client_pkg} = %{version}-%{release}
Provides:   pbs-devel = %{version}-%{release}
Provides:   lib%{project_name}-devel = %{version}-%{release}
Provides:   %{community_devel_pkg} = %{version}-%{release}
Obsoletes:  %{community_devel_pkg} < %{version}-%{release}
%ifarch x86_64 amd64
Provides:   %{community_devel_pkg}(x86-64) = %{version}-%{release}
Obsoletes:  %{community_devel_pkg}(x86-64) < %{version}-%{release}
%endif

%description %{devel_sub}
Development headers and libraries for TORQUE

%package %{mom_sub}
Summary: TORQUE MOM agent
Group: Applications/System
Provides: pbs-client pbs-mom %{?with_pam:pbs-pam}
%if %{with pam}
Provides: %{community_top_pkg}-pam = %{version}-%{release}
Obsoletes: %{community_top_pkg}-pam < %{version}-%{release}
Provides: %{community_top_pkg}-pam = %{version}-%{release}
Obsoletes: %{community_top_pkg}-pam < %{version}-%{release}
%endif
Requires:   %{common_pkg}
Provides:   %{community_mom_pkg} = %{version}-%{release}
Obsoletes:  %{community_mom_pkg} < %{version}-%{release}
%ifarch x86_64 amd64
Provides:   %{community_mom_pkg}(x86-64) = %{version}-%{release}
Obsoletes:  %{community_mom_pkg}(x86-64) < %{version}-%{release}
%endif

%description %{mom_sub}
TORQUE MOM provides the agent necessary for each compute node in a
TORQUE-managed batch system.

%prep
%setup %{?base_name:-n %{base_name}}

%build

# 0 optimization for full-on debugging.
CFLAGS="-g3 -O0"
CXXFLAGS="-g3 -O0"

%configure  --includedir=%{_includedir}/%{project_name} \
            --with-server-home=%{torque_home} \
            --with-sendmail=%{sendmail_path} \
            --disable-dependency-tracking \
            --disable-gcc-warnings \
            --disable-qsub-keep-override \
            --with-debug \
            %{ac_with_scp} %{ac_with_syslog} \
            %{ac_with_munge} %{ac_with_pam} \
            %{ac_with_blcr} %{ac_with_cpuset} %{ac_with_spool} %{?acflags}
%{__make} clean
%{__make} %{?_smp_mflags} %{?mflags}

%install
%{__install} -d %{buildroot}%{torque_appstatedir}/server_priv
%{__install} -d %{buildroot}%{torque_logdir}
%{__install} -d %{buildroot}%{torque_spooldir}
%{__install} -d %{buildroot}%{torque_sysconfdir}


%{make_install} \
    sysconfdir=%{torque_sysconfdir} \
    appstatedir=%{torque_appstatedir} \
    logdir=%{torque_logdir} \
    spooldir=%{torque_spooldir} \
     %{?mflags_install}

%{__rm} -rf %{buildroot}/%{_lib}/security/*a \
    %{buildroot}%{_sysconfdir}/modulefiles

# init.d scripts
%{__mkdir_p} %{buildroot}%{_initrddir}
INIT_PREFIX=""

for PROG in pbs_mom pbs_sched pbs_server trqauthd
do
    %{__sed} -e 's|^PBS_HOME=.*|PBS_HOME=%{torque_appstatedir}|' \
             -e 's|^SYSCONF_PATH=.*|SYSCONF_PATH=%{torque_sysconfdir}|' \
             -e 's|^APPSTATE_PATH=.*|APPSTATE_PATH=%{torque_appstatedir}|' \
             -e 's|^LOG_PATH=.*|LOG_PATH=%{torque_logdir}|' \
             -e 's|^SPOOL_PATH=.*|SPOOL_PATH=%{torque_spooldir}|' \
             -e 's|^BIN_PATH=.*|BIN_PATH=%{_bindir}|' \
             -e 's|^SBIN_PATH=.*|SBIN_PATH=%{_sbindir}|' \
             -e 's|^PBS_DAEMON=.*|PBS_DAEMON=%{_sbindir}/'"$PROG"'|' \
            contrib/init.d/$INIT_PREFIX$PROG > %{buildroot}%{_initrddir}/$PROG
    %{__chmod} 0755 %{buildroot}%{_initrddir}/$PROG
done

## Configuration
echo '__AC_HOSTNAME_NOT_SET__' > \
    %{buildroot}%{torque_sysconfdir}/server_priv/nodes
echo '$pbsserver __AC_HOSTNAME_NOT_SET__' > \
    %{buildroot}%{torque_sysconfdir}/mom_priv/config

# Moab requires libtorque.so.0, but works with libtorque.so.2, so fudge it.
%{__ln_s} libtorque.so.2 %{buildroot}%{_libdir}/libtorque.so.0

# We do not package the FIFO scheduler with our suites.
rm -rf %{buildroot}%{torque_spooldir}/sched_priv
rm -f %{buildroot}%{_initrddir}/pbs_sched
rm -f %{buildroot}%{_sbindir}/pbs_sched
rm -f %{buildroot}%{_sbindir}/qschedd
rm -rf %{buildroot}%{torque_spooldir}/sched_logs

# Empty config files

touch %{buildroot}%{torque_sysconfdir}/server_priv/nodes
touch %{buildroot}%{torque_appstatedir}/server_priv/serverdb
touch %{buildroot}%{torque_sysconfdir}/server_priv/mom_hierarchy

# %%ghost files

%{__install} -d %{buildroot}%{torque_appstatedir}/server_priv/bad_job_state
%{__install} -d %{buildroot}/etc/ld.so.conf.d
echo '%{_libdir}' > %{buildroot}/etc/ld.so.conf.d/torque.conf

%grep_safety_net "%{buildroot}" "%{buildroot}" ""
%grep_safety_net "%{buildroot}" "${HOSTNAME}" "__AC_HOSTNAME_NOT_SET__"
%grep_safety_net "%{buildroot}" "localhost" "__AC_HOSTNAME_NOT_SET__"

%pre %{common_sub}
TIMESTAMP="`date +%%Y.%%m.%%d_%%H.%%M.%%S`"
# This for loop enables globbing, which the macros do not support
%{pre_clear_back_up %{common_sub}-${TIMESTAMP}}
for file in %{_libdir}/lib%{project_name}.so.*
do
    %{pre_add_back_up_file ${file} %{common_sub}-${TIMESTAMP}}
done
%{pre_add_back_up_file %{pkg_doc_dir}/INSTALL %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/INSTALL.GNU %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/CHANGELOG %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/PBS_License.txt %{common_sub}-${TIMESTAMP}}
for file in %{pkg_doc_dir}/README.*
do
    %{pre_add_back_up_file ${file} %{common_sub}-${TIMESTAMP}}
done
%{pre_add_back_up_file %{pkg_doc_dir}/Release_Notes %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/src/pam/README.pam %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/doc/READ_ME %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/doc/doc_fonts %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/doc/soelim.c %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/doc/ers %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir  %{_docdir}/%{version} %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir  %{torque_spooldir}/spool %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir  %{torque_appstatedir}/checkpoint %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{torque_sysconfdir}/pbs_environment %{common_sub}-${TIMESTAMP}}
%{pre_add_back_up_file /etc/ld.so.conf.d/torque.conf %{common_sub}-${TIMESTAMP}}
%{pre_zip_back_up %{common_sub}-${TIMESTAMP}}

%post %{common_sub}
echo "  Running 'ldconfig'..."
ldconfig

%postun %{common_sub}
echo "  Running 'ldconfig'..."
ldconfig

%pre %{client_sub}
TIMESTAMP="`date +%%Y.%%m.%%d_%%H.%%M.%%S`"
%{pre_clear_back_up %{client_sub}-${TIMESTAMP}}
# Taken from the client's file list
%{pre_add_back_up_file %{_initrddir}/trqauthd %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/chk_tree %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/hostn %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/nqs2pbs %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/pbs_track %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/pbsdsh %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/pbsnodes %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/printjob %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/printserverdb %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/printtracking %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/printtracking %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/printtracking %{client_sub}-${TIMESTAMP}}
for file in %{_bindir}/q*
do
   %{pre_add_back_up_file ${file} %{client_sub}-${TIMESTAMP}}
done
%{pre_add_back_up_file %{_bindir}/tracejob %{client_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_sbindir}/trqauthd %{client_sub}-${TIMESTAMP}}
%{pre_zip_back_up %{client_sub}-${TIMESTAMP}}

%post %{client_sub}
echo "  Executing the '%{client_pkg}' post-install script..."
if [ $1 -eq 1 ]
then
    echo "  No other installation of '%{client_pkg}' detected on"
    echo "    the system."
    chkconfig --add trqauthd >/dev/null 2>&1 || :
    chkconfig trqauthd on >/dev/null 2>&1 || :
else
    echo "  Additional instance of '%{client_pkg}' detected on"
    echo "  the system."
fi

%preun %{client_sub}
echo "  Executing the '%{client_pkg}' pre-uninstall script..."
if [ $1 -eq 0 ]
then
    echo "  No other installation of '%{client_pkg} detected on"
    echo "  the system other than the one being uninstalled."
    echo "  Stopping the 'trqauthd' service..."
    chkconfig trqauthd off >/dev/null 2>&1 || :
    service trqauthd stop >/dev/null 2>&1 || :
    chkconfig --del trqauthd >/dev/null 2>&1 || :
fi

%pre %{server_sub}
TIMESTAMP="`date +%%Y.%%m.%%d_%%H.%%M.%%S`"
%{pre_clear_back_up %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/doc/admin_guide.ps %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{pkg_doc_dir}/torque.setup %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{torque_sysconfdir}/server_priv/mom_hierarchy \
                       %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{torque_sysconfdir}/server_name %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{torque_sysconfdir}/server_priv/nodes \
                       %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_initrddir}/pbs_server %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_sbindir}/pbs_server %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_sbindir}/qserverd %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir  %{torque_logdir}/server_logs %{server_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir  %{torque_appstatedir}/server_priv %{server_sub}-${TIMESTAMP}}
%{pre_zip_back_up %{server_sub}-${TIMESTAMP}}

%post %{server_sub}
if [ $1 -eq 1 ]
then
    echo "  No other installation of '%{server_pkg}' detected on"
    echo "  the system."
    echo "  Ensuring for the presence of the user '%{torque_user}'..."
    grep '^%{torque_user}:' /etc/passwd >/dev/null 2>&1 || \
         useradd -r %{torque_user} || :
    echo "  Looking for PBS services in '/etc/services'..."
    grep -q 'PBS services' /etc/services >/dev/null 2>&1 || {
        echo "  No PBS services found in '/etc/services'."
        echo "  Populating '/etc/services' with pbs service information..."
        cat <<EOF >>/etc/services
        # Standard PBS services
pbs           15001/tcp           # pbs server (pbs_server)
pbs           15001/udp           # pbs server (pbs_server)
pbs_mom       15002/tcp           # mom to/from server
pbs_mom       15002/udp           # mom to/from server
pbs_resmom    15003/tcp           # mom resource management requests
pbs_resmom    15003/udp           # mom resource management requests
pbs_sched     15004/tcp           # scheduler
pbs_sched     15004/udp           # scheduler
trqauthd      15005/tcp           # authorization daemon
trqauthd      15005/udp           # authorization daemon
EOF
    }

    %grep_safety_net "%{torque_home}" "__AC_HOSTNAME_NOT_SET__" "${HOSTNAME}"

    echo "`hostname` np=`grep processor /proc/cpuinfo | wc -l`" > \
        %{torque_sysconfdir}/server_priv/nodes

    echo "  Checking for the existence of the file"
    echo "    '%{torque_appstatedir}/server_priv/serverdb'..."
    if [ ! -s %{torque_appstatedir}/server_priv/serverdb ]
    then
        echo "  '%{torque_appstatedir}/server_priv/serverdb' does not"
        echo "    exist or is empty."
        export TORQUE_SERVER="${HOSTNAME}"
        echo "  Running '%{_docdir}/torque.setup' with first argument as"
        echo "    '%{torque_user}'..."
        yes 'y' | %{_docdir}/%{server_pkg}-%{version}/torque.setup \
            "%{torque_user}" >/dev/null

        qterm >/dev/null 2>&1 || :
    fi

    chkconfig --add pbs_server >/dev/null 2>&1 || :
    chkconfig pbs_server on >/dev/null 2>&1 || :
else
    echo "  Additional instance of '%{server_pkg}' detected on"
    echo "    the system."
fi

%preun %{server_sub}
echo "  Executing the '%{server_pkg}' pre-uninstall script..."
if [ $1 -eq 0 ]
then
    echo "  No other installation of '%{server_pkg}' detected on"
    echo "    the system other than the one being uninstalled."
    echo "  Stopping the 'pbs_server' service..."
    chkconfig pbs_server off >/dev/null 2>&1 || :
    service pbs_server stop >/dev/null 2>&1 || :
    chkconfig --del pbs_server >/dev/null 2>&1 || :
fi

%pre %{devel_sub}
TIMESTAMP="`date +%%Y.%%m.%%d_%%H.%%M.%%S`"
%{pre_clear_back_up %{devel_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_bindir}/pbs-config %{devel_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir  %{_includedir}/%{project_name} %{devel_sub}-${TIMESTAMP}}
for file in %{_libdir}/lib%{project_name}*a
do
    %{pre_add_back_up_file ${file} %{devel_sub}-${TIMESTAMP}}
done
for file in %{_libdir}/lib%{project_name}*so
do
    %{pre_add_back_up_file ${file} %{devel_sub}-${TIMESTAMP}}
done
%{pre_zip_back_up %{devel_sub}-${TIMESTAMP}}

%post %{devel_sub}
echo "  Running 'ldconfig'..."
ldconfig

%postun %{devel_sub}
echo "  Running 'ldconfig'..."
ldconfig

%pre %{mom_sub}
TIMESTAMP="`date +%%Y.%%m.%%d_%%H.%%M.%%S`"
%{pre_clear_back_up %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir %{torque_appstatedir}/mom_priv %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir %{torque_appstatedir}/aux %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir %{torque_logdir}/mom_logs %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_dir %{torque_spooldir}/undelivered %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{torque_sysconfdir}/mom_priv/config %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_initrddir}/pbs_mom %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_sbindir}/pbs_demux %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_sbindir}/pbs_mom %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_sbindir}/momctl %{mom_sub}-${TIMESTAMP}}
%{pre_add_back_up_file %{_sbindir}/qnoded %{mom_sub}-${TIMESTAMP}}
%if %{with pam}
%{pre_add_back_up_file /%{_lib}/security/pam_pbssimpleauth.so %{mom_sub}-${TIMESTAMP}}
%endif
%if %{with scp}
%{pre_add_back_up_file %{_sbindir}/pbs_rcp %{mom_sub}-${TIMESTAMP}}
%endif
%{pre_zip_back_up %{mom_sub}-${TIMESTAMP}}

%post %{mom_sub}
echo "  Executing the '%{mom_pkg}' post-install script..."
if [ $1 -eq 1 ]
then
    echo "  No other installation of '%{mom_pkg}' detected on"
    echo "    the system."
    echo "  Looking for PBS services in '/etc/services'..."
    grep -q 'PBS services' /etc/services >/dev/null 2>&1 || {
        echo "  No PBS services found in '/etc/services'."
        echo "  Populating '/etc/services' with pbs service information..."
        cat <<EOF >>/etc/services
# Standard PBS services
pbs           15001/tcp           # pbs server (pbs_server)
pbs           15001/udp           # pbs server (pbs_server)
pbs_mom       15002/tcp           # mom to/from server
pbs_mom       15002/udp           # mom to/from server
pbs_resmom    15003/tcp           # mom resource management requests
pbs_resmom    15003/udp           # mom resource management requests
pbs_sched     15004/tcp           # scheduler
pbs_sched     15004/udp           # scheduler
trqauthd      15005/tcp           # authorization daemon
trqauthd      15005/udp           # authorization daemon
EOF
    }

    %grep_safety_net "%{torque_home}" "__AC_HOSTNAME_NOT_SET__" "${HOSTNAME}"

    export TORQUE_SERVER="${HOSTNAME}"

    chkconfig --add pbs_mom >/dev/null 2>&1 || :
    chkconfig pbs_mom on >/dev/null 2>&1 || :
else
    echo "  Additional instance of '%{mom_pkg}' detected on"
    echo "    the system."
fi
echo "  Running 'ldconfig'..."
ldconfig

%preun %{mom_sub}
echo "  Executing the '%{mom_pkg}' pre-uninstall script..."
if [ $1 -eq 0 ]
then
    echo "  No other installation of '%{mom_pkg}' detected on"
    echo "    the system other than the one being uninstalled."
    echo "  Stopping the 'pbs_mom' service..."
    chkconfig pbs_mom off >/dev/null 2>&1 || :
    service pbs_mom stop >/dev/null 2>&1 || :
    chkconfig --del pbs_mom >/dev/null 2>&1 || :
fi

%postun %{mom_sub}
echo "  Running 'ldconfig'..."
ldconfig

%files

%files %{common_sub}
%attr(-,root,root) %{_libdir}/lib%{project_name}.so.*
%attr(-,root,root) %config(noreplace) %{torque_sysconfdir}/pbs_environment
%attr(-,root,root) %config(noreplace) /etc/ld.so.conf.d/torque.conf
%attr(-,root,root) %doc INSTALL INSTALL.GNU CHANGELOG PBS_License.txt README.*
%attr(-,root,root) %doc Release_Notes src/pam/README.pam
%attr(-,root,root) %doc doc/READ_ME doc/doc_fonts doc/soelim.c doc/ers
# This is needed by TORQUE MOM, but also by the server (pbsd_init). Therefore,
# it is in the 'common' RPM.
%attr(1777,root,root) %dir %{torque_spooldir}/spool
%attr(1777,root,root) %dir %{torque_appstatedir}/checkpoint

%files %{client_sub}
%attr(-,root,root) %config(noreplace) %{_initrddir}/trqauthd
%attr(-,root,root) %{_bindir}/chk_tree
%attr(-,root,root) %{_bindir}/hostn
%attr(-,root,root) %{_bindir}/nqs2pbs
%attr(-,root,root) %{_bindir}/pbs_track
%attr(-,root,root) %{_bindir}/pbsdsh
%attr(-,root,root) %{_bindir}/pbsnodes
%attr(-,root,root) %{_bindir}/printjob
%attr(-,root,root) %{_bindir}/printserverdb
%attr(-,root,root) %{_bindir}/printtracking
%attr(-,root,root) %{_bindir}/q*
%attr(-,root,root) %{_bindir}/tracejob
%attr(-,root,root) %{_sbindir}/trqauthd
%attr(-,root,root) %doc %{_mandir}/man*/*

%files %{server_sub}
%attr(-,root,root) %doc doc/admin_guide.ps
%attr(0755,root,root) %doc torque.setup
%attr(-,root,root) %config(noreplace) %{torque_sysconfdir}/server_priv/mom_hierarchy
%attr(-,root,root) %config(noreplace) %{torque_appstatedir}/server_priv/serverdb
%attr(-,root,root) %config(noreplace) %{torque_sysconfdir}/server_name
%attr(-,root,root) %config(noreplace) %{torque_sysconfdir}/server_priv/nodes
%attr(-,root,root) %config(noreplace) %{_initrddir}/pbs_server
%attr(-,root,root) %{_sbindir}/pbs_server
%attr(-,root,root) %{_sbindir}/qserverd
%attr(0755,root,root) %dir %{torque_logdir}/server_logs
%attr(0750,root,root) %dir %{torque_appstatedir}/server_priv
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/accounting
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/acl*
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/arrays
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/credentials
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/disallowed_types
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/hostlist
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/jobs
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/bad_job_state
%attr(-,root,root) %dir %{torque_appstatedir}/server_priv/queues

%files %{devel_sub}
%attr(-,root,root) %{_bindir}/pbs-config
%attr(-,root,root) %{_includedir}/%{project_name}
%attr(-,root,root) %{_libdir}/lib%{project_name}*a
%attr(-,root,root) %{_libdir}/lib%{project_name}*so

%files %{mom_sub}
%attr(-,root,root) %dir %{torque_appstatedir}/mom_priv
%attr(-,root,root) %dir %{torque_appstatedir}/aux
%attr(-,root,root) %dir %{torque_appstatedir}/mom_priv/jobs/
%attr(-,root,root) %dir %{torque_logdir}/mom_logs
%attr(-,root,root) %dir %{torque_spooldir}/undelivered
%attr(-,root,root) %config(noreplace) %{torque_sysconfdir}/mom_priv/config
%attr(-,root,root) %config(noreplace) %{_initrddir}/pbs_mom
%attr(-,root,root) %{_sbindir}/pbs_demux
%attr(-,root,root) %{_sbindir}/pbs_mom
%attr(-,root,root) %{_sbindir}/momctl
%attr(-,root,root) %{_sbindir}/qnoded
%if %{with pam}
%attr(-,root,root) /%{_lib}/security/pam_pbssimpleauth.so
%endif
%if %{without scp}
%attr(4755, root, root) %{_sbindir}/pbs_rcp
%endif
