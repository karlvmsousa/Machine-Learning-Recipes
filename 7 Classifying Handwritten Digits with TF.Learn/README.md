## Running the .ipyntb file
![image](https://user-images.githubusercontent.com/31048109/58753385-ba788e80-8494-11e9-99e0-0799820ae925.png)

### Google Colab
A Google cloud option to run the .ipyntb files. You just need to upload the file and then, you already can use it, without installing tensor flow, because Google Colba already have the main libraries pre-installed. The file can be stored in your Drive.

### Jupyter
Considering that you want to run the .ipyntb in Jupyter, before open it to use the code normally, we have to run the following commands:

Using the linux terminal:
```shell
$ sudo apt install anaconda
$ conda create -n tensorflow_env tensorflow
$ conda activate tenssorflow_env
```
Now will be desplayed `(tensorflow_env)` before your username at the terminal. Then we have to install the jupyter and the libraries/modules in this enviroment, in order to be able to import them in the jupyter notebook:

```shell
$ pip install jupyter tensorflow numpy pandas
$ jupyter notebook
```
At the end, a browser will be opened (or it will be given a url), so you can navigate over the directiories and open the jupyter notebook file.
