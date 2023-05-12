from setuptools import setup

setup(
    name='my-streamlit-app',
    version='0.1',
    packages=['myapp'],
    include_package_data=True,
    install_requires=[
        'streamlit'
    ],
    entry_points={
        'console_scripts': [
            'myapp = myapp.__main__:main'
        ]
    }
)
