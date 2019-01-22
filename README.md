<div align="center">
<img src="https://user-images.githubusercontent.com/7585388/27636865-e6505c60-5c0d-11e7-92d1-1adc1ac81a11.png" height="100" >
</div>

<h1 align="center">
  Uptime Performance CLI
</h1>

<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#requirements">Requirements</a></li>
  <li><a href="#Installation">Installation</a></li>
  <li><a href="#contribution">Contribution</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h1 id="overview">Overview</h1>
<p style="font-size: 20px">
  This project is a system performance metric cli based on python to monitor
  system metrics and ping a server to check if its up or down. The cli is
  modular and additional functionality can be added or removed according to the
  files.
</p>

<h1 id="requirements">Requirements</h1>

```
python >= 3.5;
pip >= 15;
```

<p style="font-size:18px">After installing python and pip and adding it to the path, enter the following code to create a virtual environment. 
<br>
Its best to use a virtual environment to stop polluting the global dependency space
</p>

```shell
$ pip install virtualenv
```

Then create an environment

```shell
$ virtualenv environment_name
```

Then activate the environment with:

```shell
$ source environment_name/bin/activate
```

<h1 id="Installation">Installation</h1>

<p>After in the virtual environment run the following code to install all the dependencies:

```shell
$ pip install -r requirements.txt
```

</p>

After installation run the following code from the same directory

```shell
$ python app.py
```

### Thats it!!!

<h1 id="contribution">Contribution</h1>
If you want to contribute feel free to submit a pr. If you want to use this *cli* in your project then follow the code below:

```python
# Dependencies
>>> import cli

# Then create a cli object
>>> obj = cli.CLI()  # This will fire up the cli
```

#### Make Sure to use Error Handling to handle any errors.

For more details see [app.py](https://github.com/Ayanrocks/uptime_performance_cli/blob/master/app.py)

# License

### GNU General Public License
