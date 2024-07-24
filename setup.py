from setuptools import setup, find_packages

setup(
    name='persian_sms_manager',
    version='1.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    description='A package for managing Iranian SMS services',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Abbas Rahimzadeh',
    author_email='arahimzadeh@gmail.com',
    url='https://github.com/AAbbasRR/persianSMSManager.git',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
