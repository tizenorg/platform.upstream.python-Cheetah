Name:           python-Cheetah
Version:        2.4.4
Release:        0
Url:            http://www.cheetahtemplate.org/
Summary:        Cheetah is a template engine and code generation tool
License:        MIT
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/C/Cheetah/Cheetah-%{version}.tar.gz
Source1001: 	python-Cheetah.manifest
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  python-devel
Provides:       python-cheetah = %{version}
Obsoletes:      python-cheetah < %{version}

%description
Cheetah is an open source template engine and code generation tool.

It can be used standalone or combined with other tools and frameworks. Web
development is its principle use, but Cheetah is very flexible and is also being
used to generate C++ game code, Java, sql, form emails and even Python code.

%prep
%setup -q -n Cheetah-%{version}
cp %{SOURCE1001} .
# Remove she-bang lines for non-executable scripts:
sed -i "1d" cheetah/{Tests/{Unicode,Filters,Parser,Template,Regressions,Cheps,Analyzer,Test,Misc,CheetahWrapper,SyntaxAndOutput,NameMapper,Performance},ImportHooks,Utils/Misc,Servlet,NameMapper,Parser,DirectiveAnalyzer}.py

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/cheetah*
%python_sitearch/*

%changelog
